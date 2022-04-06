from telethon import TelegramClient, events
import asyncio
import re 

api_id = 9623699
api_hash = 'fe0f2a7acd200c8fa21a0aaa59b59ae2'

my_channel_id = -1001765381029
channels = [-1001566434690, -1001728917276]

client = TelegramClient('myGrab', api_id, api_hash)
print("buma top")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event): 
  if event.message:
    match = re.findall(r"(?<!\/)\b(?=[0-9]*[A-Z*_])[A-Z0-9_]+\b", event.message.message)
    if not match:
      return
    await client.send_message(my_channel_id, match[0])
client.start()
client.run_until_disconnected()