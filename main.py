"""main.py.

Project launcher.
"""

import uvicorn

app_config = {
    'app': 'app:app',
    'host': '0.0.0.0',
    'port': 8000,
    'log_level': 'info',
    'env_file': '.env'
}

if __name__ == '__main__':
    uvicorn.run(**app_config)
