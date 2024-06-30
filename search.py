import requests
import config
import json
import os

BASE_URL = 'https://api.raindrop.io/rest/v1'


def save_results(query, results):
    # Create searchresults directory if it doesn't exist
    os.makedirs('searchresults', exist_ok=True)

    # Sanitize the query for use in a filename
    sanitized_query = "".join(c if c.isalnum() else "_" for c in query)
    filename = f"searchresults/{sanitized_query}.json"

    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Results saved to {filename}")


def search_collections(query):
    url = f"{BASE_URL}/collections"
    response = requests.get(url, headers=config.headers)
    try:
        collections = response.json().get('items', [])
        result = [col for col in collections if query.lower()
                  in col['title'].lower()]
        save_results(query, result)
        return result
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        print(f"Response content: {response.text}")
        return []


def search_bookmarks(query):
    # Fetch all collections to search within them
    collections_url = f"{BASE_URL}/collections"
    collections_response = requests.get(
        collections_url, headers=config.headers)
    try:
        collections = collections_response.json().get('items', [])
    except requests.exceptions.JSONDecodeError as e:
        print(f"Error decoding JSON response for collections: {e}")
        print(f"Response content: {collections_response.text}")
        return []

    result = []
    for collection in collections:
        collection_id = collection['_id']
        url = f"{BASE_URL}/raindrops/{collection_id}"
        response = requests.get(url, headers=config.headers)
        try:
            bookmarks = response.json().get('items', [])
            result.extend([bm for bm in bookmarks if query.lower() in bm['title'].lower() or
                           query.lower() in bm['excerpt'].lower() or query.lower() in bm['tags'] or
                           query.lower() in bm['link'].lower()])
        except requests.exceptions.JSONDecodeError as e:
            print(f"Error decoding JSON response for bookmarks in collection {collection_id}: {e}")
            print(f"Response content: {response.text}")

    save_results(query, result)
    return result


def cli_search():
    while True:
        print("\nSearch CLI")
        print("1. Search Collections")
        print("2. Search Bookmarks")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            query = input("Enter collection name or ID to search: ")
            search_collections(query)

        elif choice == '2':
            query = input(
                "Enter bookmark name, tag, URL, excerpt, note title, or date to search: ")
            search_bookmarks(query)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cli_search()
