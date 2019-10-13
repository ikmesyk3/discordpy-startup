# coding: utf-8
  
from discord.ext import commands
import os
import traceback
client = discord.Client()


bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

  
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def start(client):
  await client.change_presence (activity=game)
  game=discord.game(name(str('Hello,World!')))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

bot.run(token)
