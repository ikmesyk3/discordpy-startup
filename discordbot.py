# coding: utf-8
  
from discord.ext import commands
import os
import traceback

import discord

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')
            
            
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

@bot.command()
async def on_member_join(member):
  await member.send('いらっしゃいませ')
  CHANNEL_ID = 631867807264538624

bot.run(token)
