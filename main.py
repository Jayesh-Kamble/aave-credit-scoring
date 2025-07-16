#!/usr/bin/env python3
"""
Aave V2 Credit Scoring System
Author: [Your Name]
Date: July 2025
"""

import json
import pandas as pd
import numpy as np
from src.data_processing import load_and_clean_data
from src.feature_engineering import create_features
from src.model import CreditScoringModel
from src.scoring import generate_scores

def main():
    """Main execution function"""
    print("Starting Aave V2 Credit Scoring System...")
    
    # Load data
    print("Loading transaction data...")
    data = load_and_clean_data('data/user_transactions.json')
    
    # Create features
    print("Engineering features...")
    features = create_features(data)
    
    # Initialize and train model
    print("Training model...")
    model = CreditScoringModel()
    model.train(features)
    
    # Generate scores
    print("Generating credit scores...")
    scores = generate_scores(model, features)
    
    # Save results
    scores.to_csv('data/processed/credit_scores.csv', index=False)
    print(f"Credit scores generated for {len(scores)} wallets")
    print("Results saved to data/processed/credit_scores.csv")

if __name__ == "__main__":
    main()
