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
    
    # 1. Print current doctor list
    cursor.execute("SELECT * FROM doctors")
    print("Current doctors in DB:")
    for doc in cursor.fetchall():
        print(doc)
        
    # 2. Print current receptionist list
    cursor.execute("SELECT * FROM receptionists")
    print("\nCurrent receptionists in DB:")
    for recep in cursor.fetchall():
        print(recep)
        
    # 3. Clean up receptionists (Keep only 'Ratan' and 'priya.sharma')
    print("\nCleaning up receptionists...")
    cursor.execute("""
        DELETE FROM receptionists 
        WHERE username NOT IN ('Ratan', 'priya.sharma')
    """)
    print("Receptionists cleaned.")
    
    # 4. Clean up doctors (Keep only the 4 main doctors and 'rajesh.khanna' if he exists)
    print("\nCleaning up doctors...")
    cursor.execute("""
        DELETE FROM doctors 
        WHERE username NOT IN ('prajakta.patil', 'darshan.dhage', 'shradha.pandagale', 'vaishali.oak', 'rajesh.khanna')
    """)
    print("Doctors cleaned.")
    
    # 5. Modify columns: Drop contact column from doctors, add email column
    print("\nAltering doctors table structure...")
    try:
        cursor.execute("ALTER TABLE doctors DROP COLUMN contact")
        print("Dropped contact column from doctors.")
    except Exception as e:
        print("Error dropping contact from doctors:", e)
        
    try:
        cursor.execute("ALTER TABLE doctors ADD COLUMN email VARCHAR(255) NULL")
        print("Added email column to doctors.")
    except Exception as e:
        print("Email column might already exist on doctors:", e)
        
    # 6. Modify columns: Drop contact column from receptionists
    print("\nAltering receptionists table structure...")
    try:
        cursor.execute("ALTER TABLE receptionists DROP COLUMN contact")
        print("Dropped contact column from receptionists.")
    except Exception as e:
        print("Error dropping contact from receptionists:", e)
        
    # Verify final lists
    cursor.execute("SELECT * FROM doctors")
    print("\nFinal doctors in DB:")
    for doc in cursor.fetchall():
        print(doc)
        
    cursor.execute("SELECT * FROM receptionists")
    print("\nFinal receptionists in DB:")
    for recep in cursor.fetchall():
        print(recep)
        
    cursor.close()
    conn.close()
    print("\nMigration completed successfully!")
except Exception as e:
    print("Migration failed:", e)
