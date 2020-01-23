const WebSocket = require('ws')

// var WebSocketServer = require('websocket').server;
// var WebSocketClient = require('websocket').client;
// var WebSocketFrame  = require('websocket').frame;
// var WebSocketRouter = require('websocket').router;
// var W3CWebSocket = require('websocket').w3cwebsocket;

const url = "wss://price-azu-01.vndirect.com.vn/realtime/websocket"
const connection = new WebSocket(url)

function sleep(millis) {
  return new Promise(resolve => setTimeout(resolve, millis));
}

async function setInterval(){
  connection.send('ping');
  await sleep(20000);
  connection.send('ping');
}

function consume(message_name, codes) {
  connection.send(JSON.stringify(
    {type: 'registConsumer', data:{
       params: {
         name: message_name, codes: codes
        }
      } 
    }
    ));
  }

connection.onopen = () => {
  console.log("[open] Connection established");
  console.log("Sending to server");
}

connection.onerror = (error) => {
  console.log(`WebSocket error: ${error}`)
}

connection.onmessage = (e) => {
  setInterval();
  console.log(e.data)
  // console.log(e)
}