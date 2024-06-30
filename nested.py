import requests
import json
import os
import logging
import time
from datetime import datetime, timedelta
from config import headers
from utils import configure_logging

BASE_URL = "https://api.raindrop.io/rest/v1"
RATE_LIMIT = 120  # Maximum number of requests per minute
REQUEST_DELAY = 60 / RATE_LIMIT  # Delay between requests in seconds


def get_collections():
    logging.debug("Fetching root collections")
    response = requests.get(f"{BASE_URL}/collections", headers=headers)
    response.raise_for_status()
    collections_data = response.json()['items']
    logging.info(f"Fetched {len(collections_data)} root collections")
    time.sleep(REQUEST_DELAY)  # Delay to prevent rate limit
    return collections_data


def get_child_collections():
    logging.debug("Fetching child collections")
    response = requests.get(
        f"{BASE_URL}/collections/childrens", headers=headers)
    response.raise_for_status()
    child_collections_data = response.json()['items']
    logging.info(f"Fetched {len(child_collections_data)} child collections")
    time.sleep(REQUEST_DELAY)  # Delay to prevent rate limit
    return child_collections_data


def fetch_bookmarks_by_collection(collection_id):
    logging.debug(f"Fetching bookmarks for collection {collection_id}")
    bookmarks = []
    page = 0
    more_bookmarks = True

    while more_bookmarks:
        response = requests.get(
            f"{BASE_URL}/raindrops/{collection_id}?page={page}&perpage=50", headers=headers)
        response.raise_for_status()
        data = response.json()
        bookmarks.extend(data['items'])

        if len(data['items']) < 50:
            more_bookmarks = False

        page += 1
        logging.debug(f"Page {page} for collection {collection_id}: Fetched {
                      len(data['items'])} bookmarks")
        time.sleep(REQUEST_DELAY)  # Delay to prevent rate limit

    logging.info(f"Fetched total {len(bookmarks)
                                  } bookmarks for collection {collection_id}")
    return bookmarks


def retrieve_all_bookmarks():
    logging.info("Starting retrieval of all bookmarks")
    root_collections = get_collections()
    child_collections = get_child_collections()
    all_collections = root_collections + child_collections
    all_bookmarks = []

    start_time = time.time()

    for index, collection in enumerate(all_collections):
        logging.info(f"Processing collection {
                     collection['_id']} ({collection['title']})")
        collection_start_time = time.time()
        collection_bookmarks = fetch_bookmarks_by_collection(collection['_id'])
        all_bookmarks.extend(collection_bookmarks)

        elapsed_time = time.time() - start_time
        collection_elapsed_time = time.time() - collection_start_time
        logging.info(f"Processed collection {index + 1}/{len(all_collections)}: {collection['_id']} ({collection['title']}). "
                     f"Bookmarks: {len(collection_bookmarks)}. "
                     f"Time taken: {
                         timedelta(seconds=collection_elapsed_time)}. "
                     f"Total bookmarks so far: {len(all_bookmarks)}. "
                     f"Elapsed time: {timedelta(seconds=elapsed_time)}")

    return all_bookmarks


def main():
    configure_logging('nested')
    logging.info("Starting bookmark retrieval")
    start_time = time.time()

    all_bookmarks = retrieve_all_bookmarks()

    # Ensure the collections directory exists
    os.makedirs('collections', exist_ok=True)

    # Filename for the JSON output
    filename = 'collections/nested.json'

    # Write the data to the JSON file
    with open(filename, 'w') as outfile:
        json.dump(all_bookmarks, outfile, indent=4)

    elapsed_time = time.time() - start_time
    logging.info(f"Bookmark retrieval completed in {
                 timedelta(seconds=elapsed_time)}")
    print(f"Results saved to {filename}")


if __name__ == "__main__":
    main()
