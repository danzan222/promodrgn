from telethon import TelegramClient, events
import asyncio
import re 

api_id = 9623699
api_hash = 'fe0f2a7acd200c8fa21a0aaa59b59ae2'

my_channel_id = -1001700053739
channels = [-1001679245835]

client = TelegramClient('myGrab', api_id, api_hash)
print("buma top")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event):
	if event.message:
		await client.send_message(my_channel_id, event.message)

client.start()
client.run_until_disconnected()
