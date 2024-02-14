import asyncio
from websockets.server import serve

async def echo(websocket):
    print("Connection opened")
    try:
        async for message in websocket:
            print(message)
            await websocket.send(input("command: "))
    except:
        await websocket.close()
    finally:
        print("Connection closed")
async def main():
    async with serve(echo, "localhost", 5000):
        await asyncio.Future()  # run forever

asyncio.run(main())