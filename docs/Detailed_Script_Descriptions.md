# Detailed Script Descriptions

## `RAINMARX.py`

This is the main script that initializes the CLI application and presents the user with a menu of options. It uses `subprocess.run()` to execute the appropriate scripts based on user input.

## `config.py`

Contains configuration settings, primarily the API token and headers required for authenticating with the Raindrop.io API.

## `collectid.py`

Handles the retrieval of parent collections by ID. This script is called when the user selects the option to get a parent collection by ID.

## `group.py`

Manages user collection groups. This script is responsible for grouping related collections together.

## `nested.py`

Fetches all bookmarks and nested collections from Raindrop.io. This script handles the heavy lifting of paginating through API responses to retrieve all bookmarks.

## `overview.py`

Provides an overview of collections. This script summarizes the collections and their contents.

## `search.py`

Handles search functionality within the user's bookmarks. This script allows users to search for specific bookmarks based on keywords.

## `stats.py`

Retrieves user statistics, providing insights into the user's Raindrop.io usage and bookmark data.

## `updatr.py`

Updates bookmarks within a collection. This script allows for modification of bookmarks, such as updating titles or URLs.

## `utils.py`

Contains utility functions, including logging configuration. This script is used across other scripts for common functionality.
