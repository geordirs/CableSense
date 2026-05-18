import sqlite3
import os
import json

DB_PATH = 'data/diagnostics.db'

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            latitude REAL,
            longitude REAL,
            status TEXT,
            sensor_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_entry(timestamp, lat, lon, status, sensor_data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO history (timestamp, latitude, longitude, status, sensor_data)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, lat, lon, status, json.dumps(sensor_data)))
    conn.commit()
    conn.close()

def get_history(limit=100):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM history ORDER BY id DESC LIMIT ?', (limit,))
    rows = cursor.fetchall()
    conn.close()

    history = []
    for row in rows:
        history.append({
            'id': row[0],
            'timestamp': row[1],
            'location': {'latitude': row[2], 'longitude': row[3]},
            'status': row[4],
            'sensor_data': json.loads(row[5])
        })
    return history

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
