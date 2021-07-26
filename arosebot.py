import discord
from discord.ext import commands
import os
import sys
from settings.global_var import Token

client = commands.Bot(command_prefix='n13 ')


@client.remove_command("help")
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f'n13 help', type=2))
    print("Bot is ready")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


@client.command()
async def invite(ctx):
    emb = discord.Embed(
        title=f'Arose bot Invitation', description=f'[Here](https://discord.com/api/oauth2/authorize?client_id=852940002257666079&permissions=1912008311&scope=bot)', color=discord.Color.blurple())
    await ctx.send(embed=emb)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title=f"Error!!!", description=f"Command not found.", color=ctx.author.color)
        await ctx.send(embed=em)
    print(error)

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(Token)
