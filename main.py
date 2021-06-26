import requests, json


def grabmsgs(id):
	rape = open("kriisCantLog.txt", "w+")
	headers = {'authorization' : 'token_here'}
	 # halal put token in there

	penis = requests.get(f'https://discord.com/api/v9/channels/{id}/messages', headers=headers)

	msgs = json.loads(penis.text)
	for value in msgs:
		rape.write(f"[ {value['content']} ]\n")
	print(f"scraped {len(value['content'])} messages")


def cum():
	id = input("daddy put the channel id uwu: ")
	grabmsgs(id)

cum() # halal 
