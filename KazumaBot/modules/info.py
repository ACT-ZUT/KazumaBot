# -*- coding: utf-8 -*-
import discord
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
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(text)
        return

def setup(client):
    client.add_cog(Info(client, client.config))
