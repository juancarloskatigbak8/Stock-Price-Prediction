import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

benchmark_data = pd.DataFrame({
    "Algorithm": [
        "Linear Regression (Pandas)", "Linear Regression (Polars)",
        "Random Forest (Pandas)", "Random Forest (Polars)"
    ],
    "MAE": [55.33, 57.51, 52.26, 60.98],
    "MSE": [13088, 16498, 10733, 18246],
    "R² Score": [0.19, -0.01, 0.34, -0.12]
})

enhanced_csv_path = "all_stocks_5yr_enhanced_pandas.csv"
df = pd.read_csv(enhanced_csv_path)

st.title("Stock Price Prediction Dashboard")

st.header("Benchmark Results (Pandas vs. Polars)")
st.table(benchmark_data)

st.subheader("Model Performance (R² Score)")
fig, ax = plt.subplots()
colors = ["blue", "orange", "green", "red"]
ax.bar(benchmark_data["Algorithm"], benchmark_data["R² Score"], color=colors)
ax.set_xlabel("Algorithm")
ax.set_ylabel("R² Score")
plt.xticks(rotation=45, ha="right")
plt.legend(["R² Score"])
st.pyplot(fig)

st.header("Stock Price Predictions")
st.subheader("Actual vs Predicted Prices")

stock_ticker = st.selectbox("Select a stock ticker:", df["name"].unique())

df_filtered = df[df["name"] == stock_ticker]

fig, ax = plt.subplots()
ax.plot(df_filtered["date"], df_filtered["close"], label="Actual Price", color="blue")
ax.plot(df_filtered["date"], df_filtered["SMA_20"], linestyle="dashed", label="Predicted Price (SMA)", color="red")

ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.set_title(f"Actual vs Predicted Prices for {stock_ticker}")
ax.legend()

st.pyplot(fig)

st.write("This chart compares actual closing prices with predictions using technical indicators (SMA, EMA).")
