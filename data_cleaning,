import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path, encoding='ISO-8859-1')

    # Remove nulls
    df.dropna(inplace=True)

    # Remove negative quantity
    df = df[df['Quantity'] > 0]

    # Convert date
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # Create total price
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    df.to_csv(output_path, index=False)
    print("Data cleaned and saved!")

if __name__ == "__main__":
    clean_data("../data/raw.csv", "../data/cleaned.csv")
