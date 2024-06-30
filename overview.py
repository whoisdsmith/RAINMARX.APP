import requests
import json
import os
import logging
from datetime import datetime
from config import headers

# Set up logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'raindrop_overview.log'),
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Base URL for the Raindrop.io API
base_url = 'https://api.raindrop.io/rest/v1'


def get_user_stats():
    logging.debug('Fetching user stats')
    url = f'{base_url}/user/stats'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        logging.debug(f'User stats response data: {
                      json.dumps(data, indent=4)}')
        try:
            total_bookmarks = next(item['count']
                                   for item in data['items'] if item['_id'] == 0)
            unsorted_bookmarks = next(
                item['count'] for item in data['items'] if item['_id'] == -1)
            trash_bookmarks = next(item['count']
                                   for item in data['items'] if item['_id'] == -99)
            total_files = data['meta']['files']['used'] if 'files' in data['meta'] else None
            logging.info(f'Total bookmarks: {total_bookmarks}')
            logging.info(f'Unsorted bookmarks: {unsorted_bookmarks}')
            logging.info(f'Trash bookmarks: {trash_bookmarks}')
            logging.info(f'Total files (size in bytes): {total_files}')
            return total_bookmarks, unsorted_bookmarks, trash_bookmarks, total_files
        except KeyError as e:
            logging.error(f'KeyError: {e}')
            return None, None, None, None
    else:
        logging.error(f'Error fetching user stats: {response.status_code}')
        return None, None, None, None


def get_root_collections():
    logging.debug('Fetching root collections')
    url = f'{base_url}/collections'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_root_collections = len(data['items'])
        logging.info(f'Total root collections: {total_root_collections}')
        return data['items'], total_root_collections
    else:
        logging.error(f'Error fetching root collections: {
                      response.status_code}')
        return None, None


def get_child_collections():
    logging.debug('Fetching child collections')
    url = f'{base_url}/collections/childrens'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        total_child_collections = len(data['items'])
        logging.info(f'Total child collections: {total_child_collections}')
        return data['items'], total_child_collections
    else:
        logging.error(f'Error fetching child collections: {
                      response.status_code}')
        return None, None


def calculate_bookmarks_per_collection(root_collections, child_collections):
    bookmarks_per_collection = {}
    if root_collections:
        for collection in root_collections:
            bookmarks_per_collection[collection['_id']] = collection['count']
            logging.info(f'Root collection {collection["_id"]}: {
                         collection["count"]} bookmarks')
    if child_collections:
        for collection in child_collections:
            bookmarks_per_collection[collection['_id']] = collection['count']
            logging.info(f'Child collection {collection["_id"]}: {
                         collection["count"]} bookmarks')
    return bookmarks_per_collection


# Execute the functions
logging.info('Starting data retrieval')
total_bookmarks, unsorted_bookmarks, trash_bookmarks, total_files = get_user_stats()
root_collections, total_root_collections = get_root_collections()
child_collections, total_child_collections = get_child_collections()
bookmarks_per_collection = calculate_bookmarks_per_collection(
    root_collections, child_collections)

# Print the results
print(f'Total Bookmarks: {total_bookmarks}')
print(f'Unsorted Bookmarks: {unsorted_bookmarks}')
print(f'Trash Bookmarks: {trash_bookmarks}')
print(f'Total Collections: {total_root_collections + total_child_collections}')
print(f'Total Files (Size in Bytes): {total_files}')
print('Bookmarks per Collection:')
for collection_id, count in bookmarks_per_collection.items():
    print(f'  {collection_id}: {count}')

# Prepare the data for JSON output
output_data = {
    'total_bookmarks': total_bookmarks,
    'unsorted_bookmarks': unsorted_bookmarks,
    'trash_bookmarks': trash_bookmarks,
    'total_collections': total_root_collections + total_child_collections,
    'total_files': total_files,
    'bookmarks_per_collection': bookmarks_per_collection
}

# Ensure the overviews directory exists
os.makedirs('overviews', exist_ok=True)

# Generate a timestamped filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'overviews/overview_{timestamp}.json'

# Write the data to the JSON file
with open(filename, 'w') as f:
    json.dump(output_data, f, indent=4)

logging.info(f'Results saved to {filename}')
print(f'Results saved to {filename}')
