import csv
import random
from datetime import datetime, timedelta

def generate_transaction(index):
    retailers = ["Walmart", "Target", "Amazon", "Home Depot", "Costco"]
    stock_tickers = ["WMT", "TGT", "AMZN", "HD", "COST"]
    
    iso_date_time = (datetime.now() - timedelta(days=random.randint(1, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59), seconds=random.randint(0, 59))).isoformat()
    retailer = random.choice(retailers)
    stock_ticker = stock_tickers[retailers.index(retailer)]
    transaction_amount = round(random.uniform(10.0, 500.0), 2)

    return [index, iso_date_time, retailer, stock_ticker, transaction_amount]

def generate_csv(file_path, num_transactions):
    header = ["Index", "ISO Date and Time of transaction", "Name of Retailer", "Stock Ticker of Retailer", "Transaction Amount"]
    data = [header] + [generate_transaction(i) for i in range(1, num_transactions + 1)]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    file_path = "transactions.csv"
    num_transactions = 50

    generate_csv(file_path, num_transactions)
    print(f"{num_transactions} transactions have been generated and saved to {file_path}.")
