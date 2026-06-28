import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST", "localhost")
user = os.getenv("DB_USER", "root")
password = os.getenv("DB_PASS", "")
database = os.getenv("DB_NAME", "careconnect")
port = int(os.getenv("DB_PORT", 3306))

try:
    conn = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        ssl={"min_version": "TLSv1.2"} if host not in ("localhost", "127.0.0.1") else None,
        autocommit=True
    )
    cursor = conn.cursor()
    print("Updating contact number for priya.sharma...")
    cursor.execute("UPDATE receptionists SET contact = '8949163739' WHERE username = 'priya.sharma'")
    print(f"Updated {cursor.rowcount} row successfully!")
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
