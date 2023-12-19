from flask import Flask, render_template, request, redirect, url_for
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import pandas as pd

app = Flask(__name__)

# Dummy username and password (replace with a proper authentication mechanism)
correct_username = "user"
correct_password = "password"

@app.route('/', methods=['GET', 'POST'])
def login() -> str:
    """
    Handles user authentication based on form data and redirects to the dashboard on success.

    Returns:
    str: HTML content for the login page or a redirect to the dashboard.

    Example:
    >>> login()
    '<html>...</html>'
    """
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        # Dummy authentication (replace with a proper authentication mechanism)
        if username == correct_username and password == correct_password:
            # Redirect to the dashboard page if authentication is successful
            return redirect(url_for('dashboard'))

    # Render the login page
    return render_template('login.html')

@app.route('/dashboard')
def dashboard() -> str:
    """
    Generates a dashboard with Seaborn visualizations using transaction data from a CSV file.

    Returns:
    str: HTML content for the dashboard.

    Example:
    >>> dashboard()
    '<html>...</html>'
    """
    csv_path = 'resources/transactions.csv'
    transactions_df = pd.read_csv(csv_path)

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
    return render_template('dashboard.html', img_bytes_list=img_bytes_list)

if __name__ == '__main__':
    app.run(debug=True)
