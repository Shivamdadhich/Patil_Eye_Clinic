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
    
    print("Creating pharmacy_bills table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pharmacy_bills (
            id INT AUTO_INCREMENT PRIMARY KEY,
            aadhaar VARCHAR(12) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            payment_method VARCHAR(50) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (aadhaar) REFERENCES patients(aadhaar) ON DELETE CASCADE
        )
    """)
    print("Table pharmacy_bills created successfully!")
    
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
