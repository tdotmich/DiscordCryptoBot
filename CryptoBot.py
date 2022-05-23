# general imports
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


# Crypto Price Checker imports
import json
import requests


# Bot member interactions
discord.member = True
intents = discord.Intents.all()
intents.members = True

# Get auth token from local .env file
load_dotenv('token.env')

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!', intents=intents)

# Notify when Discord is connected, and list server
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )






@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server')
    await member.send(f'{member} has joined the server')
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome {member.name} to the {GUILD} server!'
    )






@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server')
    await member.send(f"{member} has left the server")




# CRYPTO EVENT HANDLER
@bot.command('server')
async def fetchServerInfo(context):
    guild = context.guild

    await context.send(f'Server Name: {guild.name}')
    await context.send(f'Server Size: {len(guild.members)}')
    await context.send(f'Server Owner: {guild.owner.display_name}')


# CRYPTO COMMANDS BELOW  - actively listen for commands from users and returns the relevant function (prices)

@bot.command('BTC')
async def getCryptoPrice(ctx):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCGBP"
    data = requests.get(key)
    data = data.json()
    response = f"{data['symbol']} price is currently {'£' + data['price']}"
    size = len(response)
    corrected_response = response[:size - 6]
    print(f"{corrected_response}")
    await ctx.send(f"{corrected_response}")


@bot.command('LRC')
async def getCryptoPrice(ctx):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=LRCUSDT"
    data = requests.get(key)
    data = data.json()
    response = f"{data['symbol']} price is currently {'$' + data['price']}"
    size = len(response)
    corrected_response = response[:size - 5]
    print(f"{corrected_response}")
    await ctx.send(f"{corrected_response}")





@bot.command('ETH')
async def getCryptoPrice(ctx):
    key = "https://api.binance.com/api/v3/ticker/price?symbol=ETHGBP"
    data = requests.get(key)
    data = data.json()
    response = f"{data['symbol']} price is currently {'£'+data['price']}"
    size = len(response)
    corrected_response = response[:size -6]
    print(f"{corrected_response}")
    await ctx.send(f"{corrected_response}")

# Always include at the end of the file. Anything below this won't run.
bot.run(TOKEN)





