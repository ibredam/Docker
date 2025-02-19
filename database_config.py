# database_config.py
import os

def load_db_credentials():
    try:
        with open('/run/secrets/db_credentials.txt', 'r') as f:
            lines = f.readlines()
            return {
                'host': lines[0].strip(),
                'user': lines[1].strip(),
                'password': lines[2].strip(),
                'database': lines[3].strip()
            }
    except FileNotFoundError:
        return {
                'host': os.environ.get("MYSQL_HOST"),
                'user': os.environ.get("MYSQL_USER"),
                'password': os.environ.get("MYSQL_PASSWORD"),
                'database': os.environ.get("MYSQL_DATABASE")
            }

db_config = load_db_credentials()