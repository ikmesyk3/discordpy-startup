  
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

  
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    await client.change_presence(activity=discord.Game(name='my game'))

# or, for watching:
activity = discord.Activity(name='my activity', type=discord.ActivityType.watching)
await client.change_presence(activity=activity)


bot.run(token)
