#!/usr/bin/env python
import asyncio
import websockets
import sys, getopt
import websocket
from threading import Thread
import time
import json
import csv
SOCKET_URL = "wss://price-azu-01.vndirect.com.vn/realtime/websocket"
EXPORT_RAW_DATA = '/data/raw/batch1.csv'


try:
    opts, args = getopt.getopt(sys.argv[1:], 'p:', ['parity='])
except getopt.GetoptError:
    sys.exit(2)

# for opt, arg in opts:
#     if opt in ('-p', '--paridade'):
#         parity = arg
#     else:
#         sys.exit(2)

data = {'command':'subscribe','channel':''+parity+''}

def on_message(ws, message):
    # print(message)
    columns = ['e', 'E', 's', 'k'] 
    out = csv. DictWriter(open(EXPORT_RAW_DATA, 'wb'), columns)
    # CSV WRITER
    with open(EXPORT_RAW_DATA, "w") as output_file:
        output_file.write(message + "\n")

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    print("ONOPEN")
    def run(*args):
        ws.send(json.dumps(data))
        while True:
            time.sleep(1)
        ws.close()
        print("thread terminating...")
    Thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET_URL,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

# async def digest():
#     uri = SOCKET_URL
#     async with websockets.connect(uri) as websocket:
#         # LISTENING
#         await websocket.recv()
# asyncio.get_event_loop().run_until_complete(hello())