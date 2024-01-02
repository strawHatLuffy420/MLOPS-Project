# model_evaluation.py
import pandas as pd
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
from main import preprocess_and_split_data

def evaluate_model_performance(model, X_valid, y_valid):
    # Make predictions on the validation set
    predictions = model.predict(X_valid)

    # Evaluate the model
    mse = mean_squared_error(y_valid, predictions)
    mae = mean_absolute_error(y_valid, predictions)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')

if __name__ == "__main__":
    data_file_path = 'dummy_sensor_data.csv'

    # Load the updated dataset
    updated_data = pd.read_csv(data_file_path)

    # Preprocess and split data
    X_train, X_valid, y_train, y_valid = preprocess_and_split_data(updated_data)

    # Load the trained model
    # Assuming that 'train_predictive_maintenance_model' function is available in main.py
    from main import train_predictive_maintenance_model

    trained_model = train_predictive_maintenance_model(X_train, y_train, X_valid, y_valid)

    # Evaluate the model on the validation set
    evaluate_model_performance(trained_model, X_valid, y_valid)
