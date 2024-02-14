local conf = {}
for i in io.lines("config.conf") do table.insert(conf,i) end
ws = assert(http.websocket(conf[1]),"fuck")
while true do
    ws.send("ready")
    rec = ws.receive()
    print(rec)
    run = load(rec)
    run()
end
