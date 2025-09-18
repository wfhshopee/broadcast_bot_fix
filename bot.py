from telethon import TelegramClient
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")  # masukkan bot token di env variable

client = TelegramClient('bot_session', api_id, api_hash)

client.start(bot_token=bot_token)  # start menggunakan token bot langsung

print("Bot berjalan...")
