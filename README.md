# RAINMARX

![](banner.jpg)

RAINMARX is a command-line interface (CLI) application designed to manage your Raindrop.io bookmarks efficiently. It provides various functionalities, including retrieving collections, updating bookmarks, and searching for specific bookmarks or collections.

## Features

- Retrieve all bookmarks and nested collections from Raindrop.io
- Get details of a parent collection by its ID
- Update bookmarks with sanitized titles and excerpts
- Search for collections or bookmarks based on user queries
- Save search results to JSON files for easy reference

## Prerequisites

- Python 3.7 or higher
- Raindrop.io API key

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/RAINMARX.git
cd RAINMARX
```

2. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

3. **Configure API headers**:

Update the `config.py` file with your Raindrop.io API key:

```python
headers = {
    'Authorization': 'Bearer YOUR_RAINDROP_API_KEY'
}
```

## Usage

### Running the Application

To start the RAINMARX CLI application, run:

```bash
python RAINMARX.py
```

### Main Menu Options

1. **Get all bookmarks and nested collections**:
   - Retrieves all collections and their bookmarks, saving the structure to `nested_structure.json`.

2. **Get parent collection by ID**:
   - Prompts for a collection ID and retrieves the collection along with its bookmarks, saving the structure to a JSON file.

3. **Update bookmarks from a collection**:
   - Prompts for a JSON file containing nested collections and updates the bookmarks with sanitized titles and excerpts.

4. **Search**:
   - Provides options to search collections or bookmarks based on user queries.

5. **Exit**:
   - Exits the application.

### Detailed Functionality

#### Retrieve All Bookmarks and Nested Collections

This option retrieves all collections and their bookmarks from Raindrop.io and saves them to `nested_structure.json`:

```bash
python nested.py
```

#### Get Parent Collection by ID

This option retrieves a specific collection by its ID and saves the structure to a JSON file in the `collections` directory:

```bash
python collectid.py
```

#### Update Bookmarks

This option updates bookmarks with sanitized titles and excerpts based on a provided JSON file:

```bash
python updatr.py
```

#### Search Collections and Bookmarks

This option allows searching for collections or bookmarks based on user queries. The results are saved to the `searchresults` directory:

```bash
python search.py
```

## Logs

The application logs important events and errors to log files located in the `logs` directory. Each script has its own log file for easier debugging and maintenance.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
