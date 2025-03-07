# Assignment Title

Assignment 1: Stock Price Prediction (S&P 500)
presented by Juan Carlos Katigbak 300366535 to Nikhil Bhardwaj CSIS4260 Special Topics in Data Analytics Section 001

## About the Assignment

The purpose of this assignment is to combine research, benchmarking and coding using the provided time-series dataset of stock prices for S&P 500 companies. The assignment is divided into three parts, each with its own research and coding components.

Objectives
Part 1: Storing and retrieving data using csv vs. parquet with compression scales of 1x, 10x, and 100x.
Part 2: Manipulating, analyzing data and building models using dataframe libraries Pandas vs. Polars with 4 technical indicators and 2 algorithms to train and test data using 80-20 split for back testing.
Part 3: Creating a visual dashboard for the results using a dashboard library with 2 dashboards where 1 displays benchmark results at all scales and the other 1 displays price prediction models for all companies.

### Prerequisites

- Install Python (>=3.8)
- Install Jupyter Notebook

## Assignment Structure

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

### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of Katigbak_300366535_Assignment1 folder

If getting it from OneDrive:
Just simply download the Katigbak_300366535_Assignment1 folder and open folder which will show files all_stocks_5yr.csv, README.md, part1.ipynb, part2.ipynb, and part3.py as well as "just-in-case" files all_stocks_5yr.parquet, all_stocks_5yr_10x.csv, all_stocks_5yr_10x.parquet, all_stocks_5yr_100x.csv, all_stocks_5yr_100x.parquet, all_stocks_5yr_enhanced_pandas.csv, and all_stocks_5yr_enhanced_polars.csv just in case there are errors like the Jupyter Notebook looking for these files.

If getting it from Github:
Extract Katigbak_300366535_Assignment1.zip and then extract all_stocks_5yr.csv.zip to get file extract all_stocks_5yr.csv

* Since Katigbak_300366535_Assignment1 downloaded as a ZIP, extract Katigbak_300366535_Assignment1 folder first and extract all_stocks_5yr.csv.zip making sure that the file all_stocks_5yr.csv has been brought out of its folder and placed in Katigbak_300366535_Assignment1 folder together with files README.md, part1.ipynb, part2.ipynb, and part3.py.

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
pip install pandas polars numpy scikit-learn matplotlib seaborn ta streamlit pyarrow

For Jupyter Notebook:
!pip install pandas polars numpy scikit-learn matplotlib seaborn ta streamlit pyarrow

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

using either macOS/Linux's Terminal or Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\Katigbak_300366535_Assignment1
(e.g. cd OneDrive\Desktop\Katigbak_300366535_Assignment1) #since Katigbak_300366535_Assignment1 is the folder with the file

streamlit run part3.py

this will open http://localhost:8501/ in your browser

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)
