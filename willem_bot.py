import discord
from discord.ext import commands
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(name='roles')
@commands.has_any_role('Suicide Squad')
async def get_roles(ctx):
    server_roles = ctx.guild.roles
    await ctx.channel.send(server_roles)


@client.command()
async def say(ctx, arg):
    await ctx.send(arg)

token = input("Insert token: ")
client.run(token)