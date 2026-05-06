import os
import sqlite3

print("🔥 RUNNING INIT DB FILE")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "fitness.db")

print("DB PATH:", db_path)

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS health_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    gender TEXT,
    height REAL,
    weight REAL,
    bmi REAL,
    category TEXT,
    calories REAL
)
""")

conn.commit()
conn.close()

print("✅ DATABASE CREATED")