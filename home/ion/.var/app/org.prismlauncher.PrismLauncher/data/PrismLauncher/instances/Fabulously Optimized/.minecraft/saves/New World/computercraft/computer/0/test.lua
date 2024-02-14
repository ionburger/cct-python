local ws = assert(http.websocket("ws://127.0.0.1:5000"))
ws.send("bacon") -- Send a message
ws.send("pork")
print(ws.receive())
print(ws.receive()) -- And receive the reply
ws.close()
