import discord
from discord import app_commands,ui
from datetime import time, timezone, timedelta
from discord.ext import tasks 
import asyncio
import os
from keep_alive import keep_alive
from dotenv import load_dotenv

CHANNEL_ID = os.getenv("CHANNEL_ID")
SERVER_ID = os.getenv("SERVER_ID")

client = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(client)

JST = timezone(timedelta(hours=+9), "JST")

times = [
    time(hour=8, minute=30, tzinfo=JST),
    time(hour=20, minute=30, tzinfo=JST)
]

@tasks.loop(time=times)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('ﾊﾁｼﾞﾊｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧｧﾝﾝ!!!!!!!!!!!!')
    await asyncio.sleep(60)

@client.event
async def on_ready():
    print('on ready')
    await tree.sync(guild=discord.Object(id={SERVER_ID}))
    loop.start()


TOKEN = os.getenv("DISCORD_TOKEN")

keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill")
