import asyncio
import json
import logging

import websockets

from services.system import gather_info


# Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '[%(asctime)s] - %(funcName)s: %(message)s',
    '%H:%M:%S'
)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
logger.addHandler(ch)


async def server(websocket, path):
    message = json.loads(await websocket.recv())
    logger.info(message)

    if message['type'] == 'update':
        await websocket.send(json.dumps(await gather_info()))


start_server = websockets.serve(server, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
