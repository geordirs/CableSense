import pandas as pd
import numpy as np
import os

def generate_enhanced_data(num_samples=2000):
    np.random.seed(42)

    # Realistic feature generation
    # GPR Reflection Amplitude (0-1): Higher indicates metal or moisture
    gpr_amplitude = np.random.uniform(0, 1, num_samples)
    # Partial Discharge Intensity (0-1): Higher indicates insulation failure
    pd_intensity = np.random.uniform(0, 1, num_samples)
    # Soil Resistivity (Ohm-m): 10 to 1000, affects signal attenuation
    soil_resistivity = np.random.uniform(10, 1000, num_samples)
    # Burial Depth (m): 0.5 to 3.0 meters
    burial_depth = np.random.uniform(0.5, 3.0, num_samples)

    data = pd.DataFrame({
        'gpr_amplitude': gpr_amplitude,
        'pd_intensity': pd_intensity,
        'soil_resistivity': soil_resistivity,
        'burial_depth': burial_depth
    })

    def classify_fault(row):
        # Logic based on research findings
        if row['pd_intensity'] > 0.75:
            return 'Insulation Failure'
        elif row['gpr_amplitude'] > 0.8 and row['soil_resistivity'] < 100:
            return 'Moisture Intrusion'
        elif row['gpr_amplitude'] > 0.9 and row['pd_intensity'] < 0.2:
            return 'Physical Break'
        elif row['pd_intensity'] > 0.4 or row['gpr_amplitude'] > 0.5:
            return 'Degraded'
        else:
            return 'Healthy'

    data['status'] = data.apply(classify_fault, axis=1)

    os.makedirs('data', exist_ok=True)
    filepath = 'data/training_data.csv'
    data.to_csv(filepath, index=False)
    print(f"Generated {num_samples} enhanced samples and saved to {filepath}")
    print("Class distribution:")
    print(data['status'].value_counts())

if __name__ == "__main__":
    generate_enhanced_data()
