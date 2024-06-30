import os
import requests
import json
import logging
from config import headers
from utils import configure_logging, read_json

BASE_URL = "https://api.raindrop.io/rest/v1"


def get_collection(collection_id):
    response = requests.get(
        f"{BASE_URL}/collection/{collection_id}", headers=headers)
    response.raise_for_status()
    return response.json()['item']


def get_raindrops(collection_id):
    response = requests.get(
        f"{BASE_URL}/raindrops/{collection_id}", headers=headers)
    response.raise_for_status()
    return response.json()['items']


def retrieve_collection_structure(collection_id):
    collection = get_collection(collection_id)
    collection_title = collection['title']
    raindrops = get_raindrops(collection_id)
    collection_structure = {
        'id': collection_id,
        'title': collection_title,
        'raindrops': raindrops
    }
    return collection_structure


def main():
    configure_logging('collectid')
    collection_id = input("Enter the parent collection ID: ")
    collection_structure = retrieve_collection_structure(collection_id)
    filename = f"{collection_structure['title']}.json".replace(
        " ", "_").replace("/", "_")

    # Create collections directory if it doesn't exist
    os.makedirs('collections', exist_ok=True)
    filepath = os.path.join('collections', filename)

    with open(filepath, 'w') as outfile:
        json.dump(collection_structure, outfile, indent=4)
    logging.info("Collection retrieval completed.")


if __name__ == "__main__":
    main()
