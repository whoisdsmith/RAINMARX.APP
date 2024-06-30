# RAINMARX

![](banner.jpg)

Welcome to RAINMARX, your ultimate CLI tool for managing Raindrop.io bookmarks. This application allows you to interact with your Raindrop.io account through various functionalities such as fetching bookmarks, updating collections, searching, and more.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Scripts Overview](#scripts-overview)
- [Logging](#logging)
- [Contributing](#contributing)
- [License](#license)

## Features
- Fetch all bookmarks and nested collections.
- Retrieve parent collections by ID.
- Update bookmarks within a collection.
- Search bookmarks.
- Get user statistics.
- Manage user collection groups.

## Installation

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

1. **API Token:**
   - Update the `config.py` file with your Raindrop.io API token.

     ```python
     api_token = 'your_api_token_here'
     headers = {
         'Authorization': f'Bearer {api_token}',
         'Content-Type': 'application/json'
     }
     ```

   Alternatively, you can set your API token as an environment variable and modify `config.py` to read from it:

     ```python
     import os

     api_token = os.getenv('RAINDROP_API_TOKEN')
     headers = {
         'Authorization': f'Bearer {api_token}',
         'Content-Type': 'application/json'
     }
     ```

2. **Logging Configuration:**
   - Configure logging as per your requirements in the `utils.py` file.

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

## Scripts Overview

- **RAINMARX.py**: Main entry point of the application, displaying the menu and handling user inputs.
- **config.py**: Contains API token and headers configuration.
- **collectid.py**: Handles retrieval of parent collections by ID.
- **group.py**: Manages user collection groups.
- **nested.py**: Fetches all bookmarks and nested collections.
- **overview.py**: Provides an overview of collections.
- **search.py**: Handles search functionality.
- **stats.py**: Retrieves user statistics.
- **updatr.py**: Updates bookmarks within a collection.
- **utils.py**: Contains utility functions, including logging configuration.

## Logging

Logging is configured in `utils.py`. You can customize the logging level and format as needed. The logs are saved in the `logs` directory.

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

## Documentation

Complete documentaiton can be found in the `docs` directory.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

