from flask import Flask, render_template
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd


# Read CSV data (replace 'your_data.csv' with your actual CSV file)
    csv_path = 'resources/transactions.csv'
    transactions_df = pd.read_csv(csv_path)

    

    # Create multiple Seaborn visualizations using the CSV data
  # Create multiple Seaborn visualizations using the CSV data
    plots = []

    img_bytes_list = []
    
    # Create a single 2 by 2 grid
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Revenue Distribution by Retailer')

    # Choose a different seaborn plot type for each subplot
    plot = sns.violinplot(ax=axes[0, 0], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    plots.append(plot)

    plot = sns.scatterplot(ax=axes[0, 1], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    plots.append(plot)

    plot = sns.barplot(ax=axes[1, 0], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    plots.append(plot)

    plot = sns.boxplot(ax=axes[1, 1], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    plots.append(plot)

    # Save the single 2 by 2 grid to BytesIO object
    img_bytes = BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # Encode the image bytes as base64
    img_bytes_list.append(base64.b64encode(img_bytes.read()).decode('utf-8'))

    plt.close(fig)