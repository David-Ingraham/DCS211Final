from flask import Flask, render_template
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Read CSV data (replace 'your_data.csv' with your actual CSV file)
    csv_path = 'resources/transactions.csv'
    trasnactionsDf = pd.read_csv(csv_path)

    

    fig, axes = plt.subplots(2, 2, figsize=(18, 10))

    fig.suptitle('Revenue Distribution by Retailer')

    # Create multiple Seaborn visualizations using the CSV data
    plots = []


    violin_polt = sns.violinplot(ax=axes[0, 0], data=trasnactionsDf, x='Stock Ticker of Retailer', y='Transaction Amount')
    scatter_plot = sns.scatterplot(ax=axes[0, 1], data=trasnactionsDf, x='Stock Ticker of Retailer', y='Transaction Amount')
    barplot = sns.barplot(ax=axes[1, 0], data=trasnactionsDf, x='Stock Ticker of Retailer', y='Transaction Amount')
    box_plot = sns.boxplot(ax=axes[1, 1], data=trasnactionsDf, x='Stock Ticker of Retailer', y='Transaction Amount')

    plots.append(violin_polt)
    plots.append(scatter_plot)
    plots.append(barplot)
    plots.append(box_plot)

    

    # Save all plots to BytesIO objects
    img_bytes_list = []
    for plot in plots:

        img_bytes = BytesIO()
        fig.savefig(img_bytes, format='png')
        img_bytes.seek(0)
        # Encode the image bytes as base64
        img_bytes_list.append(base64.b64encode(img_bytes.read()).decode('utf-8'))


    # Render the HTML template with the list of embedded images
    return render_template('dashboard.html', img_bytes_list=img_bytes_list)

if __name__ == '__main__':
    app.run(debug=True)
