#!/usr/bin/env python
import asyncio
import websockets
import sys, getopt
import thread
import time
import json
import csv
import logging
import pathlib
import ssl
import time

SOCKET_URL = "wss://price-azu-01.vndirect.com.vn/realtime/websocket"
EXPORT_RAW_DATA = '/data/raw/stocks.txt'
VN30F2002_DATA = '/data/raw/VN30F2002.txt'
VCB_DATA = '/data/raw/VCB_DATA.txt'
VIC_DATA = '/data/raw/VIC_DATA.txt'

# GENERATE MESSAGE FOLLOW FORMAT
def message_formater(type, message_name, codes):
    custom_message_json = {"type": type, data: {
        "params": {
            "name": message_name, "codes": codes
            }}}
    custom_message_str = json.dumps(custom_message_json)
    return custom_message_str


async def vndirect():
    async with websockets.connect(SOCKET_URL) as websocket:
        # VN30F2002_DATA
        devi_1 = message_formater("registConsumer", "DERIVATIVE_OPT" , "VN30F2002")
        # VCB_DATA
        vcb_stock = message_formater("registConsumer","STOCK" , "VCB" )
        # VIC_DATA
        vic_stock = message_formater("registConsumer","STOCK" ,"VIC")

        # data_raw = []

        loop_count = 100

        while loop_count > 0:
            for index in [devi_1, vcb_stock, vic_stock]:
                await websocket.send(index))
                row  = await websocket.recv()
                # WRITE TO CSV
                with open(EXPORT_RAW_DATA, "w") as output_file:
                    output_file.write(message + "\n")
                    json.dump(row, outfile)
            # WAIT 20 SECONDS
            time.sleep(20)
            loop_count -= 1
        else:
            # VN30F2002_DATA
            devi_stop = message_formater("stopConsume", "DERIVATIVE_OPT" , "VN30F2002")
            # VCB_DATA
            vcb_stop = message_formater("stopConsume","STOCK" , "VCB" )
            # VIC_DATA
            vic_stop = message_formater("stopConsume","STOCK" ,"VIC")
            for index in [devi_stop, vcb_stop, vic_stop]:
                await websocket.send(index))

asyncio.get_event_loop().run_until_complete(vndirect())


