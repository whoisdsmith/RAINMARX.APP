import logging
import json
import requests
from utils import configure_logging, read_json
from config import headers
import sys
import os
# Adjust sys.path to include the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


BASE_URL = "https://api.raindrop.io/rest/v1"


def get_collections():
    response = requests.get(f"{BASE_URL}/collections", headers=headers)
    response.raise_for_status()
    return response.json()['items']


def get_raindrops(collection_id):
    response = requests.get(
        f"{BASE_URL}/raindrops/{collection_id}", headers=headers)
    response.raise_for_status()
    return response.json()['items']


def retrieve_nested_structure():
    collections = get_collections()
    nested_structure = {}
    for collection in collections:
        collection_id = collection['_id']
        collection_title = collection['title']
        raindrops = get_raindrops(collection_id)
        nested_structure[collection_title] = {
            'id': collection_id,
            'raindrops': raindrops
        }
    return nested_structure


def main():
    configure_logging('nested')
    nested_structure = retrieve_nested_structure()
    with open('nested_structure.json', 'w') as outfile:
        json.dump(nested_structure, outfile, indent=4)
    logging.info("Nested structure retrieval completed.")


if __name__ == "__main__":
    main()
