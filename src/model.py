import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

class CreditScoringModel:
    """Credit scoring model for Aave V2 wallets"""
    
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            max_depth=10
        )
        self.scaler = StandardScaler()
        self.feature_columns = None
        
    def create_target_scores(self, features_df):
        """Create target scores based on wallet behavior"""
        
        scores = []
        
        for _, row in features_df.iterrows():
            score = 500  # Start with neutral score
            
            # Reward good behaviors
            if row['repay_to_borrow_ratio'] > 1.0:
                score += 200
            elif row['repay_to_borrow_ratio'] > 0.8:
                score += 100
            
            if row['days_active'] > 90:
                score += 150
            elif row['days_active'] > 30:
                score += 75
            
            if row['total_transactions'] > 50:
                score += 100
            elif row['total_transactions'] > 20:
                score += 50
            
            if row['is_long_term_user']:
                score += 50
            
            if row['transaction_diversity'] > 3:
                score += 50
            
            # Penalize risky behaviors
            if row['liquidation_rate'] > 0.05:
                score -= 400
            elif row['liquidation_rate'] > 0.02:
                score -= 200
            
            if row['repay_to_borrow_ratio'] < 0.5:
                score -= 200
            
            if row['avg_daily_transactions'] > 10:
                score -= 100  # Potential bot behavior
            
            # Ensure score is between 0 and 1000
            score = max(0, min(1000, score))
            scores.append(score)
        
        return np.array(scores)
    
    def train(self, features_df):
        """Train the credit scoring model"""
        
        # Select features for model
        feature_cols = [col for col in features_df.columns if col != 'wallet_address']
        self.feature_columns = feature_cols
        
        X = features_df[feature_cols]
        y = self.create_target_scores(features_df)
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model trained successfully!")
        print(f"RMSE: {rmse:.2f}")
        print(f"R²: {r2:.3f}")
        
        return self
    
    def predict(self, features_df):
        """Predict credit scores for wallets"""
        
        X = features_df[self.feature_columns]
        X_scaled = self.scaler.transform(X)
        
        scores = self.model.predict(X_scaled)
        
        # Ensure scores are between 0 and 1000
        scores = np.clip(scores, 0, 1000)
        
        return scores
    
    def save_model(self, filepath):
        """Save trained model"""
        model_data = {
            'model': self.model,
            'scaler': self.scaler,
            'feature_columns': self.feature_columns
        }
        joblib.dump(model_data, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        """Load trained model"""
        model_data = joblib.load(filepath)
        self.model = model_data['model']
        self.scaler = model_data['scaler']
        self.feature_columns = model_data['feature_columns']
        print(f"Model loaded from {filepath}")
