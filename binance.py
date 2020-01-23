from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from pandas.io.json import json_normalize

client = Client('api-key', 'api-secret')
tickers = client.get_all_tickers()


df = pd.DataFrame([])
count = 0
bm = None

### Multiplex socket

# Save incoming data
def process_message(msg):
    global count, df, bm
    print("stream: {} data: {}".format(msg['stream'], msg['data']))
    # append message to array

    df = df.append(msg, ignore_index=True)

    count += 1

    with open('klinesmultiplex_socket.csv', 'a') as f:
        df.to_csv(f, header=False)
    #df = pd.DataFrame(df)
    #df.to_csv('test.csv')


def initiate():
    global bm
    # Connect to client
    client = Client('api-key', 'api-secret')

    # Setup Socket
    bm = BinanceSocketManager(client)

    # then start the socket manager
    conn_key = bm.start_multiplex_socket(['bnbbtc@kline_1m', 'neobtc@kline_1m'], process_message)

    # start the socket
    bm.start()


initiate()