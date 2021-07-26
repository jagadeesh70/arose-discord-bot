import discord
from discord.ext import commands
from discord import Forbidden
import json


async def send_embed(ctx, embed):

    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue? :slight_smile: ", embed=embed)


with open("data/help.json", 'r', encoding='utf-8') as f:
    allhelp = json.load(f)


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    # @commands.client_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *input_):
        """Shows all modules of that client"""
        prefix = "n13 "
        version = 1.0

        owner = 573755940747345920
        owner_name = "B1nl4den#0001"
        # to sanatize help
        cogname = ''
        for cog in self.client.cogs:
            for command in self.client.get_cog(cog).get_commands():
                cogname += f'{command.name} '

        name_cog = cogname.split(" ")

        if not input_:
            try:
                owner = ctx.guild.get_member(owner).mention

            except AttributeError as e:
                owner = owner

            emb = discord.Embed(title='Arose Bot Command List',
                                color=discord.Color.green())

            cogs_desc = ''
            for cog in self.client.cogs:
                cogs_desc += f'`{cog}` {self.client.cogs[cog].__doc__}\n'

            emb.add_field(name=':camera_with_flash:  Image',
                          value="`n13 help image`")
            emb.add_field(name=':musical_note:  Music',
                          value="`n13 help music`")
            emb.add_field(name=":broom:  Clear", value="`n13 help clear`")
            emb.add_field(name=":cop:  Moderation",
                          value="`n13 help moderation`")

            emb.add_field(name=":speaking_head:  Interact",
                          value="`n13 help interact`")
            emb.add_field(name=":question:  Whoisur",
                          value="`n13 help whoisyour`")
            emb.add_field(name=":mag:  Showme", value="`n13 help showme`")
            emb.add_field(name=":underage:  NSFW", value="`n13 help nsfw`\n")

            emb.add_field(
                name="About", value=f"The Bot is developed by B1nl4den#0001\n", inline=False)
            emb.set_footer(text=f"client is running {version}")

        elif len(input_) == 1:

            rel = input_[0].lower()

            if (rel in name_cog):
                descrip = allhelp[rel]
                emb = discord.Embed(
                    title=f'{rel} - Command', description=f'{descrip}', color=discord.Color.blurple())

            elif(rel not in name_cog):
                for cog in self.client.cogs:

                    if cog.lower() == input_[0].lower():

                        emb = discord.Embed(title=f'{cog} - Commands', description=self.client.cogs[cog].__doc__,
                                            color=discord.Color.blue())

                        for command in self.client.get_cog(cog).get_commands():
                            if not command.hidden:
                                emb.add_field(
                                    name=f"`{command.name}`", value=f'{command.help}', inline=False)
                        break

            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}` before :scream:",
                                    color=discord.Color.orange())

        elif len(input_) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once :sweat_smile:",
                                color=discord.Color.orange())

        await send_embed(ctx, emb)


def setup(client):
    client.add_cog(Help(client))
