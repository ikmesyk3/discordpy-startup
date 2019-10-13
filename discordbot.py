  
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
    await change_presence(status=discord.Status.idle,activity=game)
    game = discord.game(str('Hello,World!'))
  
    class discord.game(name(str('Hello,World!')



bot.run(token)
