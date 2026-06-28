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
    print("Listing recent appointments:")
    cursor.execute("SELECT * FROM appointments ORDER BY appointment_id DESC LIMIT 10")
    for appt in cursor.fetchall():
        print(f"ID: {appt['appointment_id']}, Aadhaar: {appt['aadhaar']}, Doctor: {appt['doctor']}, Date: {appt['appointment_date']}, Slot: {appt['time_slot']}, Status: {appt['payment_status']}")
    cursor.close()
    conn.close()
except Exception as e:
    print("Error:", e)
