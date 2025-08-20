import os

DATABASE_CONFIG = {
    'host': os.getenv('MYSQL_HOST', '127.0.0.1'), 
    'user': os.getenv('MYSQL_USER', 'appuser'),
    'password': os.getenv('MYSQL_PASSWORD', ''),
    'database': os.getenv('MYSQL_DATABASE', 'user')
}
