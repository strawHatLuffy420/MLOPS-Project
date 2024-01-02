# data_collection.py
import os
import requests
import pandas as pd
from datetime import datetime

DATA_DIR = 'data/'
API_ENDPOINT = 'https://api.example.com/data'

def fetch_data():
    # Replace this with your data fetching logic
    response = requests.get(API_ENDPOINT)
    data = response.json()
    return data

def save_data(data):
    # Create a timestamped directory to store each batch of data
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    batch_dir = os.path.join(DATA_DIR, f'data_{timestamp}')

    if not os.path.exists(batch_dir):
        os.makedirs(batch_dir)

    # Save the data to a CSV file
    data_file = os.path.join(batch_dir, 'data.csv')
    pd.DataFrame(data).to_csv(data_file, index=False)

def collect_data():
    data = fetch_data()
    save_data(data)

if __name__ == "__main__":
    collect_data()
