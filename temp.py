from flask import Flask, render_template
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd


transactions_df = pd.read_csv("resources/transactions.csv")

    
fig, axes = plt.subplots(2, 2, figsize=(18, 10))

fig.suptitle('Revenue Distribution by Retailer')

# Create multiple Seaborn visualizations using the CSV data
plots = []


img_bytes_list = []
    
for _ in range(4):  # Create 4 different plots
    fig, ax = plt.subplots(2, 2, figsize=(6, 4))

    if len(plots) == 0:
        fig.suptitle('Revenue Distribution by Retailer')

        # Choose a different seaborn plot type for each iteration
    if len(plots) == 0:
        plot = sns.violinplot(ax=ax[0,0], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    elif len(plots) == 1:
        plot = sns.scatterplot(ax=ax[0,1], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    elif len(plots) == 2:
        plot = sns.barplot(ax=ax[1,0], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')
    else:
        plot = sns.boxplot(ax=ax[1,1], data=transactions_df, x='Stock Ticker of Retailer', y='Transaction Amount')

    plots.append(plot)

    img_bytes = BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # Encode the image bytes as base64
    img_bytes_list.append(base64.b64encode(img_bytes.read()).decode('utf-8'))

print(plots)

print("\n\n")

print(f"num of plots: {len(plots)}")