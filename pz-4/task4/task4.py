from utils import get_currency_rate
import decimal

cur_name = input('Enter cur name: ')
price, date = get_currency_rate(cur_name)
if price != 'None':
    print(f'{cur_name} {price:.2f}, {date}')
else:
    print('None')