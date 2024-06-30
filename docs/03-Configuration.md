# Configuration

Proper configuration of RAINMARX is crucial for ensuring it interacts correctly with your Raindrop.io account and logs information as expected. This section covers how to set up your Raindrop.io API token and configure logging settings.

## API Token

To interact with the Raindrop.io API, you need an API token. This token authenticates your requests and allows RAINMARX to access your bookmarks and collections.

### Steps to Obtain Your API Token

1. **Sign in to Raindrop.io**:

  - Open your web browser and go to [Raindrop.io](https://raindrop.io/).
  - Sign in with your account credentials.

2. **Access the Developer Portal**:

  - Navigate to the [Raindrop.io Developer Portal](https://app.raindrop.io/settings/integrations).
  - If you haven't created an application before, click on the "Create new application" button.

3. **Create a New Application**:

  - Provide a name for your application (e.g., "RAINMARX CLI Tool").
  - Fill out any other required fields and click "Create".

4. **Retrieve Your API Token**:

  - After creating the application, you will see an "API token" section.
  - Copy the API token provided. This token is a long string of characters that you will use to authenticate API requests.

### Updating `config.py` with Your API Token

Once you have obtained your API token, you need to update the `config.py` file in the RAINMARX directory with this token. Open `config.py` in a text editor and replace `'your_api_token_here'` with your actual API token:

```python
# config.py

api_token = 'your_actual_api_token_here'
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}
```

### Using Environment Variables for Your API Token

For better security practices, especially if you plan to share your code or store it in a version control system, consider using environment variables to store your API token. This prevents the token from being hardcoded in your script.

1. **Set the Environment Variable**:

  - On **Windows**, open Command Prompt and run:

    ```cmd
    setx RAINDROP_API_TOKEN "your_actual_api_token_here"
    ```

  - On **macOS/Linux**, open Terminal and run:

    ```bash
    export RAINDROP_API_TOKEN="your_actual_api_token_here"
    ```

2. **Update `config.py` to Use the Environment Variable**: Modify `config.py` to read the API token from the environment variable:

  ```python
  # config.py

  import os

  api_token = os.getenv('RAINDROP_API_TOKEN')
  if not api_token:
      raise ValueError("API token not set. Please set the RAINDROP_API_TOKEN environment variable.")

  headers = {
      'Authorization': f'Bearer {api_token}',
      'Content-Type': 'application/json'
  }
  ```

## Logging Configuration

RAINMARX uses logging to keep track of its operations and any issues that arise. Proper logging configuration is essential for debugging and monitoring the application.

### Default Logging Configuration

The default logging configuration is set up in `utils.py`. This configuration logs messages to a file in the `logs` directory with the following settings:

- **Log Level**: DEBUG (captures all levels of log messages)
- **Log Format**: Includes the timestamp, logger name, log level, and message
- **Log File**: Each script has its own log file named after the script

Here is the default logging configuration in `utils.py`:

```python
# utils.py

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

### Customizing Logging Settings

You can customize the logging settings according to your needs. Here are a few common customizations:

1. **Change Log Level**: To capture fewer details, you can set the log level to INFO, WARNING, ERROR, or CRITICAL.

  ```python
  logging.basicConfig(
       filename=log_filename,
       level=logging.INFO,  # Change this to the desired log level
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       datefmt='%Y-%m-%d %H:%M:%S'
   )
  ```

2. **Change Log Format**: Modify the format string to include different details.

  ```python
  logging.basicConfig(
       filename=log_filename,
       level=logging.DEBUG,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]',
       datefmt='%Y-%m-%d %H:%M:%S'
   )
  ```

3. **Rotate Log Files**: Use the `RotatingFileHandler` to create new log files after they reach a certain size, keeping a specified number of old log files.

  ```python
  from logging.handlers import RotatingFileHandler

   log_handler = RotatingFileHandler(log_filename, maxBytes=5*1024*1024, backupCount=5)
   log_handler.setLevel(logging.DEBUG)
   log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
   logging.getLogger('').addHandler(log_handler)
  ```

By customizing these settings, you can tailor the logging behavior to better fit your specific requirements and preferences.
