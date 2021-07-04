import discord
import os
import random
import time
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.members = True
insults = []
quotes = []
counter = 2


def get():
    global insults, quotes

    f = open('insult.txt', 'r')
    insults = f.readlines()
    f.close()

    f = open('quotes.txt', 'r')
    quotes = f.readlines()
    f.close()


client = commands.Bot(command_prefix='!', intents=intents)


@client.command(name="abuse")
async def id_(ctx, user: discord.User):
    await ctx.channel.send(f"Kutta {user.mention}")


@client.command(name="chup")
async def id_(ctx, user: discord.User):
    await ctx.channel.send(f"Chup kar kutte {user.mention}")


@client.command(name="encourage")
async def id_(ctx):
    global counter
    await ctx.channel.send(quotes[counter])
    counter += 1
    if counter != 498:
        counter = 0


@client.command(name="gay")
async def id_(ctx):
    user = "<@510833310339956752>"
    await ctx.channel.send(f"BIGGEST GAY OF THE YEAR: {user}")


@client.command(name="insult")
async def id_(ctx, user: discord.User):
    if ctx.message.author.id == 490516690518540299 or ctx.message.author.id == 510833310339956752:
        insult = random.choice(insults)
        await ctx.channel.send(f"{user.mention}, {insult}")
    else:
        await ctx.channel.send(f"{ctx.author.mention}, you are not allowed to insult, stfu.")


@client.event
async def on_member_join(member):
    global channel
    embed = discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


@client.event
async def on_ready():
    global channel, counter
    print("We have logged in as {0.user}".format(client))
    time.sleep(5)
    channel = client.get_channel(833117650317869061)

    # await channel.send("Guess who's back? RICARDO ftw", file=discord.File('ricardo.gif'))
    await channel.send(quotes[counter])
    counter += 1


@tasks.loop(hours=24)
async def printer(self):
    global channel, counter
    await channel.send(quotes[counter])
    counter += 1
    if counter != 498:
        counter = 0


get()
token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)
