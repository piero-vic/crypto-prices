# `crypto-prices.py`
A script that requests crypto prices from CoinGecko and writes them to a file in the format required by the Ledger CLI price history.

In order to know which crypto assets you hold, the script runs a ledger command that outputs a list of commodities. It also excludes fiat currencies (At the moment, this feature is hard-coded and only filters the ones that I use). Then it will search for matches among the top 500 cryptocurrencies (this is also hard-coded), get the prices, format the information, and write it to the output file.

## Installation
Clone the repository
```sh
git clone https://github.com/piero-vic/crypto-prices
```

## Usage
Run script
```sh
python crypto-prices.py LEDGER_FILE OUTPUT_FILE
```
The script will prompt you for an account
```sh
Name of the account:
Assets:Crypto
```
Confirmation
```sh
Prices written to OUTPUT_FILE
```
