import discord
from discord.ext import commands
import json


with open("data/question.json", 'r', encoding='utf-8') as f:
    allquestions = json.load(f)


class whoisyour(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['wiu'], help='''**Usage**:
                                                `n13 whoisur (question) eg:god,friend`
                                                **Description**:
                                                Bot will reply:)''')
    async def whoisur(self, ctx, question):
        a = question.lower()
        if(a == ""):
            await ctx.send(f'Use **n13 help whoisyour** for syntax')

        elif(question in allquestions):
            await ctx.send(f'{allquestions[question]}')

        else:
            await ctx.send(f'who the fck you are to ask me questions')

    @whoisur.error
    async def wiu_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Use **n13 help whoisyour** for syntax')


def setup(client):
    client.add_cog(whoisyour(client))
