import discord,requests,re,bs4,datetime,time,asyncio,json,random
from collections import namedtuple,OrderedDict
from discord.ext import tasks
client1 = discord.Client()
client2 = discord.Client()
client3 = discord.Client()
start = 0
syuppin_butu = ""
kaishi_gaku = 0
sokketu_gaku = 0
iitai_koto = ""
syuppin_sya = ""
tanni = ""
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
    loop99.start()
    loop98.start()
    CHANNEL_ID = 713273848124014592
    channel = client1.get_channel(CHANNEL_ID)
    await channel.send("再起動成功")
    await client1.change_presence(activity=discord.Game(name="稼働中"))
    await client2.change_presence(activity=discord.Game(name="稼働中"))
    await client3.change_presence(activity=discord.Game(name='監視中'))

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

@client3.event#ばいばい
async def on_message(message):
    global start
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
            if start == 0:
                embed=discord.Embed(title="オークションを開始しますか？", description="**yes**で開始\n**no**でキャンセルします\n**必ず小文字で入力してください**", color=0xff0000)
                await message.channel.send(embed=embed)
                start = 1
        elif message.content == "yes" and start == 1:
            embed = discord.Embed(title="出品物を書いてください", description="", color=0xff0000)
            await message.channel.send(embed=embed)
            start = 2
            return
        elif message.content == "no" and start == 1:
            await message.channel.send("キャンセルしました\n------------------------")
            start = 0
        elif  start == 2:
            syuppin_butu = message.content
            embed = discord.Embed(title="開始額を書いてください", description="", color=0xff0000)
            await message.channel.send(embed=embed)
            start = 3
            return
        elif  start == 3:
            try:
                kaishi_gaku = int(message.content)
                embed = discord.Embed(title="即決額を書いてください", description="なしの場合は**no**と書いてください", color=0xff0000)
                await message.channel.send(embed=embed)
                start = 4
            except:
                await message.channel.send("整数で入力して下さい\nリセットします")
                start = 0
            return
        elif start == 4:
            embed = discord.Embed(title="その他言いたいことなど", description="ない場合はなしで", color=0xff0000)
            await message.channel.send(embed=embed)
            if message.content == "no":
                sokketu_gaku = "none"
            else:
                try:
                    sokketu_gaku = int(message.content)
                    start = 5
                except:
                    await message.channel.send("整数で入力して下さい\nリセットします")
                    start = 0
            return
        elif start == 5:
            iitai_koto = message.content
            embed = discord.Embed(title="単位を書いてください", description="椎名、ガチャ券など", color=0xff0000)
            await message.channel.send(embed=embed)
            start = 6
        elif start == 6:
            tanni = message.content
            embed = discord.Embed(title="この内容でいいですか？", description="いいなら**yes**を\nダメなら**no**を", color=0xff0000)
            embed.add_field(name="出品物", value=syuppin_butu, inline=True)
            embed.add_field(name="開始額", value=kaishi_gaku, inline=True)
            embed.add_field(name="即決額", value=sokketu_gaku, inline=True)
            embed.add_field(name="単位", value=tanni, inline=True)
            embed.add_field(name="言いたいこと", value=iitai_koto, inline=True)
            await message.channel.send(embed=embed)
            start = 7
            return
        elif message.content == "yes" and start == 7:
            start = 0
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
            await new_channel.edit(topic=f"{syuppin_butu},{kaishi_gaku},{sokketu_gaku},{syuppin_sya},{tanni},,なし,{kaishi_gaku}")
            return
        elif message.content == "no" and start == 6:
            await message.channel.send("キャンセルしました\n------------------------")
            start = 0
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
                if  int(topic_list[1]) < int(message.content):
                    embed = discord.Embed(title="入札", description=int(message.content), color=0xff0000)
                    embed.set_author(name=message.author.display_name, 
                        icon_url=message.author.avatar_url_as(format="png"))
                    topic_list=message.channel.topic.split(",,")
                    await message.delete()
                    await message.channel.send(embed=embed)
                    await message.channel.edit(topic=f"{topic_list[0]},,{message.author.name},{message.content}")
            except:
                pass
#よくわからんけど2レジありがとう
#Copyright (c) 2020 disneyresidents
#Released under the MIT license
#https://opensource.org/licenses/mit-license.php
@tasks.loop(seconds=60)
async def loop99():
    global uuid
    now = datetime.datetime.now().strftime("%H:%M")
    if now == "23:58":
        mcid_uuid_dic = uuid
        msg = "<@7394341806735361>発表時間です\n"
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
Entry = namedtuple("Entry", "client event token")
entries = [
    Entry(client=client1,event=asyncio.Event(),token=discord_bot_token_1),
    Entry(client=client2,event=asyncio.Event(),token=discord_bot_token_2),
    Entry(client=client3,event=asyncio.Event(),token=discord_bot_token_3),
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