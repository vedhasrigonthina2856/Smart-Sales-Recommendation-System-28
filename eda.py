import pandas as pd
import matplotlib.pyplot as plt

def perform_eda(file_path):
    df = pd.read_csv(file_path)

    # Monthly sales
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['Month'] = df['InvoiceDate'].dt.month

    monthly_sales = df.groupby('Month')['TotalPrice'].sum()

    print("Monthly Sales:\n", monthly_sales)

    monthly_sales.plot(kind='bar', title="Monthly Sales")
    plt.savefig("../outputs/charts/monthly_sales.png")
    plt.show()

if __name__ == "__main__":
    perform_eda("../data/cleaned.csv")
