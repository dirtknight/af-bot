#!/usr/bin/env python3

import disnake
from disnake.ext import commands
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()

TOKEN = os.getenv("TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="~~", intents=intents, test_guilds=[int(GUILD_ID)])

@bot.slash_command(
    name="ping",
    description="respond when called",
)
async def ping(inter):
    await inter.response.send_message("pong")

@bot.listen('on_message')
async def on_message(message):
    if message.channel.id != 951635682399494154:
        return

    if message.content == "hi af-test":
        await message.channel.send("hi friend")

    print(message.content)

bot.run(TOKEN)
