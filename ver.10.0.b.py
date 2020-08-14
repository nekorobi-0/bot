import time
start = time.time()
import discord,requests,re,datetime,asyncio,json,random,requests,json
now = datetime.datetime.now().strftime("%H:%M")
if now[3:] == "00":
    while now[3:] == "00":
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H:%M")
from collections import namedtuple,OrderedDict
from discord.ext import tasks
from discord import Webhook, RequestsWebhookAdapter
with open('webhook.json') as f:
    webhook_iroioro = json.load(f)
webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
webhook.send(f"importが終わりました{time.time() - start}秒importにかかりました(ラズパイ)", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
client1 = discord.Client()
client2 = discord.Client()
client3 = discord.Client()
client4 = discord.Client()
start1 = False
start2 = False
start3 = False
start4 = False
start5 = False
start6 = False
start7 = False
syuppin_butu = ""
kaishi_gaku = 0
sokketu_gaku = 0
iitai_koto = ""
syuppin_sya = ""
tanni = ""

def ranking():
    try:
        resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking?type=break&offset=0&lim=50&duration=daily')
        data_json = json.loads(resp.text)
        rank_list = list(data_json["ranks"])
        msg = "```\n"
        rank = 1
        for mcid_data in rank_list:
            get_mcid = mcid_data["player"]
            get_data = mcid_data["data"]
            seichi_ryo = get_data["raw_data"]
            name = get_mcid["name"]
            if len(str(seichi_ryo)) > 8:
                seichi_ryo_kugiri0 = str(seichi_ryo)[-4:]
                seichi_ryo_kugiri1 = str(seichi_ryo)[-8:-4]
                seichi_ryo_kugiri2 = str(seichi_ryo)[:-8]
                seichi_ryo = f"{seichi_ryo_kugiri2}億{seichi_ryo_kugiri1}万{seichi_ryo_kugiri0}"
            elif len(str(seichi_ryo)) > 4:
                seichi_ryo_kugiri0 = str(seichi_ryo)[-4:]
                seichi_ryo_kugiri1 = str(seichi_ryo)[:-4]
                seichi_ryo = seichi_ryo_kugiri1 + "万" + seichi_ryo_kugiri0
            msg += f"{rank}位 {name} 整地量:{seichi_ryo}\n"
            rank += 1
        msg += "```"
        return msg
    except:
        text = "エラーが発生したよ"
        return text
#ログインボーナス
def txtread(setid):
    ints = 0
    path = "datas.txt"
    with open(path) as f:
        dataaa = f.readlines()
        idid = int("0")
    try:
        while idid != setid:
            text2=[]
            text = dataaa[ints]
            text2=text.split("!")
            text3 = text2[0].split("\n")
            idid = int(text3[0])
            ints = ints + 1
    except:
        myset(setid)
        return txtread(setid)
    return int(text2[1])
def moneyadd(setid,moneyadd):
    money = txtread(setid)
    setmoney= int(money) + int(moneyadd)
    newdata =str(setid) + "!" + str(setmoney)
    olddata = str(setid) + "!" + str(money)
    file_name = "datas.txt"
    with open(file_name, encoding="cp932") as f:
        data_lines = f.read()
    data_lines = data_lines.replace(olddata,newdata)
    with open(file_name, mode="w", encoding="cp932") as f:
        f.write(data_lines)
def myset(id):
    path = "datas.txt"
    b = str(id) 
    c = str(0)
    with open(path, mode='a') as f:
        a = str("\n"+b + "!" + c)
        f.write(a)
#ここまで
with open('uuid.json') as f:
    uuid = json.load(f)
@client1.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client1.user.name)
    print(client1.user.id)
    print(client4.user.name)
    print(client4.user.id)
    #print(ext_client.user.name)
    #print(ext_client.user.id)
    print('------')
    loop98.start()
    global start
    stop =time.time()
    result = stop -start
    with open('webhook.json') as f:
        webhook_iroioro = json.load(f)
    webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
    webhook.send(f"再起動が終わりました{result}秒再起動にかかりました(ラズパイ)", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    webhook = Webhook.partial(734666355944718428, webhook_iroioro["token_reboot1"], adapter=RequestsWebhookAdapter())
    webhook.send(f"再起動が終わりました{result}秒再起動にかかりました(ラズパイ)", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    await client1.change_presence(activity=discord.Game(name="稼働中"))
    await client4.change_presence(activity=discord.Game(name="稼働中"))

@client1.event
async def on_message(message):#考えろ
    if message.author.bot:
        return
    if message.content == "/seichi":
        await message.channel.send(ranking())
    GLOBAL_CH_NAME = "global_chat"
    if message.channel.name == GLOBAL_CH_NAME:
        await message.delete()
        channels = client1.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(title="グローバル1",
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        for channel in global_channels:
            await channel.send(embed=embed)
    GLOBAL_CH_NAME = "global_chat2"
    if message.channel.name == GLOBAL_CH_NAME:
        await message.delete()
        channels = client1.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(title="グローバル2",
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        for channel in global_channels:
            await channel.send(embed=embed)
    #ここまでグローバル
    #ここからログぼ
    if message.channel.id == 717278803893813329:
        old =  txtread(message.author.id)
        pt1 = random.randint(-20,30)
        msg = f"{message.author.mention}{pt1}ptげっと\n"
        moneyadd(message.author.id,pt1)
        await message.channel.send(f"{msg}{old}->{txtread(message.author.id)}pt")
    if message.content == "/pt":
        txtread(message.author.id)
        await message.channel.send(f"{txtread(message.author.id)}pt")
    #update_rog
    if message.channel.id == 735069077281833010:
        channel = client1.get_channel(734666320448323596)
        embed = discord.Embed(title="bot_update", description=message.content, color=0xff0000)
        await channel.send(embed=embed)



@client1.event
async def on_member_join(member):
    channel = client1.get_channel(731658529483522179)
    await channel.send(f"{member.mention}さんが{member.guild.name}に参加した様子")

@client1.event
async def on_member_remove(member):
    channel = client1.get_channel(731658529483522179)
    await channel.send(f"{member.mention}さんが{member.guild.name}を退出した様子")

@client1.event
async def on_guild_join(guild):
    channel = client1.get_channel(731658529483522179)
    await channel.send(f"botが{guild.name}に参加した様子")

@client1.event
async def on_guild_remove(guild):
    channel = client1.get_channel(731658529483522179)
    await channel.send(f"botが{guild.name}から抜けた様子")

@client1.event
async def on_guild_channel_create(channel):
    msg = f"{channel.guild.name}で{channel.name}が作成された様子"
    channel = client1.get_channel(737207294458069053)
    await channel.send(msg)

@client1.event
async def on_guild_channel_delete(channel):
    msg = f"{channel.guild.name}の{channel.name}が削除された様子"
    channel = client1.get_channel(737207294458069053)
    await channel.send(msg)

@client4.event#ウパ
async def on_message(message):
    if message.author.bot:
        return
    with open('say.json') as f:
        say = json.load(f)
    for key in say.keys():
        if key in message.content:
            msg = say[key]
            await message.channel.send(msg)
#2レジありがとう
@tasks.loop(seconds=60)
async def loop98():
    now = datetime.datetime.now().strftime("%H:%M")
    if now == "23:59":
        with open('webhook.json') as f:
            webhook_iroioro = json.load(f)
        webhook = Webhook.partial(734184972059017236, webhook_iroioro["token_hizuke"], adapter=RequestsWebhookAdapter())
        webhook.send("たぶん日付変わる直前", username='日付変更君',avatar_url=webhook_iroioro["avater_hizuke"])
#token
with open('token.json') as f:
    token = json.load(f)
#keiさんありがとう...
discord_bot_token_1 = token["client1"]
#discord_bot_token_2 = token["client2"]
#discord_bot_token_3 = token["client3"]
discord_bot_token_4 = token["client4"]
ext_bot_token = token["client1"]
Entry = namedtuple("Entry", "client event token")
entries = [
    Entry(client=client1,event=asyncio.Event(),token=discord_bot_token_1),
    Entry(client=client4,event=asyncio.Event(),token=discord_bot_token_4),
]  

async def login():
    for e in entries:
        await e.client.login(e.token)

async def wrapped_connect(entry):
    try:
        await entry.client.connect()
    except Exception as e:
        await entry.client.close()
        print("We got an exception: ", e.__class__.__name__, e)
        entry.event.set()

async def check_close():
    futures = [e.event.wait() for e in entries]
    await asyncio.wait(futures)

loop = asyncio.get_event_loop()
loop.run_until_complete(login())
for entry in entries:
    loop.create_task(wrapped_connect(entry))
loop.run_until_complete(check_close())
loop.close()
