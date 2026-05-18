import json
import os
import sqlite3
import sys

# Add the project root to the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import DB_PATH

def export_to_geojson(output_file='data/diagnostics.geojson'):
    if not os.path.exists(DB_PATH):
        print(f"Error: Database {DB_PATH} not found.")
        return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT timestamp, latitude, longitude, status, sensor_data FROM history')
    rows = cursor.fetchall()
    conn.close()

    features = []
    for row in rows:
        sensor_data = json.loads(row[4])
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [row[2], row[1]]
            },
            "properties": {
                "timestamp": row[0],
                "status": row[3],
                **sensor_data
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        json.dump(geojson, f, indent=4)
    print(f"Exported {len(features)} points to {output_file} from SQLite.")

if __name__ == "__main__":
    export_to_geojson()
