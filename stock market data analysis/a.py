import pandas as pd
import matplotlib.pyplot as plt
# Load the dataset
stock_df = pd.read_csv("stockdata.csv")
# Convert Date column to datetime
stock_df["Date"] = pd.to_datetime(stock_df["Date"])
# Check for missing values
print("\nMissing Values in Stock Market Dataset:")
print(stock_df.isnull().sum())
# Summary statistics
print("\nStock Market Summary Statistics:")
print(stock_df.describe())
# Plot Stock Market Trends
plt.figure(figsize=(12, 6))
for col in ["MSFT", "IBM", "SBUX", "AAPL", "GSPC"]:
    plt.plot(stock_df["Date"], stock_df[col], label=col)
plt.title("Stock Market Trends Over Time", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Stock Price", fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()