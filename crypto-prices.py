#!/usr/bin/env python

from sys import argv
from pathlib import Path
import requests
import subprocess
import time


def main():

	file = Path(argv[1])
	output = Path(argv[2])
	account = input('Name of the account:\n')

	all_coins = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false').json()
	all_coins.extend(requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=2&sparkline=false').json())

	ledger_command = f'ledger -f {file} commodities {account}'
	commodities = subprocess.run(ledger_command.split(), stdout=subprocess.PIPE)
	commodities = commodities.stdout.decode().lower().split()
	if 'usd' in commodities:
		commodities.remove('usd')
	if 'pen' in commodities:
		commodities.remove('pen')

	f = open(output, 'a') if output.exists() else open(output, 'w')
	for coin in all_coins:
		if coin['symbol'] in commodities:
			f.write(f"P {time.strftime('%Y-%m-%d %H:%M:%S')} {coin['symbol'].upper()} {coin['current_price']} USD\n")
	f.close()

	print(f'Prices written to {output}')


if __name__ == '__main__':
	main()
