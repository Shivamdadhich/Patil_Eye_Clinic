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
    
    # 1. Add contact columns if they don't exist
    for table in ["receptionists", "doctors", "lab_staff"]:
        print(f"Checking columns for {table}...")
        cursor.execute(f"SHOW COLUMNS FROM {table} LIKE 'contact'")
        result = cursor.fetchone()
        if not result:
            print(f"Adding contact column to {table}...")
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN contact VARCHAR(20) DEFAULT NULL")
            print(f"Contact column added to {table}!")
        else:
            print(f"Contact column already exists in {table}.")

    # 2. Update default test values
    print("Updating default staff contact numbers to '9999999999' for testing forgot password...")
    cursor.execute("UPDATE receptionists SET contact = '9999999999' WHERE contact IS NULL")
    cursor.execute("UPDATE doctors SET contact = '9999999999' WHERE contact IS NULL")
    cursor.execute("UPDATE lab_staff SET contact = '9999999999' WHERE contact IS NULL")
    print("Seeding completed successfully!")

    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
