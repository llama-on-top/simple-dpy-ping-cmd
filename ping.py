# Imports
import discord
from discord.ext import commands

# Intents + Prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='p!', intents=intents)

# When bot is ready
@bot.event
async def on_ready():
    print(f'Ping command is ready to be used!')


# Ping command
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Bot token
bot.run('your_token')
