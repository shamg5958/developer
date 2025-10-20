import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "sa_user",
    "password": "SaUser@123",
    "database": "sa_app_db"
}

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
)
""")
cursor.execute("INSERT IGNORE INTO users (username, password) VALUES ('saurabh', 'Root@12345')")
conn.commit()
cursor.close()
conn.close()
print("✅ Database initialized")

