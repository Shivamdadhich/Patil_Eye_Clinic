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
    
    updates = {
        'prajakta.patil': 'Prajakta.patil',
        'darshan.dhage': 'Darshan.dhage',
        'shradha.pandagale': 'Shradha.pandagale',
        'vaishali.oak': 'Vaishali.oak',
        'rajesh.khanna': 'Rajesh.khanna'
    }
    
    print("Updating doctor usernames...")
    for old_user, new_user in updates.items():
        cursor.execute("UPDATE doctors SET username = %s WHERE username = %s", (new_user, old_user))
        print(f"Updated: {old_user} -> {new_user}")
        
    cursor.execute("SELECT name, username FROM doctors")
    print("\nVerified current usernames in database:")
    for row in cursor.fetchall():
        print(row)
        
    cursor.close()
    conn.close()
    print("\nSuccess!")
except Exception as e:
    print("Error:", e)
