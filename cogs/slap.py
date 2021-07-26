import discord
from discord.ext import commands
import PIL.Image
from io import BytesIO


class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(help='''Slap someone you love the most''')
    async def slap(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("Pls check the command **n13 help image**")

        else:
            slapy = PIL.Image.open("data/slap.jpg")
            authorpic = ctx.author.avatar_url_as(size=128)
            userpic = user.avatar_url_as(size=128)
            data1 = BytesIO(await authorpic.read())
            data2 = BytesIO(await userpic.read())
            pfp1 = PIL.Image.open(data1)
            pfp2 = PIL.Image.open(data2)

            pfp1 = pfp1.resize((84, 77))
            pfp2 = pfp2.resize((95, 87))
            slapy.paste(pfp2, (15, 53))
            slapy.paste(pfp1, (168, 35))
            slapy.save("profile.jpg")
            await ctx.send(file=discord.File("profile.jpg"))


def setup(client):
    client.add_cog(Image(client))
