import discord
import os

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

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


@client.event
async def on_member_join(member):
    channel = client.get_channel(833117650317869061)
    embed = discord.Embed(title=f"Welcome {member.name}", description=f"Thanks for joining {member.guild.name}!")
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)


token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)
