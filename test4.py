import discord,requests,re,bs4,datetime,time,asyncio,json,random
from collections import namedtuple,OrderedDict
from discord.ext import tasks
client1 = discord.Client()
client2 = discord.Client()
client3 = discord.Client()
client4 = discord.Client()
first = True
sokketu = 0
nedann2 = 0
itemname="なし!"
gendaiti = 0
k4 = 0
omn = "なし"
omn2 = "なし"
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
    CHANNEL_ID = 713273848124014592
    channel = client1.get_channel(CHANNEL_ID)
    await channel.send("再起動成功")
    await client1.change_presence(activity=discord.Game(name="稼働中"))
    await client2.change_presence(activity=discord.Game(name="稼働中"))
    await client3.change_presence(activity=discord.Game(name='監視中'))
    await client4.change_presence(activity=discord.Game(name='オークションなし'))

@client1.event
async def on_message(message):#考えろ
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
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
        msg = f"{pt1}ptげっと\n"
        with open('pt.json') as f:
            pt = json.load(f)
        try:
            old = int(pt[message.author.id])
            msg += str(old) + "pt->"
            pt.pop(message.author.id)
            pt.pop(message.author.id)
            pt[int(message.author.id)] = pt1 + old
        except:
            pt[int(message.author.id)] = pt1
        msg += str(pt[message.author.id]) + "pt"
        with open('pt.json', 'w') as f:
            json.dump(pt, f, indent=2, ensure_ascii=False)
        await message.channel.send(msg)
        #これでうごくよな？
    if message.content == "/pt":
        with open('pt.json') as f:
            pt = json.load(f)
        await message.channel.send(f"{pt[message.author.id]}pt")

@client2.event#おめが
async def on_message(message):
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
                await message.channel.send("整地鯖にログインしたことのないMCIDです。")
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
            await message.channel.send("MCIDに使えない文字が含まれています。\n小文字で入力するといいかも?")
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
                await message.channel.send("整地鯖にログインしたことのないMCIDです。")
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
        mcid_uuid_dic = {
            "nekorobi_0": "d6be1561-47c1-4e67-9829-2aca48f9be39",
            "wanwanwan_o": "bab130b9-2247-4b18-967a-0867edcccf69",
            "NaCl2375": "9c565f26-ea8d-4c03-9731-1c89282ab2b9",
            "Moti_Yonko": "fdd25f48-395d-482d-aefc-345aa354c83a",
            "Arwing_1224": "20fd72b0-4835-4504-87e7-f1cb34b84447",
            "ENS_ATF": "b2100f40-b3a4-486a-b4e0-048fd64144af"
        }
        msg = ""
        kaisuu = 0
        for mcid in mcid_uuid_dic.keys():
            uuid = mcid_uuid_dic[mcid]
            resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types=break')
            data_json = json.loads(resp.text)
            data = data_json[0]["data"]["raw_data"]
            msg += f"{mcid}の整地量>>>{data}\n"
            kaisuu += 1
            if kaisuu == 6:
                await message.channel.send(msg)

@client3.event#ばいばい
async def on_message(message):
    buydata=[]
    mc=str(message.content)#内容保存
    mn=str(message.author.name)#名前保存
    buydata=mc.split("!")#!で分ける
    dataaaaaa = mc.split(" ")
    cid=int(message.channel.id)#チャンネルＩＤ保存
    if buydata[0]=="b":#買いか
        if cid==699804347403468801 or cid==698735320870420520:#チャンネルはあってるか
            await message.delete()
            if message.author.bot:
                return
            speak = buydata[1]+"を"+mn+"が"+buydata[2]+"買った！"#話す内容保存
            await message.channel.send(speak)#送信
    if buydata[0]=="s":#売りか
        if cid==699804347403468801 or cid == 698735320870420520:#チャンネルはあってるか
            await message.delete()
            if message.author.bot:#botはじいてる
                return
            speak = buydata[1]+"を"+mn+"が"+buydata[2]+"売った！"#話す内容保存
            await message.channel.send(speak)#送信
    if dataaaaaa[0]=="r":
        await message.delete()
        if message.author.bot:#botはじいてる
            return
        speak = dataaaaaa[1]
        await message.channel.send(speak)#送信
    if buydata[0]=="rn":
        await message.delete()
        if message.author.bot:#botはじいてる
            return
        speak = mn+">>>"+buydata[1]
        await message.channel.send(speak)#送信
    if buydata[0]=="k":
        await message.delete()
        if message.author.bot:#botはじいてる
            return
        if buydata[2]=="+":
            speak1=int(buydata[1])+int(buydata[3])
        elif buydata[2]=="-":
            speak1=int(buydata[1])-int(buydata[3])
        elif buydata[2]=="*":
            speak1=int(buydata[1])*int(buydata[3])
        elif buydata[2]=="/":
            speak1=int(buydata[1])/int(buydata[3])
        speak = (mn) + ("からの計算依頼の答え>>>")+str(speak1)
        await message.channel.send(speak)#送信
    if buydata[0]=="help":
        if message.author.bot:#botはじいてる
            return
        await message.delete()#消してる
        embed=discord.Embed(title="help", description="起動はhelp", color=0xff0000)
        embed.add_field(name="買う", value="b!買いたいもの!数量+単位", inline=True)
        embed.add_field(name="売る", value="s!売りたいもの!数量+単位", inline=True)
        embed.add_field(name="計算", value="k!数値１!演算子!数値２", inline=True)
        embed.add_field(name="代弁(無記名)", value="r 言わせたいこと", inline=True)
        embed.add_field(name="代弁(記名あり)", value="rn!言わせたいこと", inline=True)
        embed.add_field(name="やりたいこと", value="計算機能強化", inline=True)
        embed.set_footer(text="+不要")
        await message.channel.send(embed=embed)#送信
@client4.event#おく
async def on_message(message):
    buydata=[]
    mc=str(message.content)#内容保存
    mn=str(message.author.name)#名前保存
    buydata=mc.split("!")#!で分ける
    cid=int(message.channel.id)#チャンネルＩＤ保存
    if cid==712572591864283217:#チャンネル
        if message.author.bot:#botはじいてる
            return
        await message.delete()
        if buydata[0]=="o":
            if buydata[1]=="no":
                siina = str("なし")
            else:
                nedan = buydata[1]
                ryou = nedan.split("st")#stで分ける
                k1 = int(ryou[0])*64
                siina= k1 + int(ryou[1])
            tanni = buydata[4]
            nedann4 = buydata[3]
            kingaku = nedann4.split("st")#stで分ける
            global omn
            omn = mn
            global omn2
            omn2 = mn
            global itemname
            itemname = str(buydata[2])
            global sokketu
            sokketu = (siina)
            global gendaiti
            gendaiti = int(kingaku[0])*64+int(kingaku[1])
            embed=discord.Embed(title="オークション開始", description="出品者:"+mn, color=0xff0000)
            embed.add_field(name="出品物", value=itemname, inline=False)
            embed.add_field(name="即決額", value=sokketu, inline=False)
            embed.add_field(name="始値", value=str(gendaiti) + str(tanni), inline=False)
            await message.channel.send(embed=embed)#送信
            await client4.change_presence(activity=discord.Game(name='オークション開催中'))
        if buydata[0]=="n":
            g1 = str(buydata[1])
            k2 = g1.split("st")
            k3 = int(k2[0])*64
            global k4
            k4 = k3 + int(k2[1])
            if k4 == sokketu:
                embed=discord.Embed(title="オークション終了", description="落札者:"+mn, color=0xff0000)
                embed.add_field(name="値段", value=str(buydata[1]), inline=False)
                await message.channel.send(embed=embed)#送信
                omn = "なし"
                omn2 = "なし"
                itemname="なし!"
                gendaiti = 0
                await client4.change_presence(activity=discord.Game(name='オークションなし'))
            elif k4 > gendaiti:
                omn = mn
                gendaiti = k3 + int(k2[1])
                embed=discord.Embed(title="現在の価格", description=mn, color=0xff0000)
                embed.add_field(name="値段", value=gendaiti, inline=False)
                await message.channel.send(embed=embed)
        if buydata[0]=="e":
            if omn2 == mn:
                embed=discord.Embed(title="オークション終了", description="落札者:"+omn, color=0xff0000)
                embed.add_field(name="値段", value=int(gendaiti), inline=False)
                await message.channel.send(embed=embed)#送信
                omn = "なし"
                omn2 = "なし"
                itemname="なし!"
                gendaiti = 0
                await client4.change_presence(activity=discord.Game(name='オークションなし'))
            else:
                embed=discord.Embed(title="オークション終了しねぇよ", description="ばかめ", color=0xff0000)
                embed.add_field(name="値段", value=int(gendaiti), inline=False)
                await message.channel.send(embed=embed)#送信
#よくわからんけど2レジありがとう
#Copyright (c) 2020 disneyresidents
#Released under the MIT license
#https://opensource.org/licenses/mit-license.php
@tasks.loop(seconds=60)
async def loop99():
    now = datetime.datetime.now().strftime("%H:%M")
    if now == "23:58":
        mcid_uuid_dic = {
            "nekorobi_0": "d6be1561-47c1-4e67-9829-2aca48f9be39",
            "wanwanwan_o": "bab130b9-2247-4b18-967a-0867edcccf69",
            "NaCl2375": "9c565f26-ea8d-4c03-9731-1c89282ab2b9",
            "Moti_Yonko": "fdd25f48-395d-482d-aefc-345aa354c83a",
            "Arwing_1224": "20fd72b0-4835-4504-87e7-f1cb34b84447",
            "ENS_ATF": "b2100f40-b3a4-486a-b4e0-048fd64144af"
        }
        msg = "<@707444280121360464>発表時間です\n"
        kaisuu = 0
        for mcid in mcid_uuid_dic.keys():
            uuid = mcid_uuid_dic[mcid]
            resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking/player/{uuid}?types=break')
            data_json = json.loads(resp.text)
            data = data_json[0]["data"]["raw_data"]
            msg += f"{mcid}の整地量>>>{data}\n"
            kaisuu += 1
            if kaisuu == 6:
                CHANNEL_ID = 707959412664303616
                channel = client2.get_channel(CHANNEL_ID)
                await channel.send(msg)
#2レジありがとう
@tasks.loop(seconds=60)
async def loop98():
    now = datetime.datetime.now().strftime("%H:%M")
    if now == "23:59":
        CHANNEL_ID = 713248979571179560
        channel = client1.get_channel(CHANNEL_ID)
        await channel.send("そろそろ日付が変わります")
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