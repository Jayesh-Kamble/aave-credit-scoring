import pandas as pd
import numpy as np

def create_features(df):
    """Create features for credit scoring model"""
    
    print("Creating features for credit scoring...")
    
    # Group by wallet address
    wallet_features = []
    
    for wallet in df['wallet_address'].unique():
        wallet_data = df[df['wallet_address'] == wallet]
        
        # Basic transaction features
        features = {
            'wallet_address': wallet,
            'total_transactions': len(wallet_data),
            'total_volume': wallet_data['amount'].sum(),
            'avg_transaction_size': wallet_data['amount'].mean(),
            'days_active': (wallet_data['timestamp'].max() - 
                           wallet_data['timestamp'].min()).days + 1
        }
        
        # Transaction type counts
        tx_counts = wallet_data['transaction_type'].value_counts()
        features['deposit_count'] = tx_counts.get('deposit', 0)
        features['borrow_count'] = tx_counts.get('borrow', 0)
        features['repay_count'] = tx_counts.get('repay', 0)
        features['redeem_count'] = tx_counts.get('redeemunderlying', 0)
        features['liquidation_count'] = tx_counts.get('liquidationcall', 0)
        
        # Calculate key ratios
        features['repay_to_borrow_ratio'] = (
            features['repay_count'] / max(features['borrow_count'], 1)
        )
        features['deposit_to_borrow_ratio'] = (
            features['deposit_count'] / max(features['borrow_count'], 1)
        )
        
        # Risk indicators
        features['liquidation_rate'] = (
            features['liquidation_count'] / features['total_transactions']
        )
        features['avg_daily_transactions'] = (
            features['total_transactions'] / max(features['days_active'], 1)
        )
        
        # Behavioral patterns
        features['transaction_diversity'] = len(tx_counts)
        features['is_long_term_user'] = 1 if features['days_active'] > 30 else 0
        features['is_active_user'] = 1 if features['total_transactions'] > 10 else 0
        
        wallet_features.append(features)
    
    features_df = pd.DataFrame(wallet_features)
    
    print(f"Created {len(features_df.columns)-1} features for {len(features_df)} wallets")
    
    return features_df

def select_model_features(features_df):
    """Select features for the ML model"""
    
    model_features = [
        'total_transactions',
        'total_volume',
        'avg_transaction_size',
        'days_active',
        'repay_to_borrow_ratio',
        'deposit_to_borrow_ratio',
        'liquidation_rate',
        'avg_daily_transactions',
        'transaction_diversity',
        'is_long_term_user',
        'is_active_user'
    ]
    
    return features_df[['wallet_address'] + model_features]
