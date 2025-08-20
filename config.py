import os

DATABASE_CONFIG = {
    'host': os.getenv('DB_HOST', '127.0.0.1'), 
    'user': os.getenv('DB_USER', 'appuser'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME', 'user')
}
