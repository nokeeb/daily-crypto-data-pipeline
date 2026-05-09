# Crypto Data Pipeline

## General
This project fetches cryptocurrency data from CoinGecko API, processes it, and generates a daily report.

## Features
- API Data extraction
- Data cleaning
- Writing data into CSV
- Data analysis
- Report generation

## Tech stack
-Python

## How to Run

Clone the repository:

```bash
git clone https://github.com/nokeeb/daily-crypto-data-pipeline.git
```

Navigate into the project folder:

```bash
cd crypto-data-pipeline
```

Run the pipeline:

```bash
python main.py
```



## Output example (report.txt content)
```text
Crypto Report - 2026-05-09
Average Price: 4244.997577750001
Top Market Cap: Bitcoin
Lowest Volume: LEO Token
Top 3 by Ratio:
1.LEO Token - 1.9455509660829384e-05
2.Monero - 3.060533700848879e-06
3.Bitcoin - 2.875325779057809e-06
```


## Project Structure

```text
daily-crypto-data-pipeline/
│
├── .gitignore
├── README.md
├── main.py
│
└── pipeline/
    ├── extract.py
    ├── transform.py
    ├── load.py
    ├── analyze.py
    └── report.py
```
## Mission - Learning Python
-programming
-variables
-loops
-functions
-data types
-strings
-working with files (.CSV, .TXT)
-using Web services (HTTP requests, API calls, parsing JSON etc..)

## Author

GitHub: https://github.com/nokeeb

## Feedback is appreciated



