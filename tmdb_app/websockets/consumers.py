from channels.consumer import SyncConsumer
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print("websocket Connected....", event)
        self.send({
            'type' : 'websocket.accept'
        })

    def websocket_receive(self, event):
        print("Websocket Received...")
        print("Message is ", event['text'])
        self.send({
            'type': "websocket.send",
            "text": "msg from server to the client"   # this will be sent to client...
            })


    def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("websocket Connected....", event)
        await self.send({
            'type' : 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print("Websocket Received...")
        print("Message is ", event['text'])
        

        json_obj = {
            'field_1': 1,
            'field_2': 2,
            'id': 4,
            'fname': "Balbir",
            "lname":"Yadav"
        }

        await self.send({
            "type": "websocket.send",
            "text": json.dumps(json_obj)
        })

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...", event)
        raise StopConsumer()

    