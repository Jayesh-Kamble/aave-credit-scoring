# Aave V2 Credit Scoring System

A machine learning model that assigns credit scores (0-1000) to cryptocurrency wallets based on their transaction behavior on the Aave V2 DeFi protocol.

## 🎯 Project Overview

This project develops a robust credit scoring system for DeFi wallets using transaction data from the Aave V2 protocol. The model identifies responsible vs. risky wallet behavior patterns.

## 📊 Dataset

- **Source**: Aave V2 protocol transaction data
- **Size**: 100K transaction records
- **Format**: JSON
- **Transaction Types**: deposit, borrow, repay, redeemunderlying, liquidationcall

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. Clone the repository:
git clone https://github.com/yourusername/aave-credit-scoring.git
cd aave-credit-scoring

text

2. Create virtual environment:
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. Install dependencies:
pip install -r requirements.txt

text

### Usage

Run the credit scoring system:
python main.py

text

This will:
- Process the JSON transaction data
- Generate features for each wallet
- Apply the ML model
- Output credit scores (0-1000)

## 🏗️ Project Structure

├── data/ # Data storage
├── src/ # Source code
│ ├── data_processing.py
│ ├── feature_engineering.py
│ ├── model.py
│ └── scoring.py
├── models/ # Trained models
├── notebooks/ # Jupyter notebooks
├── main.py # Main execution script
├── analysis.md # Score analysis
└── README.md

text

## 📈 Features

The model uses these key features:
- **Repayment Behavior**: Repay-to-borrow ratio
- **Activity Patterns**: Transaction frequency and duration
- **Risk Indicators**: Liquidation history
- **Portfolio Management**: Asset diversification

## 🎯 Credit Score Logic

- **800-1000**: Excellent (Consistent repayments, long-term user)
- **600-799**: Good (Reliable behavior, occasional issues)
- **400-599**: Fair (Average risk profile)
- **200-399**: Poor (High risk indicators)
- **0-199**: Very Poor (Frequent liquidations, poor repayment)

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Validation**: Time-series cross-validation
- **Key Metrics**: RMSE, MAE, R²

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Author

[Your Name] - AI Engineer Intern Candidate
