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
    
    # 1. Add email columns to staff tables
    for table in ["receptionists", "doctors", "lab_staff"]:
        print(f"Checking email column for {table}...")
        cursor.execute(f"SHOW COLUMNS FROM {table} LIKE 'email'")
        result = cursor.fetchone()
        if not result:
            print(f"Adding email column to {table}...")
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN email VARCHAR(100) DEFAULT NULL")
            print(f"Email column added to {table}!")
        else:
            print(f"Email column already exists in {table}.")
            
    # 2. Update default test value
    print("Updating priya.sharma's email for testing forgot password...")
    cursor.execute("UPDATE receptionists SET email = 'shivamjod2004@gmail.com' WHERE username = 'priya.sharma'")
    print("Email seeding completed!")
    
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
