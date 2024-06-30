import aiohttp
import asyncio
import logging
from bs4 import BeautifulSoup
from config import headers
from utils import configure_logging, read_json, sanitize_text

BASE_URL = "https://api.raindrop.io/rest/v1"


async def fetch(session, url):
    logging.info(f"Fetching title and excerpt from URL: {url}")
    try:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            text = await response.text()
            soup = BeautifulSoup(text, 'html.parser')
            title = soup.title.string if soup.title else url
            meta_description = soup.find('meta', attrs={'name': 'description'})
            excerpt = meta_description['content'] if meta_description else title
            logging.info(f"Fetched title: {title}")
            logging.info(f"Fetched excerpt: {excerpt}")
            return title, excerpt
    except Exception as e:
        logging.warning(f"Error fetching data from URL {url}: {e}")
        return url, url


async def sanitize_bookmark(bookmark, session):
    url = bookmark.get('link', '')
    logging.info(f"Processing bookmark with URL: {url}")
    title, excerpt = await fetch(session, url)
    sanitized_title = sanitize_text(title)
    sanitized_excerpt = sanitize_text(excerpt)
    bookmark['title'] = sanitized_title
    bookmark['excerpt'] = sanitized_excerpt
    logging.info(f"Updated bookmark: {bookmark}")
    return bookmark


async def update_bookmark(session, bookmark):
    bookmark_id = bookmark['_id']
    url = f"{BASE_URL}/raindrop/{bookmark_id}"
    data = {
        'title': bookmark['title'],
        'excerpt': bookmark['excerpt']
    }
    try:
        async with session.put(url, json=data, headers=headers) as response:
            if response.status == 429:
                logging.warning(f"Rate limit hit for bookmark ID {
                                bookmark_id}. Sleeping for a bit before retrying...")
                await asyncio.sleep(60)
                async with session.put(url, json=data, headers=headers) as retry_response:
                    retry_response.raise_for_status()
                    logging.info(f"Updated bookmark ID {
                                 bookmark_id} successfully on retry")
            else:
                response.raise_for_status()
                logging.info(f"Updated bookmark ID {bookmark_id} successfully")
    except Exception as e:
        logging.error(f"Error updating bookmark ID {bookmark_id}: {e}")


async def process_bookmark(bookmark, session):
    try:
        updated_bookmark = await sanitize_bookmark(bookmark, session)
        await update_bookmark(session, updated_bookmark)
        return True
    except Exception as e:
        logging.error(f"Error processing bookmark {bookmark.get('_id')}: {e}")
        return False


async def process_collection(collection, session):
    logging.info(f"Processing collection ID: {collection.get('_id')}")
    tasks = [process_bookmark(bookmark, session)
             for bookmark in collection['raindrops']]
    await asyncio.gather(*tasks)


async def main():
    configure_logging('updatr')
    input_file = input("Enter the name of the JSON file: ")
    nested_structure = read_json(input_file)
    async with aiohttp.ClientSession() as session:
        try:
            tasks = [process_collection(collection, session) for collection in nested_structure.values(
            ) if isinstance(collection, dict)]
            await asyncio.gather(*tasks)
            logging.info("Sanitization and update process completed.")
        except Exception as e:
            logging.error(f"Error during the main process: {e}")

if __name__ == "__main__":
    asyncio.run(main())
