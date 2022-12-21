from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json
from time import sleep
import asyncio


class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("websocket Connected....", event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Websocket Received...")
        print("Message is ", event['text'])
        for i in range(50):
            sleep(0.5)
            self.send({
                'type': "websocket.send",
                # this will be sent to client...
                "text": str(i)+". msg from server to the client"
            })

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("websocket Connected....", event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Websocket Received...")
        print("Message is ", event['text'])

        # json_obj = {
        #     'field_1': 1,
        #     'field_2': 2,
        #     'id': 4,
        #     'fname': "Balbir",
        #     "lname": "Yadav"
        # }

        # await self.send({
        #     "type": "websocket.send",
        #     "text": json.dumps(json_obj)
        # })

        for i in range(50):
            await asyncio.sleep(0.5)
            await self.send({
                'type': "websocket.send",
                # this will be sent to client...
                "text": str(i)+". msg from server to the client"
            })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()
