import discord
from discord.ext import commands
import json
import random
import os
import termcolor
import youtube_dl
import ffmpeg
import time


def get_jokes():
    with open("data/jokes.json", 'r', encoding='utf-8') as f:
        alljokes = json.load(f)
    random_cat = random.choice(list(alljokes.keys()))
    insult = random.choice(list(alljokes[random_cat]))
    return insult


def get_scold():
    with open("data/scold.json", 'r', encoding='utf-8') as j:
        allscold = json.load(j)
    random_scold = random.choice(list(allscold.keys()))
    scold = random.choice(list(allscold[random_scold]))
    return scold


class NSFW(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['roast'], help='''Sick of someone? Easy! Just roast them!''')
    async def insult(self, ctx, member: discord.Member = None):
        if member is not None:
            insult = get_jokes()
            if insult[0:10] == "Yo mama's":
                result = f'{member.mention} {insult[9:]}'
            else:
                result = f'{member.mention} {insult[7:]}'
            await ctx.send(result)
        else:
            await ctx.send(f'{ctx.author.mention} Please check the **n13 help nsfw** or suck my dick')

    @commands.command(help="Bot will join a voice chat and scold you")
    async def scoldme(self, ctx):
        # checking whether author in vc or not

        if not ctx.author.voice or not ctx.author.voice.channel:
            await ctx.send(f'{ctx.author.mention} join vc noob')
        else:
            destination = ctx.author.voice.channel
            await destination.connect()
            FFMPEG_OPTIONS = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn',
            }
            YDL_OPTIONS = {'format': 'bestaudio'}
            vc = ctx.voice_client

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                url = get_scold()
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                sleep_time = info['duration']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS
                                                                  )
                vc.play(source)

            time.sleep(sleep_time)
            await ctx.voice_client.disconnect()


def setup(client):
    client.add_cog(NSFW(client))
