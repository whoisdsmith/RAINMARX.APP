import json
import logging
import re
import unicodedata
import os


def configure_logging(script_name):
    log_filename = f'logs/{script_name}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )


def read_json(file_name):
    logging.info(f"Reading JSON file: {file_name}")
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
        logging.info(f"Successfully read JSON file: {file_name}")
        return data
    except Exception as e:
        logging.error(f"Error reading JSON file {file_name}: {e}")
        raise


def sanitize_text(text):
    logging.debug(f"Sanitizing text: {text}")
    try:
        text = unicodedata.normalize('NFKD', text).encode(
            'ascii', 'ignore').decode('ascii')
        text = re.sub(r'[^\w\s]', '', text)
        logging.debug(f"Sanitized text: {text}")
        return text
    except Exception as e:
        logging.error(f"Error sanitizing text: {e}")
        return text
