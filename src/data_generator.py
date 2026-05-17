import pandas as pd
import numpy as np
import os

def generate_data(num_samples=1000):
    np.random.seed(42)

    gpr = np.random.uniform(0, 1, num_samples)
    acoustic = np.random.uniform(0, 1, num_samples)

    data = pd.DataFrame({
        'gpr': gpr,
        'acoustic': acoustic
    })

    def label_status(row):
        if row['gpr'] > 0.8 or row['acoustic'] > 0.8:
            return 'Fault Detected'
        elif row['gpr'] > 0.5 or row['acoustic'] > 0.5:
            return 'Degraded'
        else:
            return 'Healthy'

    data['status'] = data.apply(label_status, axis=1)

    os.makedirs('data', exist_ok=True)
    filepath = 'data/training_data.csv'
    data.to_csv(filepath, index=False)
    print(f"Generated {num_samples} samples and saved to {filepath}")

if __name__ == "__main__":
    generate_data()
