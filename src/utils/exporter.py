import json
import os

def export_to_geojson(history_file='data/history.json', output_file='data/diagnostics.geojson'):
    if not os.path.exists(history_file):
        print(f"Error: {history_file} not found.")
        return

    with open(history_file, 'r') as f:
        history = json.load(f)

    features = []
    for entry in history:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [entry['location']['longitude'], entry['location']['latitude']]
            },
            "properties": {
                "timestamp": entry['timestamp'],
                "status": entry['status'],
                **entry['sensor_data']
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    with open(output_file, 'w') as f:
        json.dump(geojson, f, indent=4)
    print(f"Exported {len(features)} points to {output_file}")

if __name__ == "__main__":
    export_to_geojson()
