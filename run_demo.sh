#!/bin/bash

echo "--- Initializing AI Cable Diagnostic Device Demo ---"

# 1. Generate Synthetic Data
echo "Step 1: Generating training data..."
python3 src/data_generator.py

# 2. Train the AI Model
echo "Step 2: Training the model..."
python3 src/train_model.py

# 3. Start the API and Dashboard
echo "Step 3: Starting the Web API and Dashboard..."
echo "Open your browser at http://localhost:5000"
python3 src/api.py
