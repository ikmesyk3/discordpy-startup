# coding: utf-8
  
from discord.ext import commands
import os
import traceback
import discord

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.client()

  
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
@client.event
async def on_join_member(member):
  await member.send('hello,world')
    
    
@bot.command()
async def (client):
  await client.change_presence (activity=game)
  game=discord.game(name(str('Hello,World!')))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
  
bot.run(token)
