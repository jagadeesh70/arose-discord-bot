import discord
from discord.ext import commands


class Interact(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["helo"], help='''Arose bot will respond you :)''')
    async def hello(self, ctx):
        await ctx.send(f'Hi {ctx.author.mention}')

    @commands.command(help='''Bot will say its name''')
    async def name(self, ctx):
        await ctx.send(f'Yeah they call me **Arose xD**')

    @commands.command(help='''Reveal of bot parents''')
    async def parents(self, ctx):
        await ctx.send(f'Songoku and Vegeta are my Parents :) xD')

    @commands.command(aliases=["win"], help='''Noob will be revealed xD''')
    async def whoisnoob(self, ctx):
        await ctx.send(f'I am the biggest brain dead noob xD')


def setup(client):
    client.add_cog(Interact(client))
