import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


#Set-up
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(message.channel.__dir__())
    if message.content == 'Beeg':
        await message.channel.send('Do you guys have the Big Yoshi?')

client.run(TOKEN)
