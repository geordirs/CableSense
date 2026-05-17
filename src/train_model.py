import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train_model():
    # Load data
    data_path = 'data/training_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run src/data_generator.py first.")
        return

    df = pd.read_csv(data_path)

    X = df[['gpr', 'acoustic']]
    y = df['status']

    # Train model
    print("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)

    # Save model
    os.makedirs('models', exist_ok=True)
    model_path = 'models/cable_model.joblib'
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
