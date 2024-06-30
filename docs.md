# RAINMARX Documentation

## Introduction

RAINMARX is a Command Line Interface (CLI) tool designed to help you manage your Raindrop.io bookmarks efficiently. With RAINMARX, you can fetch, update, search, and organize your bookmarks and collections seamlessly through the command line.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Detailed Script Descriptions](#detailed-script-descriptions)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

- Python 3.6 or higher
- Git

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/RAINMARX.git
   cd RAINMARX
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### API Token

1. Obtain your Raindrop.io API token from the Raindrop.io developer portal.
2. Update the `config.py` file with your API token:

    ```python
    api_token = 'your_api_token_here'
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    ```

    Alternatively, use an environment variable to store your API token:

    ```python
    import os

    api_token = os.getenv('RAINDROP_API_TOKEN')
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    ```

### Logging Configuration

Configure logging settings in `utils.py` according to your preferences. The default configuration logs to a file in the `logs` directory.

## Usage

Run the main script to start the CLI application:

```bash
python RAINMARX.py
```

You will be presented with a menu of options:

1. Get all bookmarks and nested collections.
2. Get parent collection by ID.
3. Update bookmarks from a collection.
4. Search.
5. Get user stats.
6. Get user collection groups.
7. Exit.

Choose the desired option by entering the corresponding number.

## Detailed Script Descriptions

### `RAINMARX.py`

This is the main script that initializes the CLI application and presents the user with a menu of options. It uses `subprocess.run()` to execute the appropriate scripts based on user input.

### `config.py`

Contains configuration settings, primarily the API token and headers required for authenticating with the Raindrop.io API.

### `collectid.py`

Handles the retrieval of parent collections by ID. This script is called when the user selects the option to get a parent collection by ID.

### `group.py`

Manages user collection groups. This script is responsible for grouping related collections together.

### `nested.py`

Fetches all bookmarks and nested collections from Raindrop.io. This script handles the heavy lifting of paginating through API responses to retrieve all bookmarks.

### `overview.py`

Provides an overview of collections. This script summarizes the collections and their contents.

### `search.py`

Handles search functionality within the user's bookmarks. This script allows users to search for specific bookmarks based on keywords.

### `stats.py`

Retrieves user statistics, providing insights into the user's Raindrop.io usage and bookmark data.

### `updatr.py`

Updates bookmarks within a collection. This script allows for modification of bookmarks, such as updating titles or URLs.

### `utils.py`

Contains utility functions, including logging configuration. This script is used across other scripts for common functionality.

## Logging

Logging is configured in `utils.py`. You can customize the logging level and format as needed. Logs are saved in the `logs` directory.

```python
import logging

def configure_logging(script_name):
    log_filename = f'logs/{script_name}.log'
    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
```

## Troubleshooting

### Common Issues

1. **Invalid API Token**:
   - Ensure your API token is correctly entered in `config.py`.
   - Check that your API token has the necessary permissions.

2. **Rate Limiting**:
   - The Raindrop.io API has a rate limit. If you encounter rate limiting errors, try increasing the `REQUEST_DELAY` in `nested.py`.

3. **Connection Errors**:
   - Check your internet connection.
   - Ensure the Raindrop.io API is accessible.

### Logs

Check the log files in the `logs` directory for detailed error messages and troubleshooting information.

