from discord import Webhook, RequestsWebhookAdapter
import requests,json
with open('webhook.json') as f:
    webhook_iroioro = json.load(f)
webhook = Webhook.partial(734178673162321930, webhook_iroioro["token_reboot"], adapter=RequestsWebhookAdapter())
webhook.send(f"再起動を開始しました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])
webhook = Webhook.partial(734666355944718428, webhook_iroioro["token_reboot1"], adapter=RequestsWebhookAdapter())
webhook.send(f"再起動を開始しました", username='再起動君',avatar_url=webhook_iroioro["avater_reboot"])