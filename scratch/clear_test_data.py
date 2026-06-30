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
    
    print("Fetching list of all tables...")
    cursor.execute("SHOW TABLES")
    tables = [t[0] for t in cursor.fetchall()]
    print("Tables in database:", tables)
    
    # Tables to clear
    tables_to_clear = [
        "appointments",
        "patients",
        "patient_history",
        "lab_reports",
        "prescription_scan_sessions",
        "prescription_scan_session_files"
    ]
    
    # Disable foreign key checks for clean truncation
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    
    for table in tables_to_clear:
        if table in tables:
            print(f"Clearing table: {table}...")
            cursor.execute(f"TRUNCATE TABLE {table}")
            print(f"Table {table} cleared.")
            
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    cursor.close()
    conn.close()
    print("All testing and dummy data cleared successfully!")
except Exception as e:
    print("Error clearing data:", e)
