import asyncio
from websockets.server import serve

async def echo(websocket):
async def main():
    async with serve(echo, "localhost", 5000):
        await asyncio.Future()  # run forever

asyncio.run(main())