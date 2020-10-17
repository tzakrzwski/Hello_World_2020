import random
import discord
import asyncio
from discord.ext import commands
import os
from dotenv import load_dotenv

#Constant
name_list = ('fred', 'bob', 'will', 'steve', 'dave', 'jim')

#Variables
is_game = False #Tells if there is currently a game going on
is_joining = False #Tells if people can join the game
player_list = [] #List of all the players and bots on the game
add_message = None #Message that react to to be added to the game
game_channel = None #Where the game takes place

#Player / Bot Class
class Player():

    def __init__(self, user=None):
        self.input = None #Store the value from input
        #Init stuff for human player
        self.user = user
        if user:
            self.name = user.name
        #Init stuff for computer player
        else:
            self.name = random.choice(name_list)
            self.channel = None #System knows to choice random thing
    
    async def send_message(self, text):
        await self.channel.send(text)
    
    async def input(self, prompt): #USE self.input to access data
        def check(message): #Check to see if person who started game canceled
            #input parsing
            try:
                self.input = int(message.content)
                return True
            except:
                self.input = -1
                return False
        try: #Wait for the host to end stop the game before starting
            await client.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            self.send_message("Timeouted")   

    async def create_channel(self):
        if self.user:
            #Create / Get Dm channel
            if not self.user.dm_channel:
                await self.user.create_dm()
            self.channel = self.user.dm_channel

async def send_message(text):
    global game_channel
    await game_channel.send(text)

#Set-up
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='!', intents=discord.Intents(reactions=True, messages=True, members=True, guilds=True))
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')



#Start-Game function
#Asks sever members to dm the bot if they want to join
#Has min, max number of players
@client.command(name='begin')
@commands.has_role('Admin')
async def begin(ctx, minn=8, maxn=20):
    global is_game, add_message, is_joining, player_list, game_channel
    game_channel = ctx.channel
    if is_game: #Check if already in a game
       return
    #Set game starting variables
    is_game = True
    is_joining = True
    #Ask players to send in chat if they are going to join
    add_message = await channel.send('Starting '+str(maxn)+' Person Game: \n'+'React to this post to join')
    def check(message): #Check to see if person who started game canceled
        return message.author == ctx.author
    try: #Wait for the host to end stop the game before starting
        await client.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        #Reset the joining variables
        is_joining = False
        add_message = None
        #Add aditional bot players (if need) to make the minimum
        while len(player_list) < minn:
            player_list.append(Player())
        #Send out directions / information
        await channel.send("Ready to Begin "+str(len(player_list))+" Player Game with:")
        x = ''
        for player in player_list:
            x += player.name + '\n'
        await channel.send(x)
        await channel.send("You will be DMed instructions on how to begin")
    else:
        await channel.send('Host canceled game')
        is_game = False
        return

@client.event
async def on_reaction_add(reaction, user):
    global player_list
    #Add only if game is allowing players and the message reacted to is correct
    if not is_joining and reaction.message != add_message:
        return
    else:
        x = Player(user)
        await x.create_channel()
        await x.send_message("Welcome to the Game")
        player_list.append(x)
        print("Got one")



'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Beeg':
        await message.channel.send('Do you guys have the Big Yoshi?')
'''
client.run(TOKEN)
