from binance.client import Client
from binance.enums import *
import config

client = Client(config.API_KEY, config.SECRET_KEY, tld='us')
client.API_URL = 'https://testnet.binance.vision/api'
info = client.get_account()
bal = info['balances']
for b in bal:
    if float(b['free']) > 0:
        print(b)

order = client.create_order(
    symbol='BTCUSDT',
    side=SIDE_SELL,
    type=ORDER_TYPE_MARKET,
    quantity=0.001
)
print('********************************')
info = client.get_account()
bal = info['balances']
for b in bal:
    if float(b['free']) > 0:
        print(b)

