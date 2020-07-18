import time
start = time.time()
import discord,requests,re,bs4,datetime,asyncio,json,random,sys,requests,json
from collections import namedtuple,OrderedDict
from discord.ext import tasks
from discord import Webhook, RequestsWebhookAdapter
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
    print('Logged in as')
    print(client2.user.name)
    print(client2.user.id)
    print('------')
    print('Logged in as')
    print(client1.user.name)
    print(client1.user.id)
    print('------')
    print('Logged in as')
    print(client3.user.name)
    print(client3.user.id)
    print('------')
    print('Logged in as')
    print(client4.user.name)
    print(client4.user.id)
    print('------')
    loop99.start()
    loop98.start()
    global start
    stop =time.time()
    result = stop -start
    with open('webhook.json') as f:
        webhook_iroioro = json.load(f)
    webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
    webhook.send(f"{result}秒で再起動しました(テキトー)", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    await client1.change_presence(activity=discord.Game(name="稼働中"))
    await client2.change_presence(activity=discord.Game(name="稼働中"))
    await client3.change_presence(activity=discord.Game(name='監視中'))

@client1.event
async def on_message(message):#考えろ
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    if message.content == "/reboot":
        await message.channel.send("再起動します")
        sys.exit()
    if message.content == "/seichi":
        await message.channel.send(ranking())
    GLOBAL_CH_NAME = "global_chat" # グローバルチャットのチャンネル名
    #ここから
    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client1.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="グローバル1",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
    GLOBAL_CH_NAME = "global_chat2" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client1.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="グローバル2",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
    #ここまでグローバル
    #ここからログぼ
    if message.channel.id == 717278803893813329:
        pt1 = random.randint(0,10)
        msg = f"{message.author.mention}{pt1}ptげっと\n"
        moneyadd(message.author.id,pt1)
        await message.channel.send(f"{msg}{txtread(message.author.id)}pt")
    if message.content == "/pt":
        txtread(message.author.id)
        await message.channel.send(f"{txtread(message.author.id)}pt")

@client1.event
async def on_member_join(member):
    channel = client1.get_channel(731658529483522179)
    await channel.send(member.mention + "さんが参加した様子")

@client2.event#おめが
async def on_message(message):
    global uuid
    mc=str(message.content)#内容保存
    mn=str(message.author.name)#名前保存
    cid=int(message.channel.id)#チャンネルＩＤ保存
    if message.author.bot:#botはじいてる
        return
    if cid == 697854272506953818:
        mcid = message.content
        p = re.compile(r"^[a-zA-Z0-9_]+$")
        if not p.fullmatch(mcid):
            await message.channel.send("MCIDに使えない文字が含まれています。")
            return
        if len(mcid) < 3:
            await message.channel.send("短すぎます！")
            return
        if len(mcid) > 16:
            await message.channel.send("長すぎます！")
            return
        url = f"https://w4.minecraftserver.jp/player/{mcid}"
        try:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            td = soup.td
            if not f'{mcid}' in f'{td}':
                await message.channel.send("整地鯖にログインしたことのないMCIDです。\n必ず小文字で入力してください")
                return
            last_login = soup.select('td')[1]
            await message.channel.send("整地鯖に入ったことがあるね!")
            await message.channel.send(last_login)
            role = discord.utils.get(message.guild.roles, name='会員')
            await message.author.add_roles(role)
            await message.channel.send("ロールを付与したよ！")
            name=mn
            old="なし"
            new="会員"
            CHANNEL_ID = 698195937792753704
            channel = client2.get_channel(CHANNEL_ID)
            speak = str(name+old+"->"+new)
            await channel.send(speak)
            CHANNEL_ID = 699526758889685012
            channel = client2.get_channel(CHANNEL_ID)
            speak = str(mn+"のMCID"+mc)
            await channel.send(speak)
        except requests.exceptions.HTTPError:
            await message.channel.send(f'requests.exceptions.HTTPError')
    elif cid == 707839980411551774:
        mcid = mc
        p = re.compile(r"^[a-zA-Z0-9_]+$")
        if not p.fullmatch(mcid):
            await message.channel.send("MCIDに使えない文字が含まれています。")
            return
        if len(mcid) < 3:
            await message.channel.send("短すぎます！")
            return
        if len(mcid) > 16:
            await message.channel.send("長すぎます！")
            return
        url = f"https://w4.minecraftserver.jp/player/{mcid}"
        try:
            res = requests.get(url)
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            td = soup.td
            if not f'{mcid}' in f'{td}':
                await message.channel.send("整地鯖にログインしたことのないMCIDです。\n必ず小文字で入力してください")
                return
            last_login = soup.select('td')[1]
            print(str(last_login)+"\n-----_")#エラー防止
            role = discord.utils.get(message.guild.roles, name='ストーンリーグ')
            await message.author.add_roles(role)
            await message.channel.send(f":ok:\nロールを付与したよ！\nhttps://api.mojang.com/users/profiles/minecraft/{mcid}\n<@672910471279673358><@684949442280947718>コードに追加しやがれ")
            CHANNEL_ID = 708269184664076332
            channel = client2.get_channel(CHANNEL_ID)
            speak = str(mn+"がグランドリーグに参加しました")
            await channel.send(speak)
        except requests.exceptions.HTTPError:
            await message.channel.send(f'requests.exceptions.HTTPError')
    if mc == "/seichi":
        mcid_uuid_dic = uuid
        msg = ""
        kaisuu = 0
        for mcid in mcid_uuid_dic.keys():
            uuid = mcid_uuid_dic[mcid]
            resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types=break')
            data_json = json.loads(resp.text)
            data = data_json[0]["data"]["raw_data"]
            msg += f"{mcid}の整地量>>>{data}\n"
            kaisuu += 1
            if kaisuu == 7:
                await message.channel.send(msg)
    if mc == "/reboot":
        await message.channel.send("再起動します")
        sys.exit()

@client3.event#ばいばい
async def on_message(message):
    global start1
    global start2
    global start3
    global start4
    global start5
    global start6
    global start7
    global iitai_koto
    global syuppin_butu
    global kaishi_gaku
    global sokketu_gaku
    global syuppin_sya
    global tanni
    if message.author.bot:
        return
    if message.channel.id == 723872932488675425:
        pass
    elif message.channel.category_id == 721478471712374811 and message.channel.id == 721479071833522296:
        if client3.user in message.mentions:
            if start1 == False:
                embed=discord.Embed(title="オークションを開始しますか？", description="**yes**で開始\n**no**でキャンセルします\n**必ず小文字で入力してください**", color=0xff0000)
                await message.channel.send(embed=embed)
                start1 = True
        elif message.content == "yes" and start1 == True:
            start1 = False
            start2 = False
            start3 = False
            start4 = False
            start5 = False
            embed = discord.Embed(title="出品物を書いてください", description="", color=0xff0000)
            await message.channel.send(embed=embed)
            start1 = False
            start2 = True
            return
        elif message.content == "no" and start1 == True:
            await message.channel.send("キャンセルしました\n------------------------")
            start1 = False
        elif  start2 == True:
            syuppin_butu = message.content
            embed = discord.Embed(title="開始額を書いてください", description="", color=0xff0000)
            await message.channel.send(embed=embed)
            start2 = False
            start3 = True
            return
        elif  start3 == True:
            try:
                kaishi_gaku = int(message.content)
                embed = discord.Embed(title="即決額を書いてください", description="なしの場合は**no**と書いてください", color=0xff0000)
                await message.channel.send(embed=embed)
                start4 = True
                start3 = False
            except:
                await message.channel.send("整数で入力して下さい\nリセットします")
                start1 = False
                start2 = False
                start3 = False
                start4 = False
                start5 = False
            return
        elif start4 == True:
            embed = discord.Embed(title="その他言いたいことなど", description="ない場合はなしで", color=0xff0000)
            await message.channel.send(embed=embed)
            if message.content == "no":
                sokketu_gaku = "none"
            else:
                try:
                    sokketu_gaku = int(message.content)
                    sokketu =True
                except:
                    await message.channel.send("整数で入力して下さい\nリセットします")
                    start1 = False
                    start2 = False
                    start3 = False
                    start4 = False
                    start5 = False
            start4 = False
            start5 = True
            return
        elif start5 == True:
            iitai_koto = message.content
            embed = discord.Embed(title="単位を書いてください", description="椎名、ガチャ券など", color=0xff0000)
            await message.channel.send(embed=embed)
            start6 = True
            start5 = False
        elif start6 == True:
            tanni = message.content
            embed = discord.Embed(title="この内容でいいですか？", description="いいなら**yes**を\nダメなら**no**を", color=0xff0000)
            embed.add_field(name="出品物", value=syuppin_butu, inline=True)
            embed.add_field(name="開始額", value=kaishi_gaku, inline=True)
            embed.add_field(name="即決額", value=sokketu_gaku, inline=True)
            embed.add_field(name="単位", value=tanni, inline=True)
            embed.add_field(name="言いたいこと", value=iitai_koto, inline=True)
            await message.channel.send(embed=embed)
            start7 = True
            start6 = False
            return
        elif message.content == "yes" and start7 == True:
            start1 = False
            start2 = False
            start3 = False
            start4 = False
            start5 = False
            start6 = False
            start7 = False
            syuppin_sya = message.author.id
            await message.channel.purge()
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name=syuppin_butu)
            embed = discord.Embed(title="オークションが始まりました", description="", color=0xff0000)
            embed.add_field(name="出品物", value=syuppin_butu, inline=True)
            embed.add_field(name="開始額", value=kaishi_gaku, inline=True)
            embed.add_field(name="即決額", value=sokketu_gaku, inline=True)
            embed.add_field(name="単位", value=tanni, inline=True)
            embed.add_field(name="言いたいこと", value=iitai_koto, inline=True)
            embed.set_author(name=message.author.display_name, 
                icon_url=message.author.avatar_url_as(format="png"))
            await new_channel.send(embed=embed)
            await new_channel.edit(topic=f"{syuppin_butu},{kaishi_gaku},{sokketu_gaku},{syuppin_sya},{tanni},,なし,未入札")
            return
        elif message.content == "no" and start6 == True:
            await message.channel.send("キャンセルしました\n------------------------")
            start1 = False
            start2 = False
            start3 = False
            start4 = False
            start5 = False
            start6 = False
            start7 = False
    elif message.channel.category_id == 721478471712374811:
        if message.content == "/del":
            if message.author.guild_permissions.administrator:
                await message.channel.delete()
            else:
                await message.channel.send('お前にはできない。')
        elif message.content == "/end":
            topic_list=message.channel.topic.split(",")
            if int(topic_list[3]) == message.author.id:
                channel = client3.get_channel(723872932488675425)
                embed = discord.Embed(title="オークションが終了しました", description="", color=0xff0000)
                embed.add_field(name="出品物", value=topic_list[0], inline=True)
                embed.add_field(name="落札者", value=topic_list[6], inline=True)
                embed.add_field(name="落札額", value=topic_list[7], inline=True)
                embed.add_field(name="単位", value=topic_list[4], inline=True)
                embed.set_author(name=message.author.display_name, 
                    icon_url=message.author.avatar_url_as(format="png"))
                await channel.send(embed=embed)
                await message.channel.delete()
            else:
                await message.channel.send('お前にはできない。')
        else:
            try:
                topic_list=message.channel.topic.split(",")
                if  int(topic_list[7]) < int(message.content):
                    embed = discord.Embed(title="入札", description=int(message.content), color=0xff0000)
                    embed.set_author(name=message.author.display_name, 
                        icon_url=message.author.avatar_url_as(format="png"))
                    topic_list=message.channel.topic.split(",,")
                    await message.delete()
                    await message.channel.send(embed=embed)
                    await message.channel.edit(topic=f"{topic_list[0]},,{message.author.name},{message.content}")
                elif str(topic_list[3]) == str(message.content):
                    if message.content != "none":
                        await message.channel.delete()
                        channel = client3.get_channel(723872932488675425)
                        embed = discord.Embed(title="オークションが終了しました", description="", color=0xff0000)
                        embed.add_field(name="出品物", value=topic_list[0], inline=True)
                        embed.add_field(name="落札者", value=topic_list[6], inline=True)
                        embed.add_field(name="落札額", value=topic_list[7], inline=True)
                        embed.add_field(name="単位", value=topic_list[4], inline=True)
                        embed.set_author(name=message.author.display_name, 
                            icon_url=message.author.avatar_url_as(format="png"))
                        await channel.send(embed=embed)
            except:
                pass
@client4.event#ウパ
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/reboot":
        await message.channel.send("再起動します")
        sys.exit()
#よくわからんけど2レジありがとう
#Copyright (c) 2020 disneyresidents
#Released under the MIT license
#https://opensource.org/licenses/mit-license.php
@tasks.loop(seconds=60)
async def loop99():
    global uuid
    now = datetime.datetime.now().strftime("%H:%M")
    if now == "23:58":
        try:
            mcid_uuid_dic = dict(uuid)
            msg = "<@&7394341806735361>発表時間です\n"
            kaisuu = 0
            for mcid in mcid_uuid_dic.keys():
                uuid = mcid_uuid_dic[mcid]
                resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types=break')
                data_json = json.loads(resp.text)
                data = data_json[0]["data"]["raw_data"]
                msg += f"{mcid}の整地量>>>{data}\n"
                kaisuu += 1
                if kaisuu == 7:
                    CHANNEL_ID = 707959412664303616
                    channel = client2.get_channel(CHANNEL_ID)
                    await channel.send(msg)
            channel = client1.get_channel(730343987906347138)
            await channel.send(ranking())
        except:
            CHANNEL_ID = 707959412664303616
            channel = client2.get_channel(CHANNEL_ID)
            await channel.send("エラーが発生したんで今日はないです")
    elif now == "23:55":
        sys.exit()
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
discord_bot_token_2 = token["client2"]
discord_bot_token_3 = token["client3"]
discord_bot_token_4 = token["client4"]
Entry = namedtuple("Entry", "client event token")
entries = [
    Entry(client=client1,event=asyncio.Event(),token=discord_bot_token_1),
    Entry(client=client2,event=asyncio.Event(),token=discord_bot_token_2),
    Entry(client=client3,event=asyncio.Event(),token=discord_bot_token_3),
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