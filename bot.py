import os
from telethon import TelegramClient, events

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient("broadcast_bot", api_id, api_hash)

@client.on(events.NewMessage(pattern=r"^/start"))
async def handler(event):
    await event.respond("Bot sudah aktif di Railway!")

print("Bot berjalan...")
client.start()
client.run_until_disconnected()
