import re,discord

@client.event
async def on_message(message):
    if message.content in "https://ptb.discordapp.com/channels/":
        embeds = []
        msg_link = message.content.split("https://ptb.discordapp.com/channels/")
        msg_id = msg_link.split("/")
        msg = await client.get_channel(msg_id[1]).fetch_message(msg_id[2])
        for r in msg.reactions:
            reaction += f"{r} | **{r.count} 回**"
        embed = discord.Embed(title="",
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        embed.add_field(name="リアクション", value=reaction, inline=True)
        embeds.apped(embed)
        embeds.apped(msg.embeds)
        await message.channel.send(embed=embeds)
    elif message.content in "https://discordapp.com/channels/":
        msg_link = message.content.split("https://discordapp.com/channels/")
        msg_id = msg_link.split("/")
        msg = await client.get_channel(msg_id[1]).fetch_message(msg_id[2])
        for r in msg.reactions:
            reaction += f"{r} | **{r.count} 回**"