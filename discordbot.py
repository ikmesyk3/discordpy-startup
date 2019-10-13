# coding: utf-8
  
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

class discord.game(name(str('Hello,World!')))

  
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@bot.command()
async def start(client):
  await client.change_presence (activity=game)
  

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

bot.run(token)
