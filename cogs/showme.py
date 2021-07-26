from utils import imagedownload
from io import BytesIO
import PIL
from discord.ext import commands
import discord
import sys
import os
sys.path.append(os.path.realpath('..'))


class Showme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='''Bot will send the picture you searched for xD''')
    async def showme(self,  ctx, name):
        imagedownload.main(name, 1)
        await ctx.send(file=discord.File(f'Images/{name}1.jpg'))
        os.remove(f'Images/{name}1.jpg')

    @showme.error
    async def showme_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('''Name something that you want me to show
`n13 showme (name)`
eg: n13 showme cat''')


def setup(client):
    client.add_cog(Showme(client))
