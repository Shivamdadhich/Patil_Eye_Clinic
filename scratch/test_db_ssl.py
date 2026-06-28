import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST", "localhost")
user = os.getenv("DB_USER", "root")
password = os.getenv("DB_PASS", "")
database = os.getenv("DB_NAME", "careconnect")
port = int(os.getenv("DB_PORT", 3306))

print("Testing connection with ssl=True...")
try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        ssl=True,
        autocommit=True
    )
    print("Success with ssl=True!")
    conn.close()
except Exception as e:
    print("Failed with ssl=True:", e)

print("\nTesting connection with ssl={'min_version': 'TLSv1.2'}...")
try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        ssl={"min_version": "TLSv1.2"},
        autocommit=True
    )
    print("Success with ssl={'min_version': 'TLSv1.2'}!")
    conn.close()
except Exception as e:
    print("Failed with ssl={'min_version': 'TLSv1.2'}:", e)

print("\nTesting connection with ssl={}...")
try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        ssl={},
        autocommit=True
    )
    print("Success with ssl={}!")
    conn.close()
except Exception as e:
    print("Failed with ssl={}:", e)
