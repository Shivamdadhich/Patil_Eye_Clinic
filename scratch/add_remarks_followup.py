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
    
    print("Altering patient_history table to add remarks and follow_up_date...")
    try:
        cursor.execute("ALTER TABLE patient_history ADD COLUMN remarks TEXT NULL")
        print("Added remarks column.")
    except Exception as e:
        print("Remarks column might already exist:", e)
        
    try:
        cursor.execute("ALTER TABLE patient_history ADD COLUMN follow_up_date DATE NULL")
        print("Added follow_up_date column.")
    except Exception as e:
        print("Follow_up_date column might already exist:", e)
        
    cursor.close()
    conn.close()
    print("Database migration successful!")
except Exception as e:
    print("Migration error:", e)
