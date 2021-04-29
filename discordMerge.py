#https://support.discord.com/hc/en-us/community/posts/360032701912-Channel-Merging
#define butt 88
import discord

# connect to guild
id = 261301479036420097
client = discord.Client()
client.connect()

client.close()

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



