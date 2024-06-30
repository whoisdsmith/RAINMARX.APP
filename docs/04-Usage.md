# Usage

This section provides detailed instructions on how to use the RAINMARX CLI application. After successfully installing and configuring the application, you can start using it to manage your Raindrop.io bookmarks.

## Starting the CLI Application

To start the RAINMARX CLI application, navigate to the directory where you cloned the repository and run the main script:

```bash
python RAINMARX.py
```

This command initializes the application and presents you with a menu of options. The menu allows you to choose from various operations to interact with your Raindrop.io bookmarks and collections.

## Menu Options

Once the application is running, you will see a menu with the following options:

1. **Get all bookmarks and nested collections**
2. **Get parent collection by ID**
3. **Update bookmarks from a collection**
4. **Search**
5. **Get user stats**
6. **Get user collection groups**
7. **Exit**

Choose the desired option by entering the corresponding number and pressing Enter.

### 1\. Get All Bookmarks and Nested Collections

This option retrieves all your bookmarks and collections, including nested collections, from Raindrop.io. The fetched data is saved to a JSON file for easy access and manipulation.

- **Steps**:

  1. Select option `1` and press Enter.
  2. The application fetches all bookmarks and collections.
  3. The data is saved in the `collections/nested.json` file.
  4. A message indicating the location of the saved file is displayed.

- **Use Case**: Use this option to get a comprehensive view of all your bookmarks and their organization in collections.

### 2\. Get Parent Collection by ID

This option allows you to retrieve a specific parent collection using its unique ID.

- **Steps**:

  1. Select option `2` and press Enter.
  2. Enter the collection ID when prompted.
  3. The application fetches the specified parent collection.
  4. The details of the collection are displayed.

- **Use Case**: Use this option when you need information about a particular collection.

### 3\. Update Bookmarks from a Collection

This option allows you to update bookmarks within a specified collection. You can modify attributes such as titles, URLs, and tags.

- **Steps**:

  1. Select option `3` and press Enter.
  2. Enter the collection ID of the collection you want to update.
  3. Follow the prompts to update bookmark attributes.
  4. The application updates the bookmarks in the specified collection.

- **Use Case**: Use this option to batch update bookmarks within a collection, making it easier to manage large sets of bookmarks.

### 4\. Search

This option enables you to search for bookmarks based on keywords. It helps you quickly find specific bookmarks among your collections.

- **Steps**:

  1. Select option `4` and press Enter.
  2. Enter the search keywords when prompted.
  3. The application searches for bookmarks matching the keywords.
  4. The search results are displayed.

- **Use Case**: Use this option to locate bookmarks based on titles, tags, or other attributes.

### 5\. Get User Stats

This option provides statistics about your Raindrop.io account, such as the number of bookmarks, collections, and other relevant metrics.

- **Steps**:

  1. Select option `5` and press Enter.
  2. The application fetches and displays user statistics.

- **Use Case**: Use this option to get insights into your bookmark usage and overall account statistics.

### 6\. Get User Collection Groups

This option retrieves the collection groups you have created in Raindrop.io, helping you manage and organize your collections more effectively.

- **Steps**:

  1. Select option `6` and press Enter.
  2. The application fetches and displays your collection groups.

- **Use Case**: Use this option to view and manage groups of collections.

### 7\. Exit

This option exits the RAINMARX CLI application.

- **Steps**:

  1. Select option `7` and press Enter.
  2. The application terminates, and you are returned to the command prompt.

- **Use Case**: Use this option to exit the application when you are done.

## Example Workflow

Here is an example workflow to demonstrate how you might use RAINMARX:

1. **Start the application**:

  ```bash
  python RAINMARX.py
  ```

2. **Fetch all bookmarks and nested collections**:

  - Select option `1` to get a comprehensive view of your bookmarks.
  - Review the saved JSON file to understand your bookmark structure.

3. **Search for specific bookmarks**:

  - Select option `4` to search for bookmarks using keywords.
  - Enter the search term (e.g., "Python") to find relevant bookmarks.

4. **Update bookmarks in a collection**:

  - Select option `3` to update bookmarks.
  - Enter the collection ID and follow the prompts to modify bookmark attributes.

5. **Get user stats**:

  - Select option `5` to view statistics about your bookmark usage.

6. **Exit the application**:

  - Select option `7` to terminate the application.


---

[<- Previous](03-Configuration.md) | [Next ->](05-Detailed_Script_Descriptions.md)
