from telethon import TelegramClient, events
import asyncio
import re 

api_id = 9623699
api_hash = 'fe0f2a7acd200c8fa21a0aaa59b59ae2'

my_channel_id = -1001765381029
channels = [-1001355465930, -1001370708606, -1001201979273, -1001286238248, -1001790607385, -1001728917276, -1001366535587, -1001470142620, -1001301799448, -1001245637221, -1001344433701, -1001588299908, -1001525746512, -1001199914162, -1001328165190]

client = TelegramClient('myGrab', api_id, api_hash)
print("buma topcg")

@client.on(events.NewMessage(chats=channels))
async def my_event_handler(event): 
  if event.message:
    match = re.findall(r"(?<!\/)\b(?=[0-9]*[A-Z]){8}[A-Z0-9]{8}+\b", event.message.message)
    if not match:
      return
    await client.send_message(my_channel_id, match[0])
client.start()
client.run_until_disconnected()