# Detailed Script Descriptions

This section provides detailed descriptions of each script in the RAINMARX CLI application. Each script has a specific purpose and functionality, working together to provide comprehensive bookmark management capabilities.

## `RAINMARX.py`

### Description

`RAINMARX.py` is the main entry point for the RAINMARX CLI application. It initializes the application, displays a menu of options to the user, and handles user input to execute the corresponding scripts.

### Key Components

- **Initialization**: Sets up the CLI environment and prints the welcome message using ASCII art.
- **Menu Display**: Presents a list of options for the user to choose from.
- **Subprocess Execution**: Uses `subprocess.run()` to call other scripts based on user input.

### Usage

Run the script with:

```bash
python RAINMARX.py
```

Select an option from the menu to perform various operations on your Raindrop.io bookmarks.

## `config.py`

### Description

`config.py` contains configuration settings for the application, primarily focusing on the API token and headers required for authenticating with the Raindrop.io API.

### Key Components

- **API Token**: Stores the API token used for authentication.
- **Headers**: Defines the HTTP headers for API requests, including the authorization header with the API token.

### Example

```python
api_token = 'your_api_token_here'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}
```

## `collectid.py`

### Description

`collectid.py` handles the retrieval of parent collections by their ID. It allows users to fetch details of specific collections by providing the collection ID.

### Key Components

- **Fetch Collection by ID**: Sends a request to the Raindrop.io API to retrieve the specified collection.
- **User Input**: Prompts the user to enter a collection ID.

### Example

Run the script and enter the collection ID when prompted:

```bash
python collectid.py
```

## `group.py`

### Description

`group.py` manages user collection groups. This script is responsible for organizing related collections into groups.

### Key Components

- **Fetch Groups**: Retrieves the user's collection groups from the Raindrop.io API.
- **Display Groups**: Outputs the groups for the user to view.

### Example

Run the script to fetch and display collection groups:

```bash
python group.py
```

## `nested.py`

### Description

`nested.py` fetches all bookmarks and nested collections from Raindrop.io. This script handles pagination and ensures that all bookmarks are retrieved, regardless of their nested structure.

### Key Components

- **Fetch Collections**: Retrieves root and child collections.
- **Fetch Bookmarks**: Iterates through collections to fetch all bookmarks, handling pagination as needed.
- **Save to JSON**: Saves the retrieved bookmarks and collections to a JSON file for easy access.

### Example

Run the script to fetch all bookmarks and nested collections:

```bash
python nested.py
```

The results are saved in `collections/nested.json`.

## `overview.py`

### Description

`overview.py` provides an overview of the user's collections. It summarizes the contents of each collection, giving a quick snapshot of the user's bookmark organization.

### Key Components

- **Fetch Overview**: Retrieves data about collections and their contents.
- **Display Overview**: Outputs a summary of each collection.

### Example

Run the script to get an overview of your collections:

```bash
python overview.py
```

## `search.py`

### Description

`search.py` handles search functionality within the user's bookmarks. It allows users to search for specific bookmarks using keywords.

### Key Components

- **User Input**: Prompts the user to enter search keywords.
- **Search Bookmarks**: Sends a request to the Raindrop.io API to search for bookmarks matching the keywords.
- **Display Results**: Outputs the search results.

### Example

Run the script and enter search keywords when prompted:

```bash
python search.py
```

## `stats.py`

### Description

`stats.py` retrieves user statistics from Raindrop.io. It provides insights into the user's bookmark usage, such as the number of bookmarks and collections.

### Key Components

- **Fetch Statistics**: Sends a request to the Raindrop.io API to retrieve user statistics.
- **Display Statistics**: Outputs the statistics for the user to view.

### Example

Run the script to get user statistics:

```bash
python stats.py
```

## `updatr.py`

### Description

`updatr.py` allows users to update bookmarks within a specified collection. Users can modify attributes such as titles, URLs, and tags.

### Key Components

- **User Input**: Prompts the user to enter the collection ID and the details to update.
- **Update Bookmarks**: Sends requests to the Raindrop.io API to update the specified bookmarks.

### Example

Run the script and follow the prompts to update bookmarks:

```bash
python updatr.py
```

## `utils.py`

### Description

`utils.py` contains utility functions that are used across other scripts in the RAINMARX application. These functions include logging configuration and other common tasks.

### Key Components

- **Configure Logging**: Sets up logging for the application, ensuring that log messages are written to files.
- **Common Utilities**: Provides helper functions that can be used by other scripts.

### Example

Logging configuration in `utils.py`:

```python
import logging
import os

def configure_logging(script_name):
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_filename = os.path.join(log_dir, f'{script_name}.log')

    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
```


---

[<- Previous](04-Usage.md) | [Next ->](06-Logging.md)
