import streamlit as st
import pandas as pd
import pickle

# Load data
df = pd.read_csv("../data/cleaned.csv")

st.title("🛒 Retail Intelligence Dashboard")

# Monthly Sales
st.subheader("📊 Monthly Sales")
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.month

monthly_sales = df.groupby('Month')['TotalPrice'].sum()
st.bar_chart(monthly_sales)

# Top Products
st.subheader("🏆 Top Products")
top_products = df.groupby('StockCode')['Quantity'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

# Prediction
st.subheader("🔮 Sales Prediction")

model = pickle.load(open("../models/model.pkl", "rb"))

qty = st.number_input("Enter Quantity", min_value=1)

if st.button("Predict"):
    prediction = model.predict([[qty]])
    st.success(f"Predicted Sales: {prediction[0]:.2f}")
