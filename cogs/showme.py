from utils import imagedownload
from io import BytesIO
import PIL
from discord.ext import commands
import discord
import sys
import os
sys.path.append(os.path.realpath('..'))

with open("data/names/names.txt", 'r') as f:
    names = [line.rstrip() for line in f]

arose = ['n13', 'daddy', 'arose', 'arose_dominic', 'baiter_daddy']
den = ['den', 'denmaster', 'denesh']
varshith = ['max', 'varshith', 'varshit', 'husky_max']
ranjith = ['ranjith', 'hellboy', 'rk']
harith = ['harith', 'songoku', 'capsule_govindan']
binladen = ['jagadeesh', 'binladen']


class Showme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='''Bot will send the picture you searched for xD''')
    async def showme(self,  ctx, name):
        all_names = names
        username = name.lower()
        img = PIL.Image.open(
            "data/ranjith/img1.png")

        if username in all_names:
            if username in varshith:
                await ctx.send(file=discord.File("data/varshit/img1.png"))
            elif username in arose:
                await ctx.send(file=discord.File("data/arose/img1.png"))
            elif username in den:
                await ctx.send(file=discord.File('data/den/img1.jpeg'))
            elif username in ranjith:
                await ctx.send(file=discord.File(
                    'data/ranjith/img1.png'))
            elif username in harith:
                await ctx.send(file=discord.File("dataharith/IMG1.JPG"))
            elif username in binladen:
                await ctx.send(file=discord.File("data/binladen/img1.jpg"))

        else:
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
