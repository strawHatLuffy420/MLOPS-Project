# concept_drift_detection.py
import pandas as pd
from main import preprocess_and_split_data, train_predictive_maintenance_model, evaluate_model_performance
from sklearn.metrics import mean_squared_error
from datetime import datetime, timedelta

def detect_concept_drift(data_file_path, window_size=7):
    # Load the entire dataset
    data = pd.read_csv(data_file_path)

    # Initialize variables for tracking performance over time
    window_start_date = datetime.strptime(data['Timestamp'].min(), '%Y-%m-%d %H:%M:%S')
    window_end_date = window_start_date + timedelta(days=window_size)
    mse_history = []

    while window_end_date <= datetime.strptime(data['Timestamp'].max(), '%Y-%m-%d %H:%M:%S'):
        # Extract data within the current window
        window_data = data[(data['Timestamp'] >= window_start_date) & (data['Timestamp'] < window_end_date)]

        # Preprocess and split data
        X_train, X_valid, y_train, y_valid = preprocess_and_split_data(window_data)

        # Train the model
        model = train_predictive_maintenance_model(X_train, y_train, X_valid, y_valid)

        # Evaluate the model on the validation set
        mse = evaluate_model_on_window(model, X_valid, y_valid)

        # Append MSE to history
        mse_history.append(mse)

        # Move the window to the next period
        window_start_date = window_end_date
        window_end_date += timedelta(days=window_size)

    # Detect concept drift based on MSE history
    detect_drift(mse_history)

def evaluate_model_on_window(model, X_valid, y_valid):
    # Make predictions on the validation set
    predictions = model.predict(X_valid)

    # Calculate mean squared error
    mse = mean_squared_error(y_valid, predictions)

    return mse

def detect_drift(mse_history, threshold=1.5):
    # Compare the current MSE with the historical average
    current_mse = mse_history[-1]
    historical_average = sum(mse_history[:-1]) / max(len(mse_history) - 1, 1)

    # Detect drift if the current MSE is significantly higher than the historical average
    if current_mse > threshold * historical_average:
        print(f"Concept drift detected at {datetime.now()}. Current MSE: {current_mse}, Historical Average MSE: {historical_average}")
    else:
        print(f"No concept drift detected at {datetime.now()}. Current MSE: {current_mse}, Historical Average MSE: {historical_average}")

if __name__ == "__main__":
    data_file_path = 'dummy_sensor_data.csv'
    window_size = 7  # Adjust the window size based on your requirements

    # Detect concept drift
    detect_concept_drift(data_file_path, window_size)
