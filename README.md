# RAINMARX

## Description

RAINMARX is a Python application designed to interact with the Raindrop.io API. It provides various functionalities to manage and update your bookmarks and collections in Raindrop.io.

## Scripts

1. **nested.py** - Collects all bookmarks and nested collections and outputs the results to a JSON file.
2. **collectid.py** - Prompts the user for a parent collection ID number and outputs the results to a JSON file named after the parent collection.
3. **updatr.py** - Asks for a JSON file created by `collectid.py` for a parent collection and all its child collections and bookmarks. It retrieves the title and excerpt from each URL, sanitizes the results, and updates them back to the collection in Raindrop.io.
4. **config.py** - Contains the configuration for the API key and headers.
5. **utils.py** - Provides utility functions for logging, reading JSON, and sanitizing text.

## Requirements

- Python 3.x
- Requests library

## Installation

Install the required libraries using the following command:

# Usage

1. Run `nested.py` to collect all bookmarks and nested collections.
2. Run `collectid.py` to collect bookmarks from a specific parent collection.
3. Run `updatr.py` to update the titles and excerpts of bookmarks in a collection.

