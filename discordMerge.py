#https://support.discord.com/hc/en-us/community/posts/360032701912-Channel-Merging
# https://discordpy.readthedocs.io/en/latest/api.html#discord.User.display_name

import os
import asyncio
import discord
from dotenv import load_dotenv
import discord.ext.commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
testID = 837354270939545670

client = discord.ext.commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.guilds[0]
    print(f'{guild.name} (id: {guild.id})')

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit=amount)

@client.command(name='history', help='save history of channel')
async def history(ctx, amount = 5):
    msgs = {}
    counter = 0
    async for message in ctx.channel.history(limit=amount):
        counter += 1
        auth = str(message.author.display_name) + "-" + str(counter)
        msgs[auth] = message.content
    print(msgs)

@client.command(name='nick', help='change bot name')
async def nick(ctx, newname = "noname"):
    await ctx.guild.get_member(client.user.id).edit(nick=newname)

@client.command(name='pong', help='test')
async def pong(ctx):
    await ctx.send("pong")



client.run(TOKEN)


# connect to guild
id = 261301479036420097

# download
chat = {1:"test",
        2:"this",
        33:"shit"}
chat2 = {1:"red",
        248:"green",
        20:"blue"}
print(chat[1])
print(chat2[1])

# merge
chatSorted = {}
for key in chat:
    chatSorted[key] = chat[key]
for key in chat2:
    # check if key exists, duplicate
    new = key
    while new in chatSorted:
        # dont know if always going to be an int
        # if this is time stamps need to not hop, instead place in between
        # depends on thetime precision, if tie at max pos, add dTime
        new += 1 # alternate key suffix
    chatSorted[new] = chat2[key]
print(chatSorted)

# sort
chatSorted = dict(sorted(chatSorted.items()))
print(chatSorted)

# save
fart = 1
print(fart * 9999)



