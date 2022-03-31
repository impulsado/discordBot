#CREATED BY @impulsado
#veneno es antidoto

import discord
from discord import embeds
from discord.colour import Color
from discord.embeds import Embed
from discord.ext import commands
from live import live

client = commands.Bot(command_prefix = '!',help_command=None)

@client.event
async def on_ready():
    print('ON!')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=20):
    await ctx.channel.purge(limit=amount)

@client.command()
async def student(ctx):
    embed = discord.Embed(
        title = 'STUDENT',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/390/PNG/512/rose_38136.png")
    embed.add_field(name='Official',value="I am studying First Year of CiberSecurity CFGS.", inline=False)
    embed.add_field(name='Unofficial',value="I work on projects continuously.", inline=False)
    embed.add_field(name='TryHackMe',value="[LINK](https://tryhackme.com/p/impulsado)",inline=True)
    embed.add_field(name='HackTheBox',value="[ComingSoon](https://app.hackthebox.com/profile/444558)",inline=True)
    embed.set_footer(text="!DM To Know More")
    await ctx.send(embed=embed)

@client.command()
async def artist(ctx):
    embed = discord.Embed(
        title = 'ARTIST',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/569/PNG/512/favourites-black-star-symbol_icon-icons.com_54534.png")
    embed.add_field(name='Social Network',value="I try to recreate the thoughts of an imaginary character.\nCheck out the highlights of my work.", inline=False)
    embed.add_field(name='Music',value="I spend the day listening to music.\nYou can play my playlists.", inline=False)
    embed.add_field(name='Instagram',value="[LINK](https://www.instagram.com/u/impulsado)",inline=True)
    embed.add_field(name='Website',value="[LINK](http://http://impulsado.cf/)",inline=True)
    embed.add_field(name='YT Music',value="[LINK](https://www.youtube.com/channel/UCK2sAQ824p2oAsmr2Cp2-SQ/playlists)",inline=True)
    embed.set_footer(text="!DM To Know More")
    await ctx.send(embed=embed)

@client.command()
async def player(ctx):
    embed = discord.Embed(
        title = 'PLAYER',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/390/PNG/512/rolling-bomb_38138.png")
    embed.add_field(name='Riot',value="I have tried going pro in Valorant.",inline=False)
    embed.add_field(name='Steam',value="I play a lot of games. Check my profile.",inline=False)
    embed.add_field(name='Valorant',value="[LINK](https://tracker.gg/valorant/profile/riot/impu%23CAT/overview)",inline=True)
    embed.add_field(name='Steam',value="[LINK](https://steamcommunity.com/id/impulsado/)",inline=True)
    embed.set_footer(text="!DM To Know More")
    await ctx.send(embed=embed)

@client.command()
async def DM(ctx):
    embed = discord.Embed(
        title = 'CONTACT',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.akamai.steamstatic.com/steamcommunity/public/images/avatars/55/55dbfa8d512b9c3ba84b6ab21bd1c29e574380f2_full.jpg")
    embed.add_field(name='Discord',value="Want to know more? Do not bother to ask.\nI will answer you ASAP.\n",inline=False)
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'HELP',
        color = discord.Color.red()
    )
    embed.set_thumbnail(url="https://cdn.icon-icons.com/icons2/933/PNG/512/settings-cogwheel-button_icon-icons.com_72559.png")
    embed.add_field(name='Information',value="`!student` `!artist` `!player`", inline=False)
    embed.add_field(name='Contact',value="`!DM`", inline=False)
    embed.set_footer(text="!DM To Know More")
    await ctx.send(embed=embed)

live()
client.run('OTA1ODA4Mjg3NjMzNjM3Mzk2.YYPdtA.CGOPG975yeXYtz2T_4QNBLSbIwg')