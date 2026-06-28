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
    print("Checking if time_slot column exists in appointments table...")
    cursor.execute("SHOW COLUMNS FROM appointments LIKE 'time_slot'")
    result = cursor.fetchone()
    
    if not result:
        print("Column time_slot does not exist. Adding column...")
        cursor.execute("ALTER TABLE appointments ADD COLUMN time_slot VARCHAR(100) DEFAULT NULL")
        print("Column time_slot added successfully!")
    else:
        print("Column time_slot already exists.")
        
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
