# 🏦 Aave V2 Credit Scoring System

A rule-based machine learning model that assigns credit scores (ranging from 0 to 1000) to DeFi wallets based on their historical transaction behavior on the Aave V2 protocol.

---

## 🎯 Objective

The goal of this project is to analyze transaction-level data from the Aave V2 protocol and score each wallet based on behavioral features such as loan repayment, liquidation history, and overall activity. This scoring system can be used to differentiate between responsible, risky, and bot-like wallets.

---

## 📊 Dataset

- **Source**: Aave V2 DeFi protocol
- **Format**: JSON (sample ~100K transactions)
- **Size**: ~87 MB
- **Transaction Types**:
  - `deposit`
  - `borrow`
  - `repay`
  - `redeemunderlying`
  - `liquidationcall`

---

## 🚀 How to Run

### ✅ Prerequisites

Make sure you have Python 3.8+ and the following Python packages installed:

```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

You can install them using:

```bash
pip install -r requirements.txt
```

### ▶️ Run the Script

```bash
python aave_credit_scoring.py
```

This will:
- Load and process the transaction JSON
- Generate behavior-based features
- Score each wallet on a 0–1000 scale
- Save:
  - `wallet_scores.csv` (wallet address + credit score)
  - `wallet_score_distribution.png` (score distribution plot)

---

## 🧠 Scoring Logic

Wallets are scored using a **weighted combination** of behavior-based features:

- 📈 **Positive Indicators**:
  - Repay-to-borrow ratio
  - High deposit and repay counts
  - Low liquidation events
  - Recent and regular activity

- ⚠️ **Negative Indicators**:
  - High borrow without repayment
  - Frequent liquidations
  - Inactive or one-time interactions

### Weight-based Heuristic Formula
Features were normalized and combined using this custom weighting:

| Feature | Weight |
|---------|--------|
| Total transactions | +1 |
| Deposit count | +1 |
| Borrow count | -0.5 |
| Repay count | +1 |
| Redeem count | +0.5 |
| Liquidation count | -1 |
| Total deposited | +1 |
| Total borrowed | -0.5 |
| Total repaid | +1 |
| Repay/Borrow ratio | +1 |
| Last activity timestamp | +0.2 |

The weighted sum is scaled to a 0–1000 range.

---

## 📂 Project Structure

```
aave-credit-scoring/
├── aave_credit_scoring.py            # Main script
├── wallet_scores.csv                 # Output: Wallet scores
├── wallet_score_distribution.png     # Output: Distribution graph
├── README.md                         # Project overview (this file)
├── analysis.md                       # Behavior analysis + observations
├── requirements.txt                  # Python dependencies
```

---

## 📈 Credit Score Ranges

| Score Range | Meaning |
|-------------|---------|
| 800–1000    | Excellent – Regular, responsible, low risk |
| 600–799     | Good – Mostly healthy usage |
| 400–599     | Fair – Average or moderate risk |
| 200–399     | Poor – Risky, incomplete repayment |
| 0–199       | Very Poor – High liquidation, suspicious activity |

---

## 📄 Deliverables

- ✅ `wallet_scores.csv`
- ✅ `wallet_score_distribution.png`
- ✅ `README.md`
- ✅ `analysis.md`

---

## 🧠 Why It Matters

Credit scoring in DeFi helps unlock undercollateralized lending opportunities. This model simulates the traditional financial scoring system in a decentralized setting and helps filter out unreliable or bot-like wallet behaviors.

---

## 👨‍💻 Author

**Jayesh Kamble** – AI Engineer Intern Candidate  
[LinkedIn]([https://linkedin.com/](https://www.linkedin.com/in/jayesh-kamble-/)) 

---

## 📄 License

This project is licensed under the MIT License.


