import discord
import asyncio
import re
import random

client = discord.Client()

last_message = ""

@client.event
async def on_ready():
	global last_message
	print('Logged in as', client.user.name, client.user.id, '\n--------')


@client.event
async def on_message(message):
	global last_message
	if message.content.startswith('!conv') and 'C' in message.content:
		try:
			deg = re.findall('-{0,1}\d+', message.content)[0]
			fah = float(deg) * 9/5 + 32
			result = '{:.2f}C = {:.2f}F'.format(float(deg), fah)
			print(result)
			tmp = await client.send_message(message.channel, result)
		except IndexError as e:
			print(e)

	elif message.content.startswith('!conv') and 'F' in message.content:
		try:
			fah = re.findall('-{0,1}\d+', message.content)[0]
			deg = (float(fah) - 32) * 5/9
			result = '{:.2f}F = {:.2f}C'.format(float(fah), deg)
			print(result)
			tmp = await client.send_message(message.channel, result)
		except IndexError as e:
			print(e)

	elif message.content.startswith('!send'):
		tmp = await client.send_message(message.channel, 'nudes')

	elif message.content.startswith('!mock'):
		msg = "".join([c.capitalize() if random.randint(0, 1) == 1 else c for c in last_message])
		tmp = await client.send_message(message.channel, msg)

	else:
		last_message = message.content


client.run('bot_token')
