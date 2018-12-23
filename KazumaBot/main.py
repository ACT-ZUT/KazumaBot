#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
import discord, datetime, logging, random, asyncio, aiohttp, json, io, os, sys, re
from time import sleep
#from datetime import *
from discord.ext import commands

# TODO List
# .check command which shows every log info since launch
#

# Checking owner id
def owner_id(ctx):
    return ctx.message.author.id == config["owner_id"]

# Bot initialization
with open('./config.json', 'r') as cjson:
    config = json.load(cjson)
Kazuma = commands.Bot(command_prefix=config["prefix"], owner_id=config["owner_id"])
Kazuma.config = config
Kazuma.config["start_time"] = datetime.datetime.now()

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
    print("Launch time: " + str(config["start_time"]))
    print("Location: " + str(os.path.abspath(__file__)))
    print("----------------------------------------\n")

    print("-----------------------------------------")
    print("Authors: " + config["authors"])
    print("Bot Version: " + config["version"])
    print("Build Date: " + config["build_date"])
    print("Running discord.py version " + discord.__version__)
    print("-----------------------------------------") 

@Kazuma.event
async def on_error(event, *args, **kwargs):
    logging.basicConfig(level=logging.WARNING, filename="error.log", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    logging.error(event + " -> " + str(args) + " " + str(kwargs))

# Bot commands (owner)
@Kazuma.command()
@commands.check(owner_id)
async def kill(ctx):
    """Kill bot"""
    await client.logout()

@Kazuma.command()
@commands.check(owner_id)
async def restart(ctx):
    """Restarts bot"""
    try:
        sleep(1)
        await ctx.message.add_reaction("\u2705")
        os.execv(sys.executable, [sys.executable] +  ['main.py'])
    except:
        await ctx.send("Something went wrong!")
    return

# Bot commands

def ready(client, config):
    for module in config["modules"]:
        try:
            client.load_extension("modules." + module)
        except Exception as e:
            raise Exception(e)

ready(Kazuma, config)
Kazuma.run(config["token"])