# 🏦 Aave V2 Credit Scoring System

A machine learning pipeline that assigns credit scores (0–1000) to cryptocurrency wallets based on their transaction behavior on the Aave V2 DeFi protocol.

---

## 🎯 Project Overview

This project aims to develop a robust credit scoring system for DeFi wallets using transaction-level data from the Aave V2 protocol. The model identifies responsible vs. risky wallet behavior by analyzing user interactions such as deposits, borrows, repayments, redemptions, and liquidations.

---

## 📊 Dataset

- **Source**: Aave V2 protocol (DeFi transaction history)
- **Size**: ~100K records
- **Format**: JSON
- **Transaction Types**:
  - `deposit`
  - `borrow`
  - `repay`
  - `redeemunderlying`
  - `liquidationcall`

---

## 🚀 Quick Start

### ✅ Prerequisites

- Python 3.8+
- `pip` package manager

### ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/aave-credit-scoring.git
   cd aave-credit-scoring
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Usage

Run the credit scoring system:
```bash
python main.py
```

This will:
- Load and process the JSON transaction data
- Generate features per wallet
- Apply the credit scoring model
- Output wallet scores in the range of 0–1000

---

## 🏗️ Project Structure

```
aave-credit-scoring/
├── data/                  # Raw and processed data
│   └── user_transactions.json
├── models/                # Trained models (if any)
├── notebooks/             # Jupyter notebooks for analysis
├── src/                   # Source code
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── scoring.py
├── main.py                # Main execution script
├── analysis.md            # Score distribution analysis
├── README.md              # Project overview and instructions
└── requirements.txt       # Python dependencies
```

---

## 📈 Features Used in Scoring

The model uses the following features derived from wallet behavior:

- **Repayment Behavior**: `repay_to_borrow_ratio`
- **Activity Patterns**: Number and type of actions (deposits, borrows, redeems, etc.)
- **Risk Indicators**: Number of `liquidationcall` events
- **Engagement**: Frequency and recency of wallet activity
- **Volume Behavior**: Total deposited, borrowed, and repaid amounts

---

## 🎯 Credit Score Logic

| Score Range | Description                             |
|-------------|-----------------------------------------|
| 800–1000    | Excellent – Long-term, responsible user |
| 600–799     | Good – Generally reliable               |
| 400–599     | Fair – Moderate risk                    |
| 200–399     | Poor – Risky behavior detected          |
| 0–199       | Very Poor – Frequent liquidations, bots |

---

## 📊 Model Performance

- **Algorithm**: Random Forest Regressor
- **Validation**: Time-series cross-validation
- **Metrics**:
  - RMSE (Root Mean Square Error)
  - MAE (Mean Absolute Error)
  - R² Score

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Author

**[Jayesh Kamble]** – AI Engineer Intern Candidate

[LinkedIn](https://www.linkedin.com/) | [GitHub](https://github.com/)
