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


def get_user_collection_groups():
    logging.debug('Fetching user collection groups')
    url = f'{base_url}/user'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        logging.debug(f'User data response: {json.dumps(user_data, indent=4)}')
        try:
            user_groups = user_data['user']['groups']
            logging.info(f'Number of groups: {len(user_groups)}')
            return user_groups
        except KeyError as e:
            logging.error(f'KeyError: {e}')
            return []
    else:
        logging.error(f'Error fetching user collection groups: {
                      response.status_code}')
        return []


# Execute the function
logging.info('Starting data retrieval')
user_groups = get_user_collection_groups()

# Check if the user has any collection groups and print the results
if user_groups:
    for group in user_groups:
        print('Group Title:', group['title'])
        print('Collection IDs:', group['collections'])
        print('---')  # Separator between groups
else:
    print('This user has no collection groups.')

# Prepare the data for JSON output
output_data = {
    'user_groups': user_groups
}

# Ensure the overviews directory exists
os.makedirs('overviews', exist_ok=True)

# Generate a timestamped filename
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'overviews/collection_groups_{timestamp}.json'

# Write the data to the JSON file
with open(filename, 'w') as f:
    json.dump(output_data, f, indent=4)

logging.info(f'Results saved to {filename}')
print(f'Results saved to {filename}')
