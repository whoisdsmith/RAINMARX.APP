# Troubleshooting

This section provides guidance on resolving common issues you might encounter while using the RAINMARX CLI application. It also explains how to use log files to diagnose problems.

## Common Issues

### 1\. Invalid API Token

#### Symptoms

- API requests fail with authentication errors.
- Error messages indicating invalid or missing API token.

#### Resolution

1. **Verify API Token Entry**:

  - Open the `config.py` file in a text editor.
  - Ensure that the `api_token` variable is correctly set with your API token.

    ```python
    api_token = 'your_actual_api_token_here'
    headers = {
      'Authorization': f'Bearer {api_token}',
      'Content-Type': 'application/json'
    }
    ```

2. **Check API Token Permissions**:

  - Ensure your API token has the necessary permissions to access and manage your Raindrop.io bookmarks. You can verify and adjust permissions in the Raindrop.io developer portal.

3. **Using Environment Variables**:

  - If you are using environment variables, make sure they are set correctly.
  - Verify the environment variable is loaded in your shell:

    ```bash
    echo $RAINDROP_API_TOKEN
    ```

  - The output should display your API token. If it is empty, set the variable again:

    ```bash
    export RAINDROP_API_TOKEN="your_actual_api_token_here"
    ```

### 2\. Rate Limiting

#### Symptoms

- API requests fail with rate limit errors.
- Slow response times due to frequent API calls.

#### Resolution

1. **Understand Rate Limits**:

  - Raindrop.io API has rate limits to prevent abuse. Exceeding these limits will result in errors.

2. **Adjust Request Delay**:

  - Open the `nested.py` file in a text editor.
  - Locate the `REQUEST_DELAY` variable. Increase its value to reduce the frequency of API requests.

    ```python
    RATE_LIMIT = 120  # Maximum number of requests per minute
    REQUEST_DELAY = 60 / RATE_LIMIT  # Delay between requests in seconds
    ```

  - For example, if you are hitting rate limits, you might reduce the rate limit to 60 requests per minute, thus increasing the delay:

    ```python
    RATE_LIMIT = 60
    REQUEST_DELAY = 60 / RATE_LIMIT  # 1 second delay between requests
    ```

3. **Implement Exponential Backoff**:

  - Consider implementing an exponential backoff strategy to handle rate limits gracefully. This involves increasing the delay between requests exponentially after each rate limit error.

### 3\. Connection Errors

#### Symptoms

- API requests fail with connection errors.
- Error messages indicating network issues or inability to reach the Raindrop.io API.

#### Resolution

1. **Check Internet Connection**:

  - Ensure your device is connected to the internet.
  - Test your connection by visiting a website or using a network tool like `ping`.

2. **Verify Raindrop.io API Accessibility**:

  - Ensure that the Raindrop.io API is accessible by visiting their status page or contacting their support if you suspect an outage.

3. **Proxy and Firewall Settings**:

  - If you are behind a proxy or firewall, ensure that your settings allow outgoing connections to the Raindrop.io API endpoints.

4. **Retry Mechanism**:

  - Implement a retry mechanism in your scripts to handle transient network issues. This involves retrying the request after a short delay if a connection error occurs.

## Logs

Logs are invaluable for diagnosing issues and understanding the behavior of the application. RAINMARX saves logs in the `logs` directory, with each script having its own log file.

### Accessing Log Files

1. **Locate Log Files**:

  - Navigate to the `logs` directory in the RAINMARX project folder.
  - Each script has a corresponding log file named after the script (e.g., `nested.log`, `search.log`).

2. **Read Log Files**:

  - Open the log file in a text editor to read its contents.
  - Look for error messages, warnings, and other log entries that provide clues about what went wrong.

### Example Log Entry

Here is an example of what a log entry might look like:

```log
2024-01-01 12:00:00 - nested - INFO - Fetching root collections
2024-01-01 12:00:05 - nested - ERROR - Failed to fetch collections: Invalid API token
```

### Using Logs for Troubleshooting

1. **Identify Errors**:

  - Look for `ERROR` entries in the log files. These entries often indicate what went wrong and provide details about the error.

2. **Trace Log Entries**:

  - Follow the sequence of log entries leading up to an error to understand the context in which the error occurred.

3. **Check Debug Information**:

  - If the log level is set to `DEBUG`, the logs will contain detailed information about the application's operations. This can help pinpoint where the issue started.

### Adjusting Log Levels

If the logs are not providing enough information, you can increase the log level to `DEBUG` for more detailed output. Conversely, if the logs are too verbose, you can reduce the log level to `INFO` or `WARNING`.

```python
import logging

logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,  # Change to INFO or WARNING if needed
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```


---

[<- Previous](06-Logging.md)
