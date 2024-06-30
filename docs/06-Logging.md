# Logging

Logging is an essential feature for any application as it helps in tracking the application's behavior, diagnosing issues, and understanding the application's flow. In RAINMARX, logging is configured in the `utils.py` file. This section will guide you through the logging setup and how you can customize it to fit your needs.

## Default Logging Configuration

The `utils.py` script sets up the default logging configuration for the RAINMARX application. The key components of this configuration include:

- **Log Filename**: Logs are saved in files named after the script that generates them.
- **Log Directory**: All log files are saved in the `logs` directory.
- **Log Level**: The default log level is set to `DEBUG`, which captures all levels of log messages, from `DEBUG` to `CRITICAL`.
- **Log Format**: The log messages include a timestamp, logger name, log level, and the actual log message.

### Default Logging Setup

Here is the default logging setup in `utils.py`:

```python
import logging
import os

def configure_logging(script_name):
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)  # Create logs directory if it does not exist
    log_filename = os.path.join(log_dir, f'{script_name}.log')

    logging.basicConfig(
        filename=log_filename,
        level=logging.DEBUG,  # Set the log level to DEBUG
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Log format
        datefmt='%Y-%m-%d %H:%M:%S'  # Date format
    )

    # Also log to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
```

### Explanation of Parameters

- **log_dir**: This variable specifies the directory where log files will be stored. The `os.makedirs(log_dir, exist_ok=True)` function ensures that this directory is created if it does not already exist.
- **log_filename**: This variable constructs the log file path using the script name, allowing each script to have its own log file.
- **logging.basicConfig()**: This function sets up the basic configuration for logging. Key parameters include:

  - `filename=log_filename`: Specifies the log file path.
  - `level=logging.DEBUG`: Sets the logging level to DEBUG, capturing all messages from DEBUG to CRITICAL.
  - `format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'`: Defines the log message format, including the timestamp, logger name, log level, and message.
  - `datefmt='%Y-%m-%d %H:%M:%S'`: Defines the date format for timestamps in the log messages.

- **console logging**: Additionally, the configuration sets up logging to the console using `logging.StreamHandler()`. This ensures that log messages are also output to the terminal, which is useful for real-time monitoring.

## Customizing Logging Settings

You can customize the logging settings in `utils.py` to suit your needs. Here are some common customizations:

### Changing the Log Level

The log level determines the severity of messages that are captured. You can change the log level from `DEBUG` to other levels such as `INFO`, `WARNING`, `ERROR`, or `CRITICAL`.

```python
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,  # Change log level to INFO
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

### Modifying the Log Format

You can change the log format to include additional information or to format the message differently.

```python
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s [in %(pathname)s:%(lineno)d]',  # Include file path and line number
    datefmt='%Y-%m-%d %H:%M:%S'
)
```

### Rotating Log Files

If you expect your log files to become large, you can use the `RotatingFileHandler` to create new log files after they reach a certain size, keeping a specified number of old log files.

```python
from logging.handlers import RotatingFileHandler

log_handler = RotatingFileHandler(log_filename, maxBytes=5*1024*1024, backupCount=5)  # 5 MB per file, keep 5 backups
log_handler.setLevel(logging.DEBUG)
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(log_handler)
```

### Logging to Multiple Destinations

You can configure logging to multiple destinations, such as different files for different log levels or sending critical errors to a separate file.

```python
error_log_handler = logging.FileHandler('logs/error.log')
error_log_handler.setLevel(logging.ERROR)
error_log_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logging.getLogger('').addHandler(error_log_handler)
```

## Using Logging in Scripts

In each script, you should import the logging module and call the `configure_logging()` function at the start of the script. This ensures that logging is set up correctly.

### Example Usage in a Script

```python
import logging
from utils import configure_logging

configure_logging('example_script')

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
```

## Accessing Log Files

Log files are saved in the `logs` directory. You can access and review these files to monitor the application's behavior, debug issues, and gain insights into its operation.

- **Log File Structure**: Each script will have its own log file named after the script (e.g., `example_script.log`).
- **Log Rotation**: If you are using rotating logs, older logs will be saved with a numeric suffix (e.g., `example_script.log.1`).


---

[<- Previous](05-Detailed_Script_Descriptions.md) | [Next ->](07-Troubleshooting.md)
