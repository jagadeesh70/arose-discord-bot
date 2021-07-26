import discord
from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(help='''Deletes the amount of meassage you specify''')
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command(aliases=['clear-all'], help='''Deletes 1e7 amount of meassages''')
    @commands.has_permissions(administrator=True)
    async def clearall(self, ctx, amount=10000000):
        await ctx.send("Deleting....")
        await ctx.channel.purge(limit=amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('You dont have permission to run this command')


def setup(client):
    client.add_cog(Clear(client))
