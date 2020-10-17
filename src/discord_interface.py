import random
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Variables
is_game = False #Tells if there is currently a game going on

#Set-up
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



#Start-Game function
#Asks sever members to dm the bot if they want to join
#Has min, max number of players
@client.command(name='begin')
@commands.has_role('Admin')
async def begin(ctx, min=8, max=20):
    print('hello')
    #if is_game and not ctx.guild: #Check if already in a game AND in a server
       # return
    print(ctx.guild)

        


'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    print(message.channel.__dir__())
    if message.content == 'Beeg':
        await message.channel.send('Do you guys have the Big Yoshi?')
'''
client.run(TOKEN)
