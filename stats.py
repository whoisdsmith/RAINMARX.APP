import requests
import json
import os
import logging
from datetime import datetime
from config import headers

# Set up logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir, 'stats.log'),
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s:%(message)s')

# Base URL for the Raindrop.io API
base_url = 'https://api.raindrop.io/rest/v1'


def get_system_collections_count():
    logging.debug('Fetching system collections count')
    url = f'{base_url}/user/stats'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        logging.debug(f'System collections count response: {
                      json.dumps(data, indent=4)}')
        try:
            return data
        except KeyError as e:
            logging.error(f'KeyError: {e}')
            return None
    else:
        logging.error(f'Error fetching system collections count: {
                      response.status_code}')
        return None


# Execute the function
logging.info('Starting data retrieval')
stats_data = get_system_collections_count()

# Print the results
if stats_data:
    print('System Collections Count:', stats_data)
else:
    print('Failed to retrieve system collections count.')

# Ensure the stats directory exists
os.makedirs('stats', exist_ok=True)

# Generate a timestamped filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'stats/system_collections_stats_{timestamp}.json'

# Write the data to the JSON file
with open(filename, 'w') as f:
    json.dump(stats_data, f, indent=4)

logging.info(f'Results saved to {filename}')
print(f'Results saved to {filename}')
