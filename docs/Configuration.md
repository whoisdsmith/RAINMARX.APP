
# Configuration

## API Token

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

## Logging Configuration

Configure logging settings in `utils.py` according to your preferences. The default configuration logs to a file in the `logs` directory.
