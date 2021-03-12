from utils import get_currency_rate
import sys

currency_list = []
currency_list.extend(sys.argv[1:])
for currency in currency_list:
    price, date = get_currency_rate(currency)
    print(f'{currency} {price:.2f}, {date}')