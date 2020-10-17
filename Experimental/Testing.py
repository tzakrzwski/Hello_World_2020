#Just some test code for connecting to Discord bot
import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to Discord!')
    #f'{client.user} is connected to the following guild:\n'
    #print(f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'Beeg':
        await message.channel.send('Do you guys have the Big Yoshi?')

client.run(TOKEN)