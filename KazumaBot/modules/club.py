# -*- coding: utf-8 -*-
import discord, datetime
from discord.ext import commands
import json



class Club:
    """
    Commands about a science club
    """

    def __init__(self, client, config):
        self.client = client
        self.config = config

    @commands.command(name='spotkanie', aliases=['meeting'])
    async def spotkanie(self, ctx):
        """
        Prints how long to the next meeting
        """
        spotkania_raw = config["spotkania"]
        spotkania = []
        for daty in spotkania_raw:
            spotkania.append(datetime.datetime.strptime(daty, '%Y-%m-%dT%H:%M:%S.%fZ'))
        for daty in spotkania:
            timeleft = daty - datetime.datetime.now()
            if(timeleft.days) >= 0:
                break
            else:
                continue

        days = timeleft.days
        hours, remainder = divmod(timeleft.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timeleft_str = "Następne spotkanie za {} dni, {} godzin i {} minut".format(days, hours, minutes)

        embed = discord.Embed()
        embed.add_field(name="Spotkanie", value=timeleft_str)
        embed.set_footer(text="KazumaBot - 2018")
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Club(client, client.config))