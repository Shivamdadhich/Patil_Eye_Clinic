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
    print("Checking if payment_status column exists in appointments table...")
    cursor.execute("SHOW COLUMNS FROM appointments LIKE 'payment_status'")
    result = cursor.fetchone()
    
    if not result:
        print("Column payment_status does not exist. Adding column...")
        cursor.execute("ALTER TABLE appointments ADD COLUMN payment_status VARCHAR(20) NOT NULL DEFAULT 'Paid'")
        print("Column payment_status added successfully!")
    else:
        print("Column payment_status already exists.")
        
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
