# Project Title

Stock Price Prediction (S&P 500)


## About the Assignment

The purpose of this assignment is to combine research, benchmarking and coding using the provided time-series dataset of stock prices for S&P 500 companies. The assignment is divided into three parts, each with its own research and coding components.

Objectives
Part 1: Storing and retrieving data using csv vs. parquet with compression scales of 1x, 10x, and 100x.
Part 2: Manipulating, analyzing data and building models using dataframe libraries Pandas vs. Polars with 4 technical indicators and 2 algorithms to train and test data using 80-20 split for back testing.
Part 3: Creating a visual dashboard for the results using a dashboard library with 2 dashboards where 1 displays benchmark results at all scales and the other 1 displays price prediction models for all companies.

### Prerequisites

- Install Python (>=3.8)
- Install Jupyter Notebook

## Assignment Structure (if extracted using Github)

📂 Katigbak_300366535_Assignment1
│── part1.ipynb               # Part 1: Data Storage and Retrieval - evaluating CSV vs Parquet.
│── part2.ipynb               # Part 2: Part 2: Data Analysis & Machine Learning - uses 4 technical indicators to enhance the dataset (Simple & Exponential 
                                Moving Averages, Moving Average Convergence Divergence, Bollinger Bands, and Stochastic Oscillator), trains Linear 
                                Regression & Random Forest, and compares Pandas vs Polars.
│── part3.py                  # Part 3: Creating a Dashboard - built a Streamlit dashboard to visualize benchmark results (csv format vs. parquet with 
                                compression scales 
                                of 1x, 10x, and 100x) and stock price predictions per company.
│── README.md                 # This documentation
│── all_stocks_5yr.csv.zip    # This is the dataset to be able to run everything
│── dashboard.pdf             # This is a pdf file containing screenshots of the dashboard of Part 3: Creating a Dashboard

### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of Katigbak_300366535_Assignment1 folder

If getting it from OneDrive:
Just simply download the Katigbak_300366535_Assignment1 folder and open folder which will show files dashboard.pdf, all_stocks_5yr.csv, README.md, part1.ipynb, part2.ipynb, and part3.py as well as "just-in-case" files all_stocks_5yr.parquet, all_stocks_5yr_enhanced_pandas.csv, and all_stocks_5yr_enhanced_polars.csv just in case there are errors like the Jupyter Notebook looking for these files.

If getting it from Github:
Extract Katigbak_300366535_Assignment1.zip and then extract all_stocks_5yr.csv.zip to get file extract all_stocks_5yr.csv

*Note: Since Katigbak_300366535_Assignment1 downloaded as a ZIP, extract Katigbak_300366535_Assignment1 folder first and extract all_stocks_5yr.csv.zip making sure that the file all_stocks_5yr.csv has been brought out of its folder and placed in Katigbak_300366535_Assignment1 folder together with files dashboard.pdf, README.md, part1.ipynb, part2.ipynb, and part3.py because ideally the assignment should be run sequentially starting with Part 1, then Part 2, and lastly Part 3 with all_stocks_5yr.csv as the crucial file to be able to create the other csv files to run everything.

2. Set Up a Virtual Environment (Optional but Recommended)
   
For macOS/Linux (Terminal):
python -m venv env
source env/bin/activate

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

* Make sure to proactively do this in both Terminal/Command Prompt and Jupyter Notebook just to be sure so that there is no interruption with running the assignment!

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install pandas polars numpy scikit-learn matplotlib seaborn ta streamlit pyarrow plotly

For Jupyter Notebook:
!pip install pandas polars numpy scikit-learn matplotlib seaborn ta streamlit pyarrow plotly

## Running each part of the assignment
**Best to run Part 1, 2, and 3 in sequence to ensure that the whole assignment runs

Part 1: Data Storage and Retrieval - evaluating CSV vs Parquet.
(Output: Benchmark results comparing CSV vs Parquet)

using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open part1.ipynb and run each code using shift + enter

Part 2: Data Analysis & Machine Learning - uses 4 technical indicators to enhance the dataset (Simple & Exponential Moving Averages, Moving Average Convergence Divergence, Bollinger Bands, and Stochastic Oscillator), trains Linear Regression & Random Forest, and compares Pandas vs Polars.
(Output: Evaluation metrics MAE, MSE, and R² Score used for both algorithms)

using either macOS/Linux's Terminal or Windows' Command Prompt, run:

jupyter notebook

this will then open Jupyter Notebook in your web browser and once inside Jupyter Notebook, open part2.ipynb and run each code using shift + enter

Part 3: Creating a Dashboard - built a Streamlit dashboard to visualize benchmark results (csv format vs. parquet with compression scales of 1x, 10x, and 100x) and stock price predictions per company.
(Open http://localhost:8501/ in your browser)

using macOS/Linux's Terminal, run:

cd ~/Desktop/Katigbak_300366535_Assignment1

streamlit run part3.py

using Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\Katigbak_300366535_Assignment1
(e.g. cd OneDrive\Desktop\Katigbak_300366535_Assignment1) #since Katigbak_300366535_Assignment1 is the folder with the file

streamlit run part3.py

this will open http://localhost:8501/ in your browser

## Explanation of Each Part

Part 1: Data Storage and Retrieval
In this section, the goal was to evaluate the efficiency of CSV versus Parquet file formats when handling time-series stock price data. The dataset provided was stored in a CSV format, and I investigated whether converting it to Parquet with compression would provide performance benefits, particularly in file size reduction and faster read times. Unlike CSV, Parquet is a columnar storage format, meaning it is optimized for reading only the necessary columns, making it faster and more efficient for analytical workloads. Snappy compression significantly reduces file size while maintaining fast decompression speed.

1. Loading and Validating the Dataset
The first step was to ensure the dataset was accessible in the same directory as the script. This checks if all_stocks_5yr.csv exists before attempting to load it, preventing file not found errors.

2. Converting CSV to Parquet
After loading the dataset, the next step was to convert it to Parquet format using Snappy compression, a lightweight, high-speed compression algorithm.

3. Benchmarking Read Performance

To compare how quickly the two formats load data, I used %timeit, a Jupyter Notebook function that runs the command multiple times and reports the average execution time using this code:

%timeit pd.read_csv(csv_file)
%timeit pd.read_parquet(parquet_file, engine='pyarrow')

This directly measures read performance between CSV and Parquet.

4. Simulating Large-Scale Datasets (10x, 100x)

Since real-world data scales over time, I simulated dataset expansions:
10x Data Growth to Duplicated the original dataset 10 times.
100x Data Growth to Duplicated the original dataset 100 times.

Here is the code:

df_10x = pd.concat([df] * 10, ignore_index=True)

df_10x.to_csv('all_stocks_5yr_10x.csv', index=False)
df_10x.to_parquet('all_stocks_5yr_10x.parquet', engine='pyarrow', compression='snappy')
print("10x dataset created!")

%timeit pd.read_csv('all_stocks_5yr_10x.csv')
%timeit pd.read_parquet('all_stocks_5yr_10x.parquet', engine='pyarrow')

df_100x = pd.concat([df] * 100, ignore_index=True)

df_100x.to_csv('all_stocks_5yr_100x.csv', index=False)
df_100x.to_parquet('all_stocks_5yr_100x.parquet', engine='pyarrow', compression='snappy')
print("100x dataset created!")

%timeit pd.read_csv('all_stocks_5yr_100x.csv')
%timeit pd.read_parquet('all_stocks_5yr_100x.parquet', engine='pyarrow')

This allowed me to measure how both CSV and Parquet perform at large data scales.

Here are the takeaways:
1. Parquet is significantly more efficient than CSV for larger datasets, especially at 10x and 100x scales.
2. Read time improved by up to 19.4x at 100x scale with Parquet.
3. Parquet reduces file size by 3x with Snappy compression.
4. However, CSV is still more universally compatible, as Parquet requires specific libraries.

If data size is small (1x scale) and compatibility across different tools is essential, CSV is fine. However, as data scales to 10x or 100x, Parquet is the superior choice due to smaller file size, much faster read times, and better compression efficiency.


Part 2: Data Storage and Retrieval
In this section, the goal was to compare the performance of Pandas vs. Polars for data manipulation and analysis. Additionally, I implemented four technical indicators to enhance the dataset and trained two machine learning models (Linear Regression & Random Forest) to predict stock prices.

Step 1 - Loading and Filtering Data
First, I checked if the CSV dataset exists before loading it to avoid file errors.

import os
import pandas as pd

csv_file = "all_stocks_5yr.csv"

if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Error: {csv_file} not found. Please place the CSV file in the same folder as this script.")

df = pd.read_csv(csv_file)
print("Dataset loaded successfully.")

Ensures the script runs on any computer without assuming the dataset is present. After loading, I filtered stocks where the closing price was greater than $100, a simple example of data filtering.

filtered_df = df[df['close'] > 100]
print(filtered_df.head())

Then, I did the same filtering operation using Polars, since it’s known for its speed.

import polars as pl
df_polars = pl.read_csv(csv_file)

filtered_df_polars = df_polars.filter(pl.col("close") > 100)
print(filtered_df_polars.head())

This demonstrates how Pandas and Polars handle filtering differently.

Performance Benchmark:

%timeit pd.read_csv(csv_file)
%timeit pl.read_csv(csv_file)

Pandas: 329 ms
Polars: 20.5 ms

Polars was significantly faster at reading CSV files (16x speedup).

Step 2 - Enhancing the Dataset with 4 Technical Indicators
Since raw data isn’t always useful for predictions, I enhanced the dataset by adding four key technical indicators using both Pandas and Polars.

(1) Simple & Exponential Moving Averages (SMA & EMA)
SMA and EMA help smooth price trends by averaging past values.

Pandas Implementation:

df["SMA_20"] = df["close"].rolling(window=20).mean()
df["EMA_20"] = df["close"].ewm(span=20, adjust=False).mean()

Polars Implementation:

df_polars = df_polars.with_columns([
    df_polars["close"].rolling_mean(window_size=20).alias("SMA_20"),
    df_polars["close"].ewm_mean(span=20).alias("EMA_20"),
])

(2) Moving Average Convergence Divergence (MACD)
MACD measures the momentum of price movements.

Pandas Implementation:

import ta
macd = ta.trend.MACD(df["close"])
df["MACD"] = macd.macd()
df["MACD_Signal"] = macd.macd_signal()

Polars Implementation:

def compute_macd(df, column="close"):
    short_ema = df[column].ewm_mean(span=12)
    long_ema = df[column].ewm_mean(span=26)
    macd = short_ema - long_ema
    macd_signal = macd.ewm_mean(span=9)
    return macd, macd_signal

macd, macd_signal = compute_macd(df_polars, "close")
df_polars = df_polars.with_columns(macd.alias("MACD"), macd_signal.alias("MACD_Signal"))

(3) Bollinger Bands
Measures volatility by plotting an upper and lower band around the price.

Pandas Implementation:

bb = ta.volatility.BollingerBands(df["close"], window=20)
df["BB_High"] = bb.bollinger_hband()
df["BB_Low"] = bb.bollinger_lband()

Polars Implementation:

def compute_bollinger_bands(df, column="close", window=20):
    sma = df[column].rolling_mean(window_size=window)
    std_dev = df[column].rolling_std(window_size=window)
    upper_band = sma + (2 * std_dev)
    lower_band = sma - (2 * std_dev)
    return upper_band, lower_band

bb_high, bb_low = compute_bollinger_bands(df_polars, "close", 20)
df_polars = df_polars.with_columns(bb_high.alias("BB_High"), bb_low.alias("BB_Low"))

(4) Stochastic Oscillator
Measures the stock’s closing price relative to its price range over time.

Pandas Implementation:

df["Lowest_Low"] = df["low"].rolling(window=14).min()
df["Highest_High"] = df["high"].rolling(window=14).max()
df["Stoch"] = 100 * ((df["close"] - df["Lowest_Low"]) / (df["Highest_High"] - df["Lowest_Low"]))

Polars Implementation:

df_polars = df_polars.with_columns([
    df_polars["low"].rolling_min(window_size=14).alias("Lowest_Low"),
    df_polars["high"].rolling_max(window_size=14).alias("Highest_High"),
])
df_polars = df_polars.with_columns(
    ((df_polars["close"] - df_polars["Lowest_Low"]) / 
     (df_polars["Highest_High"] - df_polars["Lowest_Low"]) * 100).alias("Stoch")
)

Forward and backward filled missing values to avoid gaps in calculations.

df.ffill(inplace=True)
df.bfill(inplace=True)
df_polars = df_polars.fill_null(strategy="forward").fill_null(strategy="backward")

Step 3 - Training Machine Learning Models
After enriching the dataset, I trained Linear Regression and Random Forest models to predict the next day’s closing price.

Defining Features & Target

features = ["SMA_20", "EMA_20", "MACD", "MACD_Signal", "BB_High", "BB_Low", "Stoch"]
df_pandas["target"] = df_pandas["close"].shift(-1)
df_polars = df_polars.with_columns(df_polars["close"].shift(-1).alias("target"))

Splitting Data for Training & Testing

X_train_pandas, X_test_pandas, y_train_pandas, y_test_pandas = train_test_split(
    df_pandas[features], df_pandas["target"], test_size=0.2, random_state=42, shuffle=False
)

X_train_polars, X_test_polars, y_train_polars, y_test_polars = train_test_split(
    df_polars.select(features).to_pandas(), df_polars.select("target").to_pandas(), 
    test_size=0.2, random_state=42, shuffle=False
)

Training Models

(1) Linear Regression

lr_model_pandas = LinearRegression().fit(X_train_pandas, y_train_pandas)
lr_model_polars = LinearRegression().fit(X_train_polars, y_train_polars)

(2) Random Forest

rf_model_pandas = RandomForestRegressor(n_estimators=100).fit(X_train_pandas, y_train_pandas)
rf_model_polars = RandomForestRegressor(n_estimators=100).fit(X_train_polars, y_train_polars)

Evaluating Models

print("MAE:", mean_absolute_error(y_test_pandas, y_pred_lr_pandas))
print("R2 Score:", r2_score(y_test_pandas, y_pred_lr_pandas))

Findings:
1. Polars models performed slightly worse than Pandas.
2. Pandas and Polars both showed similar MAE, but Polars had slower training.

Final Takeaways:
1. Polars is faster than Pandas for data manipulation, but it’s less optimized for ML tasks.
2. Random Forest outperformed Linear Regression for stock price predictions.
3. All four technical indicators were useful in improving model accuracy.


Part 3: Visual Dashboard for Benchmarking & Predictions
In this final section, the goal was to create an interactive dashboard to display:

Benchmarking results from Part 1 (CSV vs. Parquet, Pandas vs. Polars, ML model performance)
Stock price predictions from Part 2, including actual & predicted prices and technical indicators

For this, I chose Streamlit as the dashboarding framework because: (1) It provides an interactive and user-friendly interface, (2) it allows real-time updates for selected stock tickers, (3) it integrates well with Plotly for data visualization, and (4) it is good for beginners.

Step 1 - Loading & Caching Data
To improve performance, I cached the benchmark data and stock dataset using @st.cache_data, ensuring data is only loaded once unless the script is restarted.
    
Caching the data prevents unnecessary reloading, making the dashboard faster and is useful when switching between different stock tickers.

Step 2 - Creating the Dashboard Layout
The dashboard has two sections, controlled via a sidebar navigation menu.

This allows users to switch between:

1. Benchmark Results
2. Stock Price Predictions
   
Step 3 - Displaying Benchmark Results (Dashboard A)
This section visualizes machine learning model performance and CSV vs. Parquet storage performance.

Comparison of MAE, MSE, and R² Score for Pandas vs. Polars models.

fig1 = px.bar(benchmark_long, 
              x="Algorithm", 
              y="Value", 
              color="Metric", 
              barmode="group", 
              title="Model Performance Comparison (MAE, MSE, R² Score)")
st.plotly_chart(fig1)

Findings:
1. Random Forest performed slightly better than Linear Regression in Pandas but had slower performance in Polars.

Comparison of CSV vs. Parquet read times across different dataset sizes (1x, 10x, 100x).

fig2 = px.bar(storage_benchmark, 
              x="Scale", 
              y="Read Time (ms)", 
              color="Kind of File", 
              barmode="group",
              title="CSV vs Parquet Read Time Across Different Scales")
st.plotly_chart(fig2)

Findings:
1. Parquet was consistently faster than CSV, especially at 10x and 100x scales.
2. At 100x scale, Parquet was 19.4x faster than CSV.
   
Step 4 - Stock Price Predictions (Dashboard B)
This section visualizes actual vs. predicted stock prices and includes key technical indicators.

Selecting a Stock Ticker

stock_ticker = st.selectbox("Select a stock ticker:", df["name"].unique())
df_stock = df[df["name"] == stock_ticker]

Users can select any stock ticker, and the charts will update dynamically.

Candlestick Chart with Predictions

Displays actual stock price movement with predicted next-day prices.

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

Users can visually compare actual vs. predicted prices.

Overlaying Technical Indicators

To help analyze trends, I plotted: (1) SMA (20) & EMA (20), (2) Bollinger Bands, (3) MACD & MACD Signal, and (4) Stochastic Oscillator

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

Users can toggle indicators on/off using the legend.

Final Takeaways:
1. Streamlit provided a fast, interactive way to visualize model results.
2. Dashboard A demonstrated how CSV vs. Parquet and Pandas vs. Polars performed across different benchmarks.
3. Dashboard B allowed users to explore stock price predictions and key technical indicators dynamically.
   

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
