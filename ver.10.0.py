import time
start = time.time()
import discord,requests,re,bs4,datetime,asyncio,json,random,sys,requests,json
now = datetime.datetime.now().strftime("%H:%M")
if now[3:] == "00":
    while now[3:] == "00":
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H:%M")
import matplotlib as mpl
from collections import namedtuple,OrderedDict
from discord.ext import tasks,commands
from discord import Webhook, RequestsWebhookAdapter
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
with open('webhook.json') as f:
    webhook_iroioro = json.load(f)
webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
webhook.send(f"importが終わりました{time.time() - start}秒importにかかりました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
client2 = discord.Client()
client3 = discord.Client()
ext_client = commands.Bot(command_prefix='/')
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
async def reboot():
    with open('webhook.json') as f:
        webhook_iroioro = json.load(f)
    webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
    webhook.send("再起動、始めました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    webhook = Webhook.partial(734666355944718428, webhook_iroioro["token_reboot1"], adapter=RequestsWebhookAdapter())
    webhook.send("再起動、始めました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    await client2.change_presence(activity=discord.Game(name="停止中"))
    await client3.change_presence(activity=discord.Game(name='停止中'))
    await client2.close()
    await client3.close()
async def kabu(type_type,imput,imput2,imput3):
    #ファイル
    #第２階層
    def read_file(ids,category):
        def read_kabu(ids):
            ints = 0
            path = "kabu.txt"
            with open(path) as f:
                dataaa = f.readlines()
                idid = int("0")
            try:
                while idid != ids:
                    text2=[]
                    text = dataaa[ints]
                    text2=text.split("!")
                    text3 = text2[0].split("\n")
                    idid = int(text3[0])
                    ints = ints + 1
            except:
                b = str(ids) 
                c = str(0)
                with open(path, mode='a') as f:
                    a = str("\n"+b + "!" + c)
                    f.write(a)
                return read_kabu(ids)
            return int(text2[1])
        #file_read
        if category == "kabu":
            return read_kabu(ids)
        elif category == "kabuka":#ここからファイル処理
            #株か
            path = "temp.txt"
            with open(path) as f:
                data = f.readlines()
            list0 = data
            if ids == "1mryo":
                #1~0時間前の注文数
                return list0[0]
            elif ids == "2mryo":
                #2~1時間前の注文数
                return list0[1]
            elif ids == "kabuka":
                with open("kabuka.txt", encoding="cp932") as f:
                    data = f.read()
                return data.split("\n")[0]
    def white_file(ids,category,add):
        #white_read
        #書き込み
        def white_files(ids,category,add):
            #white_read
            #流用
            if category == "kabu":
                def read_kabu(ids):#これなんだったけ？
                    ints = 0
                    path = "kabu.txt"
                    with open(path) as f:
                        dataaa = f.readlines()
                        idid = int("0")
                    try:
                        while idid != ids:
                            text2=[]
                            text = dataaa[ints]
                            text2=text.split("!")
                            text3 = text2[0].split("\n")
                            idid = int(text3[0])
                            ints = ints + 1
                    except:
                        b = str(ids) 
                        c = str(0)
                        with open(path, mode='a') as f:
                            a = str("\n"+b + "!" + c)
                            f.write(a)
                        return read_kabu(ids)
                    return int(text2[1])
                money = read_kabu(ids)
                setmoney= int(money) + int(add)
                newdata =str(ids) + "!" + str(setmoney)
                olddata = str(ids) + "!" + str(money)
                file_name = "kabu.txt"
                with open(file_name, encoding="cp932") as f:
                    data_lines = f.read()
                data_lines = data_lines.replace(olddata,newdata)
                with open(file_name, mode="w", encoding="cp932") as f:
                    f.write(data_lines)
        if category == "kabu":
            #所有りょうとか
            white_files(ids,"kabu",add)
            return
        elif category == "kabuka":
            #株価
            def add_temp(add):
                file_name = "temp.txt"
                with open(file_name, encoding="cp932") as f:
                    data_lines = f.readlines()
                olddata = data_lines
                newdata = olddata
                data1 = int(olddata[0]) + int(add)
                newdata = f"{data1}\n{int(olddata[1])}"
                data_lines = data_lines.replace(olddata,newdata)
                with open(file_name, mode="w", encoding="cp932") as f:
                    f.write(data_lines)
            if ids == "1mryo":
                #1~0時間前の注文数
                add_temp(add)
            elif ids == "kabuka":
                #
                path_w = "kabuka.txt"
                with open(path_w) as f:
                    l = f.readlines()
                l.insert(0, f"{ids}\n")
                with open(path_w, mode='w') as f:
                    f.writelines(l)
    def make_glaf():
        #make_glaf
        with open("kabuka.txt", encoding="cp932") as f:
            data = f.read()
        x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        t = data.split("\n")[0:24]
        y = []
        for i in range(24):
            y.append(float(t[23-i]))
        print(y)
        plt.plot(x, y);
        plt.savefig("kabuka.png")
    #最終階層
    #高確率でやらかしそうなので隔離
    if type_type == "buy_sell":
        #buy or sell
        white_file(imput2,"kabu",imput)
        channel = client2.get_channel(698362068746895442)
        siina = float(read_file("kabuka","kabuka")) * imput
        if siina < 0:
            siina = siina / 4 
        await channel.send(f"{imput3}が{imput}株購入しました\n{siina}椎名もちに渡しといてね")
        def add_temp(add):
            file_name = "temp.txt"
            with open(file_name, encoding="cp932") as f:
                data_lines = f.readlines()
            olddata = data_lines
            newdata = olddata
            data1 = int(olddata[0]) + int(add)
            newdata = f"{data1}\n{int(olddata[1])}"
            with open(file_name, mode="w", encoding="cp932") as f:
                f.write(newdata)
        add_temp(imput)
    elif type_type == "time_update":
        tekitou1 = int(read_file("1mryo","kabuka"))-int(read_file("2mryo","kabuka"))
        tekitou2 = random.randint(8,12)/10
        tekitou3 = 0.05 * tekitou1
        numnum = 10 * tekitou2
        num = numnum + tekitou3
        if num < 8:
            num = 8.0
        elif num > 32:
            num = 32.0
        print(num)
        path_w = "kabuka.txt"
        with open(path_w) as f:
            l = f.readlines()
        l.insert(0, f"{num}\n")
        with open(path_w, mode='w') as f:
            f.writelines(l)
        hozon1 = read_file("1mryo","kabuka")
        data = f"0\n{hozon1}"
        with open("temp.txt", mode="w", encoding="cp932") as f:
            f.write(data)
        #update
        make_glaf()
        channel = client2.get_channel(698359379061243994)
        await channel.send(file=discord.File("kabuka.png"))
        await channel.send(f"株価{num}椎名")
        await reboot()
        sys.exit()
    elif type_type == "get":
        #get
        if imput == "kabuka":
            return read_file("kabuka","kabuka")
        elif imput == "kabu":
            return int(read_file(imput2,"kabu"))
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
with open('uuid.json') as f:
    uuid = json.load(f)
@client2.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client2.user.name)
    print(client2.user.id)
    print(client3.user.name)
    print(client3.user.id)
    #print(ext_client.user.name)
    #print(ext_client.user.id)
    print('------')
    loop99.start()
    global start
    stop =time.time()
    result = stop -start
    with open('webhook.json') as f:
        webhook_iroioro = json.load(f)
    webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
    webhook.send(f"再起動が終わりました{result}秒再起動にかかりました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    webhook = Webhook.partial(734666355944718428, webhook_iroioro["token_reboot1"], adapter=RequestsWebhookAdapter())
    webhook.send(f"再起動が終わりました{result}秒再起動にかかりました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
    await client2.change_presence(activity=discord.Game(name="稼働中"))

@client2.event#おめが
async def on_message(message):
    global uuid
    mc=str(message.content)#内容保存
    mn=str(message.author.name)#名前保存
    cid=int(message.channel.id)#チャンネルＩＤ保存
    if message.author.bot:#botはじいてる
        return
    #株システム
    if mc == "/file":
        await message.channel.send(file=discord.File("kabuka.txt"))
        await message.channel.send(file=discord.File("kabu.txt"))
        await message.channel.send(file=discord.File("temp.txt"))
    if mc == "/help":
        await message.channel.send("**help**\n株\n<#698362068746895442>で数字を入力すると買えます\n<#698359379061243994>で株価を発表します")
    if message.content == "/kabu":
        await message.channel.send(await kabu("get","kabu",message.author.id,0))
    if mc == "/time":
        if message.author.id == 690386791831830578 or message.author.id == 672910471279673358:
            await kabu("time_update",0,0,0)
    if cid == 698362068746895442:
        try:
            int_nisuru = int(mc)
            imano_Kabu = await kabu("get","kabu",message.author.id,0)
            if int_nisuru + imano_Kabu < 0:
                await message.channel.send("あははは\n借金はできないよ\nあははは")
                return
            await kabu("buy_sell",int_nisuru,message.author.id,mn)
        except:
            await message.channel.send("数字で入力しろ")
            return
        #注文株 > 持ってる株
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
        await reboot()
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
#よくわからんけど2レジありがとう
#Copyright (c) 2020 disneyresidents
#Released under the MIT license
#https://opensource.org/licenses/mit-license.php
@tasks.loop(seconds=60)
async def loop99():
    global uuid
    now = datetime.datetime.now().strftime("%H:%M")
    if now[3:] == "00":
        await kabu("time_update",0,0,0)
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
        except:
            CHANNEL_ID = 707959412664303616
            channel = client2.get_channel(CHANNEL_ID)
            await channel.send("エラーが発生したんで今日はないです")
    elif now == "23:55":
        await reboot()
        sys.exit()
#2レジありがとう
with open('token.json') as f:
    token = json.load(f)
#keiさんありがとう...
discord_bot_token_2 = token["client2"]
discord_bot_token_3 = token["client3"]
ext_bot_token = token["client1"]
Entry = namedtuple("Entry", "client event token")
entries = [
    Entry(client=client2,event=asyncio.Event(),token=discord_bot_token_2),
    Entry(client=client3,event=asyncio.Event(),token=discord_bot_token_3),
    Entry(client=ext_client,event=asyncio.Event(),token=ext_bot_token),
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
