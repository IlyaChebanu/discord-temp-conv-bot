import discord
import asyncio
import re

client = discord.Client()


@client.event
async def on_ready():
	print('Logged in as', client.user.name, client.user.id, '\n--------')


@client.event
async def on_message(message):
	if message.content.startswith('!conv') and 'C' in message.content:
		try:
			deg = re.findall('\d+', message.content)[0]
			fah = float(deg) * 9/5 + 32
			result = '{:.2f}C = {:.2f}F'.format(float(deg), fah)
			print(result)
			tmp = await client.send_message(message.channel, result)
		except IndexError as e:
			print(e)

	elif message.content.startswith('!conv') and 'F' in message.content:
		try:
			fah = re.findall('\d+', message.content)[0]
			deg = (float(fah) - 32) * 5/9
			result = '{:.2f}F = {:.2f}C'.format(float(fah), deg)
			print(result)
			tmp = await client.send_message(message.channel, result)
		except IndexError as e:
			print(e)


client.run('bot_token')
