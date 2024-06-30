
# Troubleshooting

## Common Issues

1. **Invalid API Token**:
   - Ensure your API token is correctly entered in `config.py`.
   - Check that your API token has the necessary permissions.

2. **Rate Limiting**:
   - The Raindrop.io API has a rate limit. If you encounter rate limiting errors, try increasing the `REQUEST_DELAY` in `nested.py`.

3. **Connection Errors**:
   - Check your internet connection.
   - Ensure the Raindrop.io API is accessible.

## Logs

Check the log files in the `logs` directory for detailed error messages and troubleshooting information.
