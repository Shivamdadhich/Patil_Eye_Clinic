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
    
    print("Deleting old Ophthalmology doctors from DB...")
    cursor.execute("DELETE FROM doctors WHERE specialization = 'Ophthalmology'")
    
    new_doctors = [
        ("prajakta.patil", "pass123", "Dr. Prajakta Patil", "Ophthalmology", "9970269844", "prajakta@gmail.com"),
        ("darshan.dhage", "pass123", "Dr. Darshan Dhage", "Ophthalmology", "9999999999", "darshan@gmail.com"),
        ("shradha.pandagale", "pass123", "Dr. Shradha Pandagale", "Ophthalmology", "9999999999", "shradha@gmail.com"),
        ("vaishali.oak", "pass123", "Dr. Vaishali Oak", "Ophthalmology", "9999999999", "vaishali@gmail.com")
    ]
    
    print("Inserting new clinic doctors...")
    for username, pwd, name, spec, contact, email in new_doctors:
        cursor.execute("""
            INSERT INTO doctors (username, password, name, specialization, contact, email) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (username, pwd, name, spec, contact, email))
        print(f"Inserted: {name}")
        
    cursor.close()
    conn.close()
    print("Migration finished successfully!")
except Exception as e:
    print("Error:", e)
