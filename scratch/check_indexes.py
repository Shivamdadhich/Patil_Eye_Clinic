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
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    print("Checking indexes on appointments...")
    cursor.execute("SHOW INDEX FROM appointments")
    for row in cursor.fetchall():
        print(row['Table'], row['Column_name'], row['Key_name'])
        
    print("\nChecking indexes on prescription_scan_session_files...")
    cursor.execute("SHOW INDEX FROM prescription_scan_session_files")
    for row in cursor.fetchall():
        print(row['Table'], row['Column_name'], row['Key_name'])

    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
