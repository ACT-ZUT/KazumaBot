# -*- coding: utf-8 -*-
import discord, datetime
from discord.ext import commands
import json

class Info:
    """
    Info Commands
    """

    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        '''
        Test bot response
        '''
        latency = self.client.latency * 1000 
        text = "Pong! {}ms".format(round(latency, 2))
        embed = discord.Embed()
        embed.add_field(name="Latency test", value=text)
        embed.set_footer(text="KazumaBot v" + self.config["version"])
        await ctx.send(embed=embed)
        

    @commands.command()
    async def uptime(self, ctx):
        '''
        Shows bot uptime
        '''
        current_time = datetime.datetime.now()
        difference = current_time - self.config["start_time"]
        days = difference.days
        hours, remainder = divmod(difference.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        text = "{} dni, {} godzin, {} minut, {} sekund".format(days, hours, minutes, seconds)

        embed = discord.Embed()
        embed.add_field(name="Uptime", value=text)
        embed.set_footer(text="KazumaBot v" + self.config["version"])
        await ctx.send(embed=embed)


    @commands.command()
    async def about(self, ctx):
        '''
        Gives info about the bot
        '''
        embed = discord.Embed(title="About Me", description="", colour=0x1f3A44)
        embed.add_field(name="Creator\'s Discord Name: ", value="SaDiablo#0637", inline=True)
        embed.add_field(name="GitHub repo: ", value="https://github.com/act-zut", inline=True)
        embed.add_field(name="Website: ", value="http://act.zut.edu.pl/", inline=True)
        embed.add_field(name="Build date: ", value=self.config["build_date"], inline=True)
        embed.add_field(name="Bot version: ", value=self.config["version"], inline=True)
        embed.set_footer(text="Made in Python 3.7+ with discord.py@rewrite library!", icon_url='http://findicons.com/files/icons/2804/plex/512/python.png')
        embed.set_author(name=ctx.me.name, icon_url=ctx.me.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client, client.config))