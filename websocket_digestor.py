#!/usr/bin/env python
import asyncio
import websockets
import sys, getopt
import websocket
import thread
import time
import json
import csv
import logging
import pathlib
import ssl

SOCKET_URL = "wss://price-azu-01.vndirect.com.vn/realtime/websocket"
EXPORT_RAW_DATA = '/data/raw/stocks.csv'


# GENERATE MESSAGE FOLLOW FORMAT
def message_formater(message_name, codes):
    custom_message_json = {type: 'registConsumer', data: {
        params: {
            name: message_name, codes: codes
            }}}

    custom_message_json


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())


