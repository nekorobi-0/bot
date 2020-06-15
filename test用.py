import discord
client = discord.Client()
@client.event
async def on_ready():
    
with open('token.json') as f:
    token = json.load(f)
#keiさんありがとう...
client.run(token["client1"])