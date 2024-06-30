# Logging

Logging is configured in `utils.py`. You can customize the logging level and format as needed. Logs are saved in the `logs` directory.

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
