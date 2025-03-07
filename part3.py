import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


@st.cache_data
def load_benchmark_data():
    benchmark_data = pd.DataFrame({
        "Algorithm": [
            "Linear Regression (Pandas)", "Linear Regression (Polars)",
            "Random Forest (Pandas)", "Random Forest (Polars)"
        ],
        "MAE": [57.89, 57.51, 62.61, 60.98],
        "MSE": [16435, 16498, 17011, 18231],
        "R² Score": [-0.01, -0.01, -0.04, -0.12]
    })
    
    storage_benchmark = pd.DataFrame({
        "File Name": ["all_stocks_5yr.csv", "all_stocks_5yr.parquet",
                      "all_stocks_5yr_10x.csv", "all_stocks_5yr_10x.parquet",
                      "all_stocks_5yr_100x.csv", "all_stocks_5yr_100x.parquet"],
        "Kind of File": ["CSV", "Parquet", "CSV", "Parquet", "CSV", "Parquet"],
        "Scale": ["1x", "1x", "10x", "10x", "100x", "100x"],
        "Size": ["30.1 MB", "10.6 MB", "295.8 MB", "99.9 MB", "2.96 GB", "997.2 MB"],
        "Read Time (ms)": [471, 99.5, 11200, 967, 78000, 41600],
        "Speedup": ["-", "7.5x faster", "-", "6.3x faster", "-", "19.4x faster"]
    })
    
    return benchmark_data, storage_benchmark


@st.cache_data
def load_stock_data():
    df = pd.read_csv("all_stocks_5yr_enhanced_pandas.csv", parse_dates=["date"])
    df = df.sort_values(by="date")
    return df


benchmark_data, storage_benchmark = load_benchmark_data()
df = load_stock_data()


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Benchmark Results", "Stock Price Prediction"])


if page == "Benchmark Results":
    st.title("Benchmark Results")


    st.subheader("Model Performance")

    benchmark_long = benchmark_data.melt(id_vars=["Algorithm"], 
                                         var_name="Metric", 
                                         value_name="Value")

    fig1 = px.bar(benchmark_long, 
                  x="Algorithm", 
                  y="Value", 
                  color="Metric", 
                  barmode="group", 
                  title="Model Performance Comparison (MAE, MSE, R² Score)")
    
    st.plotly_chart(fig1)


    st.subheader("Storage Performance")

    fig2 = px.bar(storage_benchmark, 
                  x="Scale", 
                  y="Read Time (ms)", 
                  color="Kind of File", 
                  barmode="group",
                  title="CSV vs Parquet Read Time Across Different Scales")
    
    st.plotly_chart(fig2)


elif page == "Stock Price Prediction":
    st.title("Stock Price Predictions")
    

    stock_ticker = st.selectbox("Select a stock ticker:", df["name"].unique())


    df_stock = df[df["name"] == stock_ticker]


    fig3 = go.Figure()


    fig3.add_trace(go.Candlestick(
        x=df_stock["date"],
        open=df_stock["open"],
        high=df_stock["high"],
        low=df_stock["low"],
        close=df_stock["close"],
        name="Actual Price",
        increasing_line_color="green",
        decreasing_line_color="red"
    ))


    fig3.add_trace(go.Scatter(
        x=df_stock["date"], 
        y=df_stock["close"].shift(-1),
        mode="lines",
        name="Predicted Price",
        line=dict(color="black", dash="dot")
    ))


    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["SMA_20"], 
                              mode="lines", name="SMA (20)", line=dict(color='blue')))
    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["EMA_20"], 
                              mode="lines", name="EMA (20)", line=dict(color='orange', dash='dot')))


    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["BB_High"], 
                              mode="lines", name="Bollinger High", line=dict(color='purple', dash='dot')))
    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["BB_Low"], 
                              mode="lines", name="Bollinger Low", line=dict(color='purple', dash='dot')))


    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["MACD"], 
                              mode="lines", name="MACD", line=dict(color='green')))
    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["MACD_Signal"], 
                              mode="lines", name="MACD Signal", line=dict(color='red')))


    fig3.add_trace(go.Scatter(x=df_stock["date"], y=df_stock["Stoch"], 
                              mode="lines", name="Stochastic Oscillator", line=dict(color='brown', dash='dot')))


    fig3.update_layout(title=f"Stock Price Prediction with Technical Indicators - {stock_ticker}",
                       xaxis_title="Date",
                       yaxis_title="Price",
                       xaxis_rangeslider_visible=False,
                       height=600,
                       legend=dict(orientation="h", yanchor="top", y=1.1, xanchor="center", x=0.5))

    st.plotly_chart(fig3)
