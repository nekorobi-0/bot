import requests,json
def ranking():
    resp = requests.get(f'https://w4.minecraftserver.jp/api/ranking?type=break&offset=0&lim=20&duration=daily')
    data_json = json.loads(resp.text)
    rank_list = list(data_json["ranks"])
    msg = "```\n"
    rank = 1
    for mcid_data in rank_list:
        get_mcid = mcid_data["player"]
        get_data = mcid_data["data"]
        seichi_ryo = get_data["raw_data"]
        name = get_mcid["name"]
        seichi_ryo_kugiri0 = str(seichi_ryo)[-4:]
        seichi_ryo_kugiri1 = str(seichi_ryo)[:-4]
        seichi_ryo = seichi_ryo_kugiri1 + "万" + seichi_ryo_kugiri0
        msg += f"{rank}位 {name} 整地量:{seichi_ryo}\n"
        rank += 1
    msg += "```"
    return msg
ranking()