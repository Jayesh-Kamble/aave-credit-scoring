import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_scores(model, features_df):
    """Generate credit scores for all wallets"""
    
    # Get predictions
    scores = model.predict(features_df)
    
    # Create results DataFrame
    results = pd.DataFrame({
        'wallet_address': features_df['wallet_address'],
        'credit_score': scores.round(0).astype(int),
        'score_category': categorize_scores(scores)
    })
    
    # Add feature information
    results = results.merge(features_df, on='wallet_address', how='left')
    
    return results

def categorize_scores(scores):
    """Categorize scores into risk buckets"""
    
    categories = []
    for score in scores:
        if score >= 800:
            categories.append('Excellent')
        elif score >= 600:
            categories.append('Good')
        elif score >= 400:
            categories.append('Fair')
        elif score >= 200:
            categories.append('Poor')
        else:
            categories.append('Very Poor')
    
    return categories

def analyze_score_distribution(scores_df):
    """Analyze score distribution and create visualizations"""
    
    print("Analyzing score distribution...")
    
    # Score distribution by ranges
    score_ranges = {
        '0-100': len(scores_df[(scores_df['credit_score'] >= 0) & (scores_df['credit_score'] < 100)]),
        '100-200': len(scores_df[(scores_df['credit_score'] >= 100) & (scores_df['credit_score'] < 200)]),
        '200-300': len(scores_df[(scores_df['credit_score'] >= 200) & (scores_df['credit_score'] < 300)]),
        '300-400': len(scores_df[(scores_df['credit_score'] >= 300) & (scores_df['credit_score'] < 400)]),
        '400-500': len(scores_df[(scores_df['credit_score'] >= 400) & (scores_df['credit_score'] < 500)]),
        '500-600': len(scores_df[(scores_df['credit_score'] >= 500) & (scores_df['credit_score'] < 600)]),
        '600-700': len(scores_df[(scores_df['credit_score'] >= 600) & (scores_df['credit_score'] < 700)]),
        '700-800': len(scores_df[(scores_df['credit_score'] >= 700) & (scores_df['credit_score'] < 800)]),
        '800-900': len(scores_df[(scores_df['credit_score'] >= 800) & (scores_df['credit_score'] < 900)]),
        '900-1000': len(scores_df[(scores_df['credit_score'] >= 900) & (scores_df['credit_score'] <= 1000)])
    }
    
    # Create visualizations
    create_score_visualizations(scores_df, score_ranges)
    
    return score_ranges

def create_score_visualizations(scores_df, score_ranges):
    """Create score distribution visualizations"""
    
    plt.figure(figsize=(15, 10))
    
    # Score distribution histogram
    plt.subplot(2, 2, 1)
    plt.hist(scores_df['credit_score'], bins=50, alpha=0.7, edgecolor='black')
    plt.title('Credit Score Distribution')
    plt.xlabel('Credit Score')
    plt.ylabel('Number of Wallets')
    plt.grid(True, alpha=0.3)
    
    # Score ranges bar chart
    plt.subplot(2, 2, 2)
    ranges = list(score_ranges.keys())
    counts = list(score_ranges.values())
    plt.bar(ranges, counts, alpha=0.7)
    plt.title('Score Distribution by Ranges')
    plt.xlabel('Score Range')
    plt.ylabel('Number of Wallets')
    plt.xticks(rotation=45)
    
    # Score by category
    plt.subplot(2, 2, 3)
    category_counts = scores_df['score_category'].value_counts()
    plt.pie(category_counts.values, labels=category_counts.index, autopct='%1.1f%%')
    plt.title('Score Distribution by Category')
    
    # Box plot of scores by category
    plt.subplot(2, 2, 4)
    sns.boxplot(data=scores_df, y='score_category', x='credit_score')
    plt.title('Score Distribution by Category (Box Plot)')
    
    plt.tight_layout()
    plt.savefig('docs/score_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()

def analyze_high_low_scorers(scores_df):
    """Analyze characteristics of high and low scoring wallets"""
    
    high_scorers = scores_df[scores_df['credit_score'] >= 700]
    low_scorers = scores_df[scores_df['credit_score'] < 300]
    
    print(f"\nHigh Scorers (≥700): {len(high_scorers)} wallets")
    print(f"Average repay ratio: {high_scorers['repay_to_borrow_ratio'].mean():.2f}")
    print(f"Average days active: {high_scorers['days_active'].mean():.0f}")
    print(f"Average liquidation rate: {high_scorers['liquidation_rate'].mean():.3f}")
    
    print(f"\nLow Scorers (<300): {len(low_scorers)} wallets")
    print(f"Average repay ratio: {low_scorers['repay_to_borrow_ratio'].mean():.2f}")
    print(f"Average days active: {low_scorers['days_active'].mean():.0f}")
    print(f"Average liquidation rate: {low_scorers['liquidation_rate'].mean():.3f}")
    
    return high_scorers, low_scorers
