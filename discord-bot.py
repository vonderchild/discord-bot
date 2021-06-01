import discord
import os
import random

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
insults = []


def get_insult():
    global insults
    f = open('insult.txt', 'r')

    insults = f.readlines()


client = commands.Bot(command_prefix='!', intents=intents)


@client.command(name="abuse")
async def id_(ctx, user: discord.User):
    await ctx.channel.send(f"Kutta {user.mention}")


@client.command(name="chup")
async def id_(ctx, user: discord.User):
    await ctx.channel.send(f"Chup kar kutte {user.mention}")


@client.command(name="gay")
async def id_(ctx):
    user = "<@510833310339956752>"
    await ctx.channel.send(f"BIGGEST GAY OF THE YEAR: {user}")


@client.command(name="insult")
async def id_(ctx, user: discord.User):
    if ctx.message.author.id == "490516690518540299" or ctx.message.author.id == "510833310339956752":
        insult = random.choice(insults)
        await ctx.channel.send(f"{user.mention}, {insult}")
    else:
        await ctx.channel.send(f"{user.mention}, you are not allowed to insult, stfu.")


@client.event
async def on_member_join(member):
    channel = client.get_channel(833117650317869061)
    embed = discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


get_insult()
token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)
