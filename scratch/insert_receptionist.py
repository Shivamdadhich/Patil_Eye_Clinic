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
    
    # Check if Ratan already exists
    cursor.execute("SELECT * FROM receptionists WHERE username = 'Ratan'")
    exists = cursor.fetchone()
    
    if exists:
        print("Receptionist 'Ratan' already exists. Updating details...")
        cursor.execute("""
            UPDATE receptionists 
            SET password = %s, email = %s, name = %s 
            WHERE username = 'Ratan'
        """, ("pass123", "ratankumarram2006@gmail.com", "Ratan Kumar"))
        print("Updated receptionist details successfully!")
    else:
        print("Inserting new receptionist 'Ratan'...")
        cursor.execute("""
            INSERT INTO receptionists (username, password, name, email) 
            VALUES (%s, %s, %s, %s)
        """, ("Ratan", "pass123", "Ratan Kumar", "ratankumarram2006@gmail.com"))
        print("Inserted new receptionist successfully!")
        
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
