import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

def train_enhanced_model():
    # Load data
    data_path = 'data/training_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found. Run src/data_generator.py first.")
        return

    df = pd.read_csv(data_path)

    # Feature columns in specific order
    features = ['gpr_amplitude', 'pd_intensity', 'soil_resistivity', 'burial_depth']
    X = df[features]
    y = df['status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    print("Training Enhanced Random Forest model for multi-class classification...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    os.makedirs('models', exist_ok=True)
    model_path = 'models/cable_model.joblib'
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_enhanced_model()
