#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import discord, datetime, logging, random, asyncio, aiohttp, json, io, os, sys, re
from time import sleep
#from datetime import *
from discord.ext import commands


# Bot initialization
with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
Kazuma = commands.Bot(command_prefix=config["prefix"], owner_id=config["owner_id"])
Kazuma.config = config
modules = config["modules"]
start_time = datetime.datetime.now()

# Bot events
@Kazuma.event
async def on_ready():
    try:
        await Kazuma.change_presence(status=discord.Status.online, 
                                     activity=discord.Game(name=random.choice(config["games"])))
    except:
        await print('Something went wrong!')
    
    print("Finished Loading!\n")
    print("Login Details:")
    print("-----------------------------------------")
    print("Logged in as: " + Kazuma.user.name)
    print("Bot User ID: " + str(Kazuma.user.id))
    print("Launch time: " + str(start_time))
    print("Location: " + str(os.path.abspath(__file__)))
    print("----------------------------------------\n")

    print("-----------------------------------------")
    print("Authors: " + config["authors"])
    print("Bot Version: " + config["version"])
    print("Build Date: " + config["build_date"])
    print("Running discord.py version " + discord.__version__)
    print("-----------------------------------------") 

# Bot commands
@Kazuma.command()
async def uptime(ctx):
    '''
    Shows bot uptime
    '''
    current_time = datetime.datetime.now()
    difference = current_time - start_time
    days = difference.days
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    text = "{} dni, {} godzin, {} minut, {} sekund".format(days, hours, minutes, seconds)

    embed = discord.Embed()
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text="KazumaBot v" + config["version"])
    try:
        await ctx.send(embed=embed)
    except discord.HTTPException:
        await ctx.send("Current uptime: " + text)
    return

def ready(client, config):
    for module in modules:
        try:
            client.load_extension("modules." + module)
        except Exception as e:
            raise Exception(e)
        return

ready(Kazuma, config)
Kazuma.run(config["token"])