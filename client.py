import asyncio
import json
import logging

import websockets


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


async def hello():
    message = dict()
    async with websockets.connect('ws://localhost:8765') as websocket:
        message['type'] = 'update'

        await websocket.send(json.dumps(message))

        message = json.loads(await websocket.recv())
        logger.info(message)

asyncio.get_event_loop().run_until_complete(hello())
