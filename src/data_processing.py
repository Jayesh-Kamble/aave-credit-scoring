import json
import pandas as pd
import numpy as np
from datetime import datetime

def load_and_clean_data(file_path):
    """Load and clean transaction data from JSON file"""
    
    print(f"Loading data from {file_path}...")
    
    # Load JSON data
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")
        return None
    
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    # Basic data cleaning
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    
    # Remove invalid transactions
    df = df.dropna(subset=['wallet_address', 'transaction_type', 'amount'])
    df = df[df['amount'] > 0]
    
    print(f"Loaded {len(df)} transactions for {df['wallet_address'].nunique()} wallets")
    
    return df

def get_transaction_summary(df):
    """Get summary statistics of transactions"""
    
    summary = {
        'total_transactions': len(df),
        'unique_wallets': df['wallet_address'].nunique(),
        'transaction_types': df['transaction_type'].value_counts().to_dict(),
        'date_range': {
            'start': df['timestamp'].min(),
            'end': df['timestamp'].max()
        }
    }
    
    return summary
