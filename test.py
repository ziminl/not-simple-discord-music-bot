


import nextcord
from nextcord.ext import commands


token = ''



intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents = intents, description='4test')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(token)


