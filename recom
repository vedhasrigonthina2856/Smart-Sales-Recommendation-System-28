import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def generate_rules(file_path):
    df = pd.read_csv(file_path)

    basket = df.pivot_table(index='InvoiceNo',
                            columns='StockCode',
                            values='Quantity',
                            fill_value=0)

    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    frequent_items = apriori(basket, min_support=0.02, use_colnames=True)
    rules = association_rules(frequent_items, metric="lift", min_threshold=1)

    print(rules[['antecedents', 'consequents', 'lift']].head())

if __name__ == "__main__":
    generate_rules("../data/cleaned.csv")
