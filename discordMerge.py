#https://support.discord.com/hc/en-us/community/posts/360032701912-Channel-Merging
# https://discordpy.readthedocs.io/en/latest/api.html#discord.User.display_name

import os
import asyncio
import discord
from dotenv import load_dotenv
import discord.ext.commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
#GUILD = os.getenv("DISCORD_GUILD")
archiveID = 837804547623354438

client = discord.ext.commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.guilds[0]
    print(f'{guild.name} (id: {guild.id})')

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 1):
    await ctx.channel.purge(limit=amount + 1)

@client.command(name='arch', help='save history of channel')
async def arch(ctx, amount = 1):
    await ctx.channel.purge(limit=1)
    archiveChannel = ctx.guild.get_channel(archiveID)
    async for msg in ctx.channel.history(limit=amount, oldest_first=True):
        date = msg.created_at
        send = "`" + msg.author.display_name + " - " + str(msg.created_at) + "`\n"
        if msg.content != "":
            send += msg.content
        if msg.attachments:
            emb = discord.Embed(desciption='image', color=0x333333)
            emb.set_image(url=msg.attachments[0].url)
            await archiveChannel.send(content=send, embed=emb)
        else:
            await archiveChannel.send(send)



    #     msgs[date] = [msg.author.display_name, msg.content, msg.embeds]
    # for msg in msgs:
    #     hisMsg = "`" + msgs[msg][0] + " - " + str(msg) + "`\n"
    #     embMsg = []
    #     if msgs[msg][1] != "":
    #         hisMsg += msgs[msg][1]
    #         await ctx.send(content=hisMsg)
    #         hisMsg = ""
    #     if len(msgs[msg][2]) > 0:
    #         embMsg = msgs[msg][2][0]
    #         await ctx.send(embed=embMsg)
    

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



