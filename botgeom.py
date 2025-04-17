import discord # type: ignore
from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import logging
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord.ui import View, Button

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='bwa', intents=intents)

# Scheduler
scheduler = AsyncIOScheduler()

# Data Notifikasi & Voice
notifications = [
    {"time": "23:45:00", "days": ["tue", "thu", "wed"], "sound": "Kano - 【Rabinva】Stella-rium by Geomacher on Smule- Social Singing Karaoke App_5(2).mp3"},
]
voice_schedule = [
    {"join_time": "23:45:00", "leave_time": "23:50:00", "days": ["tue", "thu", "wed"], "voice_channel_id": 1005098144251527218},
]

# ======================= VOICE FUNCTIONS =========================
async def join_voice_channel(voice_channel_id):
    channel = bot.get_channel(voice_channel_id)
    if channel and isinstance(channel, discord.VoiceChannel):
        if not bot.voice_clients:
            await channel.connect()
            logging.info(f"Bergabung ke voice channel: {channel.name}")

async def leave_voice_channel(voice_channel_id):
    for vc in bot.voice_clients:
        if vc.channel.id == voice_channel_id:
            await vc.disconnect()
            logging.info(f"Keluar dari voice channel: {vc.channel.name}")

async def play_sound(voice_channel_id, sound_file):
    channel = bot.get_channel(voice_channel_id)
    if channel and isinstance(channel, discord.VoiceChannel):
        voice_client = await channel.connect() if not bot.voice_clients else bot.voice_clients[0]
        audio_source = discord.FFmpegPCMAudio(sound_file)
        if not voice_client.is_playing():
            logging.info(f"Memutar: {sound_file} di {channel.name}")
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(1)
            await voice_client.disconnect()

# ======================= RAID REMINDER =========================
async def send_raid_reminder():
    guild = discord.utils.get(bot.guilds)
    if not guild:
        logging.warning("Guild tidak ditemukan.")
        return

    channel = bot.get_channel()
    if not channel:
        logging.warning("Channel tidak ditemukan.")
        return

    role = discord.utils.get(guild.roles, name="`『ＲＩ』")
    if not role:
        logging.warning("Role 『ＲＩ』 tidak ditemukan.")
        return

    msg = f"{role.mention} guys kita raid malam ini jam 21:00 WIB!"
    await channel.send(msg)
    logging.info(f"Pengingat raid dikirim ke {channel.name}")

# ======================= BOT EVENTS =========================
@bot.event
async def on_ready():
    logging.info(f"Bot {bot.user.name} sudah online.")
    scheduler.start()

    # Notifikasi suara
    for notif in notifications:
        h, m, s = map(int, notif["time"].split(":"))
        for day in notif["days"]:
            scheduler.add_job(
                play_sound,
                CronTrigger(day_of_week=day, hour=h, minute=m, second=s),
                args=[1189594050307825756, notif["sound"]]
            )

    # Voice Join/Leave
    for sched in voice_schedule:
        jh, jm, js = map(int, sched["join_time"].split(":"))
        lh, lm, ls = map(int, sched["leave_time"].split(":"))
        for day in sched["days"]:
            scheduler.add_job(join_voice_channel, CronTrigger(day_of_week=day, hour=jh, minute=jm, second=js), args=[sched["voice_channel_id"]])
            scheduler.add_job(leave_voice_channel, CronTrigger(day_of_week=day, hour=lh, minute=lm, second=ls), args=[sched["voice_channel_id"]])

    # Pengingat RAID setiap Sabtu
    for reminder_time in ["11:00", "19:00", "20:00"]:
        h, m = map(int, reminder_time.split(":"))
        scheduler.add_job(
            send_raid_reminder,
            CronTrigger(day_of_week='sat', hour=h-7, minute=m, timezone='UTC')
        )

@bot.event
async def on_error(event, *args, **kwargs):
    logging.exception(f"Error terjadi di event: {event}")


################################################################################################################################




@bot.event
async def on_ready():
    logging.info(f'Bot {bot.user} telah siap.')
    scheduler.start()
    reconnect_task.start()


@tasks.loop(seconds=60)
async def reconnect_task():
    if not bot.is_closed():
        logging.info('Bot masih terhubung dan berjalan dengan baik.')
    else:
        logging.warning('Bot terputus, mencoba untuk reconnect...')
        try:
            await bot.connect(reconnect=True)
            logging.info('Bot berhasil reconnect.')
        except Exception as e:
            logging.error(f'Reconnect gagal: {e}')
            await asyncio.sleep(5)

@bot.event
async def on_disconnect():
    logging.warning('Bot terputus, mencoba untuk reconnect...')
#######################################################
             #COMMAND#
###################################################
@bot.command(name='commands', aliases=['helpme'])
async def show_commands(ctx):
    embed = discord.Embed(title='Command List', description='Berikut daftar command yang tersedia:', color=0x00ff00)
    embed.add_field(name='bwanamabossmq', value='Contoh: `bwabossroga` - Menampilkan detail tentang boss.', inline=False)
    embed.add_field(name='bwaxnamaboss', value='Contoh: `bwaxbossroga` - Menampilkan stat xtall boss yang diinginkan.', inline=False)
    embed.add_field(name='bwastatbuffland', value='Contoh: `bwastr` - Menampilkan code room untuk buff yang dicari.', inline=False)
    embed.add_field(name='bwaconsumbuff', value='Contoh: `bwaconsumhp` - Menampilkan list consum buff.', inline=False)
    embed.add_field(name='bwalevel', value='Contoh: `bwa250` - Menampilkan list boss untuk leveling di level yang diinginkan.', inline=False)
    embed.add_field(name='bwaelearrow', value='Contoh: `bwafirearrow` - Menampilkan list ele arrow yang diinginkan dan lokasi dropnya.', inline=False)
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')
    await ctx.send(embed=embed)



@bot.command(name='consumbuff', aliases=['consumebuff'])
async def show_commandsconsumbuff(ctx):
    embed = discord.Embed(title='bwaconsumbuff', description='Berikut daftar command yang tersedia:', color=0x00ff00)
    embed.add_field(name='1', value='Contoh: `bwaconsumhp` - Menampilkan list consum buff hp.', inline=False)
    embed.add_field(name='2', value='Contoh: `bwaconsummp` - Menampilkan list consum buff mp.', inline=False)
    embed.add_field(name='3', value='Contoh: `bwaconsumaspd` - Menampilkan list consum buff aspd.', inline=False)
    embed.add_field(name='4', value='Contoh: `bwaconsumcspd` - Menampilkan list consum buff cspd.', inline=False)
    embed.add_field(name='5', value='Contoh: `bwaconsumail` - Menampilkan list consum buff ailement.', inline=False)
    embed.add_field(name='6', value='Contoh: `bwaconsumacc` - Menampilkan list consum buff acc.', inline=False)
    embed.add_field(name='7', value='Contoh: `bwaconsumresis` - Menampilkan list consum buff resis.', inline=False)
    embed.add_field(name='8', value='Contoh: `bwaconsumele` - Menampilkan list consum buff element.', inline=False)
    embed.add_field(name='9', value='Contoh: `bwaconsumflee` - Menampilkan list consum buff dodge.', inline=False)
    embed.add_field(name='10', value='Contoh: `bwaconsumatk` - Menampilkan list consum buff atk.', inline=False)
    embed.add_field(name='11', value='Contoh: `bwaconsummatk` - Menampilkan list consum buff m atk.', inline=False)
    embed.add_field(name='12', value='Contoh: `bwaconsumdef` - Menampilkan list consum buff def.', inline=False)
    embed.add_field(name='13', value='Contoh: `bwaconsummdef` - Menampilkan list consum buff mdef.', inline=False)
    embed.add_field(name='14', value='Contoh: `bwaconsumhprecovery` - Menampilkan list consum buff hp recovery.', inline=False)
    embed.add_field(name='15', value='Contoh: `bwaconsummprecovery` - Menampilkan list consum buff mp recovery.', inline=False)
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')
    await ctx.send(embed=embed)

################# MQ BAB 1 #####################################################
@bot.command(name='bosscolon')
async def bosscolon(ctx):
    embed = discord.Embed(title='Boss Colon')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Land Under Development')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='1000', inline=True)
    embed.add_field(name='Base EXP', value='3000', inline=True)
    embed.add_field(name='P.Def', value='7', inline=True)
    embed.add_field(name='M.Def', value='7', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='11', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_footer(text='EASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='bossroga')
async def bossroga(ctx):
    embed = discord.Embed(title='Boss Roga')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Saham Underground Cave - Deepest Part')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='250.000', inline=True)
    embed.add_field(name='Base EXP', value='3000', inline=True)
    embed.add_field(name='P.Def', value='62\nFTS 186', inline=True)
    embed.add_field(name='M.Def', value='62\nFTS 186', inline=True)
    embed.add_field(name='P.Res', value='2\nFTS 27', inline=True)
    embed.add_field(name='M.Res', value='2\nFTS 27', inline=True)
    embed.add_field(name='Prorate', value='N:15 P:10 M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='279\nFTS 93\n\n', inline=True)
    embed.add_field(name='Retaliation', value='FTS: The bosss defenses and resistances significantly increase for a\nperiod of time (~15 seconds). The boss attack power is also\nreduced during this duration.\n\n', inline=False)
    embed.set_image(url='https://aminoapps.com/c/toram_online/page/item/boss-colon/Rrnm_MgvTvIjXm8dZmklLWwkNg8M7Rk3nW')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='excavatedgolem')
async def excavatedgolem(ctx):
    embed = discord.Embed(title='Excavated Golem')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Underground Ruins: Deepest Part')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='3150', inline=True)
    embed.add_field(name='Base EXP', value='90', inline=True)
    embed.add_field(name='P.Def', value='12', inline=True)
    embed.add_field(name='M.Def', value='12', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:15  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='12', inline=True)
    embed.add_field(name='Retaliation', value='None\n\nNote : Breaking the parts will reduce the boss defenses by 100%', inline=False)
    embed.set_image(url='https://www.google.com/imgres?q=excavated%20golem%20toram&imgurl=http%3A%2F%2Fpm1.aminoapps.com%2F6694%2Fad4abbd36f9ccd84df9ab1b9e7139bd94dc18712_00.jpg&imgrefurl=https%3A%2F%2Faminoapps.com%2Fc%2Ftoram_online%2Fpage%2Fitem%2Fexcavated-golem%2F6PzK_pYniYIKlvb8mjJ5VallKPNBZB4Ez0q&docid=sKPcKSBgJ09qpM&tbnid=KDGFcqtn02HURM&vet=12ahUKEwjGu8G38sSMAxWbTmwGHSbbHmwQM3oECGoQAA..i&w=512&h=397&hcb=2&ved=2ahUKEwjGu8G38sSMAxWbTmwGHSbbHmwQM3oECGoQAA')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='eeiriecrystal')
async def eeiriecrystal(ctx):
    embed = discord.Embed(title='Eeirie Crystal')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Isthmus Of Kaus: Dragons Den')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='6.300', inline=True)
    embed.add_field(name='Base EXP', value='225', inline=True)
    embed.add_field(name='P.Def', value='0', inline=True)
    embed.add_field(name='M.Def', value='0', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='0', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='https://toram.fandom.com/wiki/Eerie_Crystal')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='minotaur')
async def minotaur(ctx):
    embed = discord.Embed(title='Minotaur')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Ruined Temple: Forbidden hall')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='18.000', inline=True)
    embed.add_field(name='Base EXP', value='420', inline=True)
    embed.add_field(name='P.Def', value='32', inline=True)
    embed.add_field(name='M.Def', value='32', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='48', inline=True)
    embed.add_field(name='Retaliation', value='When the boss HP reaches below 20% the boss will gain 100% guard rate for 10 seconds\nand perform three long-range rush attacks that inflict ignite\n\n', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='brutaldragondecel')
async def brutaldragondecel(ctx):
    embed = discord.Embed(title='Brutal Dragon Decel')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Nisel Mountain: The Top')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='53.000', inline=True)
    embed.add_field(name='Base EXP', value='560', inline=True)
    embed.add_field(name='P.Def', value='20', inline=True)
    embed.add_field(name='M.Def', value='20', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:20  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='75', inline=True)
    embed.add_field(name='Retaliation', value='T : Guard rate up for 12 seconds\n', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='warmonger')
async def warmonger(ctx):
    embed = discord.Embed(title='Warmonger')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Haotas Ravine: Deepest Part')
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='147.690', inline=True)
    embed.add_field(name='Base EXP', value='960', inline=True)
    embed.add_field(name='P.Def', value='60', inline=True)
    embed.add_field(name='M.Def', value='60', inline=True)
    embed.add_field(name='P.Res', value='2', inline=True)
    embed.add_field(name='M.Res', value='2', inline=True)
    embed.add_field(name='Prorate', value='N:150  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='45', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='forestia')
async def forestia(ctx):
    embed = discord.Embed(title='Forestia')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Land Of Chaos')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='135.000', inline=True)
    embed.add_field(name='Base EXP', value='1480', inline=True)
    embed.add_field(name='P.Def', value='24', inline=True)
    embed.add_field(name='M.Def', value='24', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='292', inline=True)
    embed.add_field(name='Retaliation', value='The players can fall off the stages cliffs.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='ancientempress')
async def ancientempress(ctx):
    embed = discord.Embed(title='Ancient Empress')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='Yes (Area Lock)', inline=True)
    embed.add_field(name='Map', value='Ancient Empress Tomb: Deepest Part')
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='130.000', inline=True)
    embed.add_field(name='Base EXP', value='3.120', inline=True)
    embed.add_field(name='P.Def', value='32', inline=True)
    embed.add_field(name='M.Def', value='32', inline=True)
    embed.add_field(name='P.Res', value='52', inline=True)
    embed.add_field(name='M.Res', value='52', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='48', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='flarevolg')
async def flarevolg(ctx):
    embed = discord.Embed(title='Flare Volg')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Fiery Volcano: Boss Map')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='120.000', inline=True)
    embed.add_field(name='Base EXP', value='1.500', inline=True)
    embed.add_field(name='P.Def', value='Ph1:100|Ph2:62', inline=True)
    embed.add_field(name='M.Def', value='Ph1:100|Ph2:62', inline=True)
    embed.add_field(name='P.Res', value='28', inline=True)
    embed.add_field(name='M.Res', value='28', inline=True)
    embed.add_field(name='Prorate', value='N:6  P:25  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='56', inline=True)
    embed.add_field(name='Retaliation', value='The boss switches to PH2 at 50% HP.\n\nNote : Breaking parts reduces the boss DEF and MDEF by 25%.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='ganglef')
async def ganglef(ctx):
    embed = discord.Embed(title='Ganglef')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='Yes (Area Lock)', inline=True)
    embed.add_field(name='Map', value='Scaro Town: Deepest Part')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='107.800', inline=True)
    embed.add_field(name='Base EXP', value='1.150', inline=True)
    embed.add_field(name='P.Def', value='232', inline=True)
    embed.add_field(name='M.Def', value='58', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='25', inline=True)
    embed.add_field(name='Prorate', value='N:6  P:25  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='43', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='gespenst')
async def gespenst(ctx):
    embed = discord.Embed(title='Gespenst')
    embed.add_field(name='Map', value='Underground Channel')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='8.544', inline=True)
    embed.add_field(name='Base EXP', value='240', inline=True)
    embed.add_field(name='P.Def', value='26', inline=True)
    embed.add_field(name='M.Def', value='50', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:20  P:25  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='30', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='forestwolf')
async def forestwolf(ctx):
    embed = discord.Embed(title='Forest Wolf')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Marbaro Forest: Deepest Part')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='16.038', inline=True)
    embed.add_field(name='Base EXP', value='300', inline=True)
    embed.add_field(name='P.Def', value='30', inline=True)
    embed.add_field(name='M.Def', value='30', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:8  P:20  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='45', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='bossgoblin')
async def bossgoblin(ctx):
    embed = discord.Embed(title='Boss Goblin')
    embed.add_field(name='MQ Chapter', value='1', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Ribisco Cave: Deepest Part')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='26.758', inline=True)
    embed.add_field(name='Base EXP', value='560', inline=True)
    embed.add_field(name='P.Def', value='30', inline=True)
    embed.add_field(name='M.Def', value='30', inline=True)
    embed.add_field(name='P.Res', value='0', inline=True)
    embed.add_field(name='M.Res', value='0', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='75', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='mochelo')
async def mochelo(ctx):
    embed = discord.Embed(title='Mochelo')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Fiery Volcano: Area 3')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='60.000', inline=True)
    embed.add_field(name='Base EXP', value='620', inline=True)
    embed.add_field(name='P.Def', value='0', inline=True)
    embed.add_field(name='M.Def', value='0', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:3  P:50  M:50', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='64', inline=True)
    embed.add_field(name='Retaliation', value='None.\nThe boss attack power decreases at 50% HP and at 25% HP.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='ooze')
async def ooze(ctx):
    embed = discord.Embed(title='Ooze')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Lutaros Cavern: Deepest Part')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='44.000', inline=True)
    embed.add_field(name='Base EXP', value='1.400', inline=True)
    embed.add_field(name='P.Def', value='78', inline=True)
    embed.add_field(name='M.Def', value='78', inline=True)
    embed.add_field(name='P.Res', value='12', inline=True)
    embed.add_field(name='M.Res', value='12', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='0', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='mauez')
async def mauez(ctx):
    embed = discord.Embed(title='Mauez')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Lutaros Cavern: Deepest Part')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='86.000', inline=True)
    embed.add_field(name='Base EXP', value='1.290', inline=True)
    embed.add_field(name='P.Def', value='PH1: 165 | PH2 : 28', inline=True)
    embed.add_field(name='M.Def', value='PH1: 165 | PH2 : 28', inline=True)
    embed.add_field(name='P.Res', value='7', inline=True)
    embed.add_field(name='M.Res', value='7', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1 : 41 | PH2 : 246', inline=True)
    embed.add_field(name='Retaliation', value='The boss switches to PH2 at 50% HP.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='demonsgate')
async def demonsgate(ctx):
    embed = discord.Embed(title='Demons Gate')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Saham Crater')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='18.000', inline=True)
    embed.add_field(name='Base EXP', value='1.440', inline=True)
    embed.add_field(name='P.Def', value='180', inline=True)
    embed.add_field(name='M.Def', value='180', inline=True)
    embed.add_field(name='P.Res', value='N:165 | F:28', inline=True)
    embed.add_field(name='M.Res', value='N:165 | F:28', inline=True)
    embed.add_field(name='Prorate', value='N:150  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='0', inline=True)
    embed.add_field(name='Retaliation', value='F: Guard rate up for 15 seconds', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='astol')
async def astol(ctx):
    embed = discord.Embed(title='Astol')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Aulada Ancient Tower')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='82.040', inline=True)
    embed.add_field(name='Base EXP', value='760', inline=True)
    embed.add_field(name='P.Def', value='50', inline=True)
    embed.add_field(name='M.Def', value='150', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:6  P:25  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='112', inline=True)
    embed.add_field(name='Retaliation', value='TS: The boss will perform a delayed straight-line counter attack. Due to the delayed nature of this attack, TS is actually safe to use.\n\nNote: You can easily break this boss\'s head by interrupting it while it is slowly flying towards you with its body parallel to the ground.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='ruingolem')
async def ruingolem(ctx):
    embed = discord.Embed(title='Ruin Golem')
    embed.add_field(name='MQ Chapter', value='2', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Zoktzda Ruins: Reversed Hall')
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='41.200', inline=True)
    embed.add_field(name='Base EXP', value='660', inline=True)
    embed.add_field(name='P.Def', value='106', inline=True)
    embed.add_field(name='M.Def', value='106', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:15  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='14', inline=True)
    embed.add_field(name='Retaliation', value='Support mobs will spawn every 20 seconds\n\nNote: Breaking parts reduces the boss DEF and MDEF by 23.8%.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='maskedwarrior')
async def maskedwarrior(ctx):
    embed = discord.Embed(title='Masked Warrior')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Land Under Cultivation: Hill')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='276.000', inline=True)
    embed.add_field(name='Base EXP', value='4.300', inline=True)
    embed.add_field(name='P.Def', value='134', inline=True)
    embed.add_field(name='M.Def', value='134', inline=True)
    embed.add_field(name='P.Res', value='2', inline=True)
    embed.add_field(name='M.Res', value='2', inline=True)
    embed.add_field(name='Prorate', value='N:6  P:25  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='200', inline=True)
    embed.add_field(name='Retaliation', value='None.\n\nNote: Breaking parts will increase the boss movement speed.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='pillargolem')
async def pillargolem(ctx):
    embed = discord.Embed(title='Pillar Golem')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Lost Town: Magic Barrier')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='324.000', inline=True)
    embed.add_field(name='Base EXP', value='3.600', inline=True)
    embed.add_field(name='P.Def', value='140', inline=True)
    embed.add_field(name='M.Def', value='140', inline=True)
    embed.add_field(name='P.Res', value='2', inline=True)
    embed.add_field(name='M.Res', value='2', inline=True)
    embed.add_field(name='Prorate', value='N:3  P:50  M:50', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='11', inline=True)
    embed.add_field(name='Retaliation', value='FT: If inflicted when the boss is Yellow, the boss will turn Red and become enraged (EN) for 10 seconds. While in enraged mode, the boss defenses and attack power are significantly increased and the boss does not retaliate to FTS.\nInflicting F to the boss while it is Yellow will also cause the boss to attack with a foe-centered AOE ground pound.\n\nNote: Breaking parts lowers the boss movement speed', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='yelb')
async def yelb(ctx):
    embed = discord.Embed(title='Grass Dragon Yelb')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Albatif Village')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='439.190', inline=True)
    embed.add_field(name='Base EXP', value='5.040', inline=True)
    embed.add_field(name='P.Def', value='N: 146 | SHELL: 1022', inline=True)
    embed.add_field(name='M.Def', value='N: 146 | SHELL: 657', inline=True)
    embed.add_field(name='P.Res', value='N: 2 | SHELL: 22', inline=True)
    embed.add_field(name='M.Res', value='N: 2 | SHELL: 2', inline=True)
    embed.add_field(name='Prorate', value='N:3  P:50  M:50', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='87', inline=True)
    embed.add_field(name='Retaliation', value='SLOW/STOP/IGNITE: When the boss receives a Slow or Stop ailment during normal mode, it will change to enraged mode for 30 sec and then go back to normal mode. While in enraged mode, the boss defenses are halved and the boss movement speed increases.\nDAMAGE: When the boss receives damage higher than 3% of its health in one instance, it will go into enraged mode and shell mode\n(SHELL) at the same time for 30 sec. While in shell mode, the bosses defenses increase by a lot.\nPARA/ARMORBREAK: Removes the boss shell mode and returns the defenses to normal. The boss will retaliate with a low damage, full-map AOE attack that inflicts paralysis if inflicted with Armor Break or Paralysis while in shell mode.\nWhile the boss is in enraged mode, it will perform full-map AOE attacks periodically. All of these full-map AOE attacks inflict ailments.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='nurethoth')
async def nurethoth(ctx):
    embed = discord.Embed(title='Nurethoth')
    embed.add_field(name='MQ Chapter', value='3', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Gate to Another World: Front')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='500.000', inline=True)
    embed.add_field(name='Base EXP', value='5.360', inline=True)
    embed.add_field(name='P.Def', value='PH1 : 152 | PH2 : 76', inline=True)
    embed.add_field(name='M.Def', value='PH1 : 152 | PH2 : 76', inline=True)
    embed.add_field(name='P.Res', value='PH1 : 23 | PH2 : 3', inline=True)
    embed.add_field(name='M.Res', value='PH1 : 23 | PH2 : 3', inline=True)
    embed.add_field(name='Prorate', value='N:75  P:2  M:2', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1 : 57 | PH2 : 285', inline=True)
    embed.add_field(name='Retaliation', value='FTS: If inflicted above 50% HP, the boss will retaliate with a high damage AOE that: flinches (if the boss was flinched), tumbles (if the boss was tumbled), or stuns (if the boss was stunned).\n\nThe boss switches to PH2 at 50% HP.', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='b.b.goblin')
async def bbgoblin(ctx):
    embed = discord.Embed(title='B.B. Goblin')
    embed.add_field(name='Map', value='Rinom Plains')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='24.331', inline=True)
    embed.add_field(name='Base EXP', value='2.400', inline=True)
    embed.add_field(name='P.Def', value='140', inline=True)
    embed.add_field(name='M.Def', value='210', inline=True)
    embed.add_field(name='P.Res', value='1', inline=True)
    embed.add_field(name='M.Res', value='1', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='157', inline=True)
    embed.add_field(name='Retaliation', value='None', inline=False)
    embed.set_image(url='')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='goovua')
async def goovua(ctx):
    embed = discord.Embed(title='Goovua')
    embed.add_field(name='MQ Chapter', value='4', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Akaku Desert: Hill')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='400.000', inline=True)
    embed.add_field(name='Base EXP', value='500.000', inline=True)
    embed.add_field(name='P.Def', value='PH1: 41\nPH2: 57\nPH3: 82\nLHP: 0', inline=True)
    embed.add_field(name='M.Def', value='PH1: 41\nPH2: 57\nPH3: 82\nLHP: 0', inline=True)
    embed.add_field(name='P.Res', value='3', inline=True)
    embed.add_field(name='M.Res', value='3', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 246 | PH2: 273 | PH3: 308 | LPH: 0', inline=True)
    embed.add_field(name='Retaliation', value='The boss switches to PH2 30 seconds after initiating the battle. Similarly, the boss switches to PH3 30 seconds after switching to PH2. When the boss HP goes below 20%, the boss enters the LHP phase. During the LHP phase, the boss defenses are zero and the boss nonfractional damage to players is increased by approximately 10 times.', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/goovua.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='scrader')
async def scrader(ctx):
    embed = discord.Embed(title='Scrader')
    embed.add_field(name='MQ Chapter', value='4', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Magic Waste Site: Deepest Part')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='660.000', inline=True)
    embed.add_field(name='Base EXP', value='7.900', inline=True)
    embed.add_field(name='P.Def', value='255', inline=True)
    embed.add_field(name='M.Def', value='255', inline=True)
    embed.add_field(name='P.Res', value='3', inline=True)
    embed.add_field(name='M.Res', value='3', inline=True)
    embed.add_field(name='Prorate', value='N:150  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='64', inline=True)
    embed.add_field(name='Retaliation', value='Dealing damage above 2% of its max HP in one instance will cause the boss to go into rage mode (Red color) for 20 seconds. While in rage mode, the boss ATK and MATK increase.', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/scrader.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='bkod')
async def bkod(ctx):
    embed = discord.Embed(title='Black Knight Of Delusion')
    embed.add_field(name='MQ Chapter', value='4', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Abyss of No Return: Deepest Area')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='540.000', inline=True)
    embed.add_field(name='Base EXP', value='6.600', inline=True)
    embed.add_field(name='P.Def', value='176', inline=True)
    embed.add_field(name='M.Def', value='176', inline=True)
    embed.add_field(name='P.Res', value='PH1:23\nPH2:33', inline=True)
    embed.add_field(name='M.Res', value='PH1:23\nPH2:33', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:30  M:30', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='231', inline=True)
    embed.add_field(name='Retaliation', value='TS: Boss backs away to the left (PH1) or to the right (PH2) if inflicted.\n\nThe boss switches from PH1 to PH2 at 50% HP.', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/bkod.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='ecb')
async def ecb(ctx):
    embed = discord.Embed(title='Evil Crystal Beast')
    embed.add_field(name='MQ Chapter', value='4', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Lunagent Mountain: Deepest Area')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='530.000', inline=True)
    embed.add_field(name='Base EXP', value='6.300', inline=True)
    embed.add_field(name='P.Def', value='PH1: 274; PH2: 165', inline=True)
    embed.add_field(name='M.Def', value='PH1: 274; PH2: 165', inline=True)
    embed.add_field(name='P.Res', value='3', inline=True)
    embed.add_field(name='M.Res', value='3', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:30  M:30', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='231', inline=True)
    embed.add_field(name='Retaliation', value="FS: 100% guard rate for 10 sec if inflicted during PH1 (Purple).\nFTS: 100% evasion rate for 10 sec if inflicted during PH2 (Red).\n\nWhen the boss's HP goes below 25%, the boss turns Red and switches to PH2.\nWhen the boss receives damage that is greater than 3% of its max HP, the boss's guard rate (PH1) or evasion rate (PH2) will increase to 100% for 10 sec.", inline=False)
    embed.add_field(name='Parts Destruction:', value='2 Parts: Left Hand (Evil Crystal Beast Claw, ARM), Chest (ADD)', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/ecb.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='cerberus')
async def cerberus(ctx):
    embed = discord.Embed(title='Cerberus')
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Spring of Rebirth: Top')
    embed.add_field(name='Element', value='BLUE: Water; RED: Fire; YELLOW: Wind; White: Neutral', inline=True)
    embed.add_field(name='Base HP', value='800.000', inline=True)
    embed.add_field(name='Base EXP', value='9.200', inline=True)
    embed.add_field(name='P.Def', value='N: 146; F: 970; T: 49; S: 97; LHP: 194', inline=True)
    embed.add_field(name='M.Def', value='N: 146; F: 970; T: 49; S: 97; LHP: 194', inline=True)
    embed.add_field(name='P.Res', value='N: 3; F: 50; T: 3; S: -5; LHP: 10', inline=True)
    embed.add_field(name='M.Res', value='N: 3; F: 50; T: 3; S: -5; LHP: 10', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:20  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='145', inline=True)
    embed.add_field(name='Retaliation', value="F: Boss switches color to red (Fire element). In this state, the boss's def and physical resistance significantly increase, while\nits mdef and magical resistance significantly decrease\n T: Boss switches color to red (Fire element). In this state, the boss's mdef and magical resistance significantly increase, while\n its def and physical resistance significantly decrease.S: Boss switches color to yellow (Wind element) which decreases both its def/mdef and pres/mres.\n\nAfter 30 seconds of switching to red (Fire element) or yellow (Wind element), the boss will revert back to blue (Water element).\nWhen HP reaches below 25%, the boss switches color to white (Neutral element). From this point on, the boss can be FTS without any retaliation.TIPS: The non-tank party members should be aware of the tank's position at all times. This is a precaution just in case the boss performs the whole map, player-centered AOE, where the safe spot is at the tank's location.", inline=False)
    embed.add_field(name='Parts Destruction:', value='3 Parts:Head (Cerberus Head Crystal)\nLeft Shoulder\nRight Shoulder', inline=False)
    embed.set_image(url='https://images-ext-1.discordapp.net/external/VY4FHnY-iQO8QoAmABnVDMBDSaYEDPQAvymz2CcW5Cs/https/raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/cerberus.png?quality=lossless&format=webp&width=540&height=270')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='zolban', aliases=['zol'])
async def zolban(ctx):
    embed = discord.Embed(title='Zolban')
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Dark Mirror')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='244.000', inline=True)
    embed.add_field(name='Base EXP', value='3.900', inline=True)
    embed.add_field(name='P.Def', value='196', inline=True)
    embed.add_field(name='M.Def', value='382', inline=True)
    embed.add_field(name='P.Res', value='3', inline=True)
    embed.add_field(name='M.Res', value='3', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='145', inline=True)
    embed.add_field(name='Retaliation', value="S: Retaliates with a foe-centered, fractional spikes AOE that inflicts Stop.\nT: Boss moves away", inline=False)
    embed.add_field(name='Parts Destruction:', value='2 Parts:\nBack/Crystal Wings (Magic Crystal Wing Fragment)\nTorso', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/zolban.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='aranea', aliases=['ara'])
async def aranea(ctx):
    embed = discord.Embed(title='Aranea')
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Garden of Sublimation: Central')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='380.000', inline=True)
    embed.add_field(name='Base EXP', value='4.400', inline=True)
    embed.add_field(name='P.Def', value='PH1: 130; PH2: 120', inline=True)
    embed.add_field(name='M.Def', value='PH1: 110; PH2: 100', inline=True)
    embed.add_field(name='P.Res', value='4', inline=True)
    embed.add_field(name='M.Res', value='4', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:20  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 300; PH2: 375', inline=True)
    embed.add_field(name='Retaliation', value="None", inline=False)
    embed.add_field(name='Parts Destruction:', value='3 Parts:\nUpper Right Leg (HB),\nTorso (MD),\nLower Left Leg (Crystal Spider Leg Shell)', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/aranea.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

@bot.command(name='bexiz', aliases=['bex'])
async def bexiz(ctx):
    embed = discord.Embed(title='Bexiz')
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='Yes(Area Lock)', inline=True)
    embed.add_field(name='Map', value='Cradle of Soldier: Deepest Part')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='645.000', inline=True)
    embed.add_field(name='Base EXP', value='7.610', inline=True)
    embed.add_field(name='P.Def', value='216', inline=True)
    embed.add_field(name='M.Def', value='247', inline=True)
    embed.add_field(name='P.Res', value='4', inline=True)
    embed.add_field(name='M.Res', value='4', inline=True)
    embed.add_field(name='Prorate', value='N:35  P:40  M:50', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='123', inline=True)
    embed.add_field(name='Retaliation', value="TS: The boss does not stop when interrupted by TS. Instead, it immediately moves on to the next attack pattern.\nIf the boss does not receive damage for 10 seconds, the boss will start healing itself until the next damage is inflicted.", inline=False)
    embed.add_field(name='Parts Destruction:', value='3 Parts: Right Arm, Left Arm, Right Leg (Broken Floating Stone)', inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/bexiz.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='imitator', aliases=['tator'])
async def imitator(ctx):
    embed = discord.Embed(title='Imitator')
    embed.add_field(name='Level Boss', value='Normal : 106', inline=True)
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Plastida: Deepest Part')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='780.000', inline=True)
    embed.add_field(name='Base EXP', value='8.700', inline=True)
    embed.add_field(name='P.Def', value='371', inline=True)
    embed.add_field(name='M.Def', value='392', inline=True)
    embed.add_field(name='P.Res', value='20', inline=True)
    embed.add_field(name='M.Res', value='20', inline=True)
    embed.add_field(name='Prorate', value='N:35  P:35  M:30', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='238', inline=True)
    embed.add_field(name='Retaliation', value="FTS: Retaliates with a wide AOE attack if inflicted below 40% HP.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Fake General's Helm),\nRight Arm (OHS),\nLeft Leg (SHIELD)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/imitator.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='imitacia', aliases=['imit'])
async def imitacia(ctx):
    embed = discord.Embed(title='Imitacia')
    embed.add_field(name='Level Boss', value='Normal : 109', inline=True)
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Dark Castle: Grand Hall')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='780.000', inline=True)
    embed.add_field(name='Base EXP', value='8.700', inline=True)
    embed.add_field(name='P.Def', value='PH1: 164; FROZ: 33; PH2: 55', inline=True)
    embed.add_field(name='M.Def', value='PH1: 218; FROZ: 33; PH2: 109', inline=True)
    embed.add_field(name='P.Res', value='PH1: 35; FROZ: 10; PH2: 4', inline=True)
    embed.add_field(name='M.Res', value='PH1: 35; FROZ: 10; PH2: 4', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:35  M:40', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 302; FROZ: 163; PH2: 489', inline=True)
    embed.add_field(name='Retaliation', value="TS: Retaliates with a 16m radius, foe-centered AOE that inflicts sleep ailment if inflicted at 30% - 100% HP.\nF: Retaliates with a 16m radius, foe-centered AOE that inflicts sleep ailment if inflicted below 30% HP.\nFREEZE: lowers def/mdef for a short amount of time.", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nRight Wing (ARM),\nLeft Coat Feather/Neck (Copied Goddess's Robe)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/imitacia.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

############################## MAIN QUEST BAB 6 ###########################################

@bot.command(name='inzanio', aliases=['inza'])
async def inzanio(ctx):
    embed = discord.Embed(title='Inzanio the Dark Knight')
    embed.add_field(name='Level Boss', value='Normal : 94', inline=True)
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Fort Solfini: Roof')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='489.000', inline=True)
    embed.add_field(name='Base EXP', value='5.500', inline=True)
    embed.add_field(name='P.Def', value='PH1: 212; PH2: 263', inline=True)
    embed.add_field(name='M.Def', value='PH1: 188; PH2: 235', inline=True)
    embed.add_field(name='P.Res', value='3', inline=True)
    embed.add_field(name='M.Res', value='3', inline=True)
    embed.add_field(name='Prorate', value='N:4  P:35  M:35', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='176', inline=True)
    embed.add_field(name='Retaliation', value="FTS: Increases guard rate for 10 seconds;Below 50% HP, the boss will turn blue and will gain 100% evasion rate for a short period of time. During this time, the boss will cast a full map AOE meteor that drops after 2 minutes.", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nSpear (Cracked Magic Spear),\nHelmet (ADD)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/inzaniothedarkknight.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='iconos', aliases=['ico'])
async def iconos(ctx):
    embed = discord.Embed(title='Iconos')
    embed.add_field(name='Level Boss', value='Normal : 108', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Artillery Defense Line')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='404.000', inline=True)
    embed.add_field(name='Base EXP', value='4.200', inline=True)
    embed.add_field(name='P.Def', value='PH1: 162; PH2: 216;\nPH3: 270; PH4: 324', inline=True)
    embed.add_field(name='M.Def', value='PH1: 140; PH2: 194;\nPH3: 248; PH4: 302', inline=True)
    embed.add_field(name='P.Res', value='PH1: 10; PH2: 15;\nPH3: 20; PH4: 25', inline=True)
    embed.add_field(name='M.Res', value='PH1: 10; PH2: 15;\nPH3: 20; PH4: 25', inline=True)
    embed.add_field(name='Prorate', value='N:  P:  M:', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='162', inline=True)
    embed.add_field(name='Retaliation', value="F: If inflicted above 50% HP, the boss's guard rate becomes 100%;\nT: If inflicted below 50% HP, the boss's guard rate becomes 100%.\nThe boss's defenses and resistances increase every time its HP decreases by 25% (PH1 to PH4).", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTorso/Core (Iconos Core),\nLeft Arm (THS),\nRight Leg (KN)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/iconos.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='twilightdragon', aliases=['twilight'])
async def twilightdragon(ctx):
    embed = discord.Embed(title='Twilight Dragon')
    embed.add_field(name='Level Boss', value='Normal : 100', inline=True)
    embed.add_field(name='MQ Chapter', value='5', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Fort Solfini: Roof')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='695.000', inline=True)
    embed.add_field(name='Base EXP', value='8000', inline=True)
    embed.add_field(name='P.Def', value='PH1: 180; PH2: 230', inline=True)
    embed.add_field(name='M.Def', value='PH1: 260; PH2: 300', inline=True)
    embed.add_field(name='P.Res', value='4', inline=True)
    embed.add_field(name='M.Res', value='4', inline=True)
    embed.add_field(name='Prorate', value='N:8  P:20  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 240; PH2: 255', inline=True)
    embed.add_field(name='Retaliation', value="F: Boss will teleport and launch a high-damage bullet attack.\n\nThe boss will not retaliate if flinched within 20 seconds of entering the battle field.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLegs Center Area (Mithril Ore, DAGGER),\nLeft Wing (ARM),Right Wing (Twilight Dragon Wing, ARROW)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/twilightdragon.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='ifrid', aliases=['ifrit'])
async def ifrid(ctx):
    embed = discord.Embed(title='Ifrid')
    embed.add_field(name='Level Boss', value='Normal : 112', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Blazing Graben: Deepest Part')
    embed.add_field(name='Element', value='', inline=True)
    embed.add_field(name='Base HP', value='555.500', inline=True)
    embed.add_field(name='Base EXP', value='6.000', inline=True)
    embed.add_field(name='P.Def', value='179', inline=True)
    embed.add_field(name='M.Def', value='158', inline=True)
    embed.add_field(name='P.Res', value='4', inline=True)
    embed.add_field(name='M.Res', value='4', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:30  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='185', inline=True)
    embed.add_field(name='Retaliation', value="FTS: Retaliates with a knockback attack if inflicted while the boss's HP is below 50%.\n\nThe farther away a player is from the boss, the more aggro the player generates while attacking.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\n Head, Right Skull Tentacle,\n Left Arm (Broken Robot Arm)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/ifrid.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='york', aliases=['yor'])
async def york(ctx):
    embed = discord.Embed(title='York')
    embed.add_field(name='Level Boss', value='Normal : 118', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Huge Crysta Factory: Storage')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='640.000', inline=True)
    embed.add_field(name='Base EXP', value='6.800', inline=True)
    embed.add_field(name='P.Def', value='PH1: 295; PH2: 295;\n PH3: 413; PH4: 0', inline=True)
    embed.add_field(name='M.Def', value='PH1: 118; PH2: 236;\n PH3: 354; PH4: 0', inline=True)
    embed.add_field(name='P.Res', value='PH1: 4; PH2: 4;\n PH3: 50; PH4: 0', inline=True)
    embed.add_field(name='M.Res', value='PH1: 4; PH2: 4;\n PH3: 50; PH4: 0', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:40  M:0', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 248; PH2:\n 354; PH3: 89; PH4: 0', inline=True)
    embed.add_field(name='Retaliation', value="PH1 (>75% HP); PH2 (20%-75% HP); PH3 (10%-20% HP); PH4 (<10% HP)\nFT: If inflicted during PH4, the boss retaliates with a full map fractional AOE attack that inflicts Sleep ailment;\nS: If inflicted during PH2 or PH4, the boss retaliates with a full map fractional AOE attack that inflicts Sleep ailment (PH2) or Fear ailment (PH4).", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLauncher Muzzle (HB),\nLauncer Side/Right Arm (BWG),\nEnergy Tank/Back (Launcher Arm)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/york.png')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='protoleon', aliases=['proto'])
async def protoleon(ctx):
    embed = discord.Embed(title='Proto Leon')
    embed.add_field(name='Level Boss', value='Normal : 115', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Singolare Ruins: 3rd Floor')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='585.000', inline=True)
    embed.add_field(name='Base EXP', value='6.250', inline=True)
    embed.add_field(name='P.Def', value='PH1: 161; PH1+FTS: 92; PH2: 230', inline=True)
    embed.add_field(name='M.Def', value='PH1: 138; PH1+FTS: 58; PH2: 207', inline=True)
    embed.add_field(name='P.Res', value='PH1: 4; PH2: 24', inline=True)
    embed.add_field(name='M.Res', value='PH1: 4; PH2: 24', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:30  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='275', inline=True)
    embed.add_field(name='Retaliation', value="FTS: If inflicted between 40%-100% HP, the boss retaliates with a large, knockback-inflicting fractional AOE attack and enters an enraged mode (increased attack power). The enraged mode lasts for 20 seconds. While in enraged mode, the boss will not retaliate against FTS.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nPants (Ancient Fabric),\nRight Arm Crystal (Proto Leon's Hammer Bit, OHS),\nBack/Ponytail (BOW)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/protoleon.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='tyrantmachina', aliases=['tyrant'])
async def tyrantmachina(ctx):
    embed = discord.Embed(title='Tyrant Machina')
    embed.add_field(name='Level boss', value='Normal : 121', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Small Demi Machina Factory Core')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='1.050.000', inline=True)
    embed.add_field(name='Base EXP', value='8.400', inline=True)
    embed.add_field(name='P.Def', value='PH1: 61; GREEN+T: 387; PH2: 242', inline=True)
    embed.add_field(name='M.Def', value='PH1: 61; GREEN+T: 387; PH2: 242', inline=True)
    embed.add_field(name='P.Res', value='PH1: 4; GREEN: 25; PH2: 10', inline=True)
    embed.add_field(name='M.Res', value='PH1: 4; GREEN: 25; PH2: 10', inline=True)
    embed.add_field(name='Prorate', value='N:100  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 543; GREEN: 181; PH2: 181', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 2 phases: PH1>25% HP and PH2<=25% HPThe boss has 2 phases: PH1>25% HP and PH2<=25% HP", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Arm,\nRight Arm (ADD - Tyrant Grievance),\nHead (Broken Gas Mask, ADD - Tyrant Mask)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/tyrantmachina.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='moztomachina', aliases=['mozto'])
async def moztomachina(ctx):
    embed = discord.Embed(title='Mozto Machina')
    embed.add_field(name='Level boss', value='Normal : 124', inline=True)
    embed.add_field(name='MQ Chapter', value='6', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Large Demi Machina Factory: Deepest Part')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='1.110.000', inline=True)
    embed.add_field(name='Base EXP', value='12.240', inline=True)
    embed.add_field(name='P.Def', value='PH1: 248; Ph2: 124', inline=True)
    embed.add_field(name='M.Def', value='PH1: 372; PH2: 248', inline=True)
    embed.add_field(name='P.Res', value='15', inline=True)
    embed.add_field(name='M.Res', value='15', inline=True)
    embed.add_field(name='Prorate', value='N:100  P:50  M:50', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 186; PH2: 372', inline=True)
    embed.add_field(name='Retaliation', value="FS: Retaliates when above 50% HP.\nTS: Retaliates when below 50% HP.\n\nDuring PH2, the boss moves to a higher, unreachable area every 20 seconds and launches attacks towards the players.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Arm (DAGGER, ARROW),\nHead (Chimera Hard Horn),\nTail (ARM)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/mozto.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

################ MAIN  QUEST BAB 7 ###################


@bot.command(name='lalvada', aliases=['lal'])
async def lalvada(ctx):
    embed = discord.Embed(title='Lalvada')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value="Monster's Forest: Deep Part")
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='600.000', inline=True)
    embed.add_field(name='Base EXP', value='6.000', inline=True)
    embed.add_field(name='P.Def', value='GREEN: 382;\n YELLOW: 446;\n PH2: 446', inline=True)
    embed.add_field(name='M.Def', value='GREEN: 446;\n YELLOW: 382;\n PH2: 38', inline=True)
    embed.add_field(name='P.Res', value='15', inline=True)
    embed.add_field(name='M.Res', value='15', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:30  M:40', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='228', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nUpper Left Arm (THS),\nHead (STF),\nRight Lower Arm (Mystic Crystal Stone, KTN)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/lalvada.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)



@bot.command(name='zahhakmachina', aliases=['zahhak'])
async def zhhakmachina(ctx):
    embed = discord.Embed(title='Zahhak Machina')
    embed.add_field(name='Level boss', value='Normal : 130', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Lufenas Mansion: Hall')
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='600.000', inline=True)
    embed.add_field(name='Base EXP', value='6.000', inline=True)
    embed.add_field(name='P.Def', value='NORMAL: 1000;\nS: 350;\nPOISON: 350', inline=True)
    embed.add_field(name='M.Def', value='NORMAL: 1000;\nS: 350;\nPOISON: 350', inline=True)
    embed.add_field(name='P.Res', value='5', inline=True)
    embed.add_field(name='M.Res', value='5', inline=True)
    embed.add_field(name='Prorate', value='N:4  P:2  M:1', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='', inline=True)
    embed.add_field(name='Retaliation', value="FTS:\nFT: OK\nS: OK. Reduces def/mdef for 20 sec.\n\nPOIS: Reduces def/mdef for 10 sec if afflicted by POISON", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts: Head/Chin, Left Leg, Tail (Twin Head Dragon Tail, SPEC)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/zahhak.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='guignol', aliases=['guig'])
async def guignol(ctx):
    embed = discord.Embed(title='Guignol')
    embed.add_field(name='Level boss', value='Normal : 130', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Brahe Laboratory: 4th Building')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='490.000', inline=True)
    embed.add_field(name='Base EXP', value='6.200', inline=True)
    embed.add_field(name='P.Def', value='400', inline=True)
    embed.add_field(name='M.Def', value='0', inline=True)
    embed.add_field(name='P.Res', value='BLUE: 80; YELLOW: 55; RED: 30', inline=True)
    embed.add_field(name='M.Res', value='BLUE: 80; YELLOW: 55; RED: 30', inline=True)
    embed.add_field(name='Prorate', value='N:50  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='300', inline=True)
    embed.add_field(name='Retaliation', value="FTS: When in Red mode, the boss will retaliate with a player-centered spike attack.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead,\nLeft Arm (Shattered Guignol's Arm, BWG),\nRight Leg (Broken Guignol's Leg, KN)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/guignol.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='gwaimol', aliases=['gwai'])
async def gwaimol(ctx):
    embed = discord.Embed(title='Gwaimol')
    embed.add_field(name='Level boss', value='Normal : 136', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Cuervo Jail: Roof')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='850.000', inline=True)
    embed.add_field(name='Base EXP', value='8.100', inline=True)
    embed.add_field(name='P.Def', value='205', inline=True)
    embed.add_field(name='M.Def', value='205', inline=True)
    embed.add_field(name='P.Res', value='5', inline=True)
    embed.add_field(name='M.Res', value='5', inline=True)
    embed.add_field(name='Prorate', value='N:3  P:1  M:2', inline=True)
    embed.add_field(name='Crit Res', value='25', inline=True)
    embed.add_field(name='Flee', value='204', inline=True)
    embed.add_field(name='Retaliation', value="F: Immune;\nT: 50% resistance against tumble", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Shoulder,\nHead (Gwaimol's Horn),\nSpear (Gwaimol's Huge Blade)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/gwaimol.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='ornlarf', aliases=['orn'])
async def ornlarf(ctx):
    embed = discord.Embed(title='Ornlarf')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Ultimea Palace: Corridor')
    embed.add_field(name='Element', value='Light', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='108', inline=True)
    embed.add_field(name='M.Def', value='710', inline=True)
    embed.add_field(name='P.Res', value='5', inline=True)
    embed.add_field(name='M.Res', value='5', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:11', inline=True)
    embed.add_field(name='Crit Res', value='30', inline=True)
    embed.add_field(name='Flee', value='692', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Shoulder (Chief BK Shoulder Armor),\nHead (Mithril Ore, check [Retaliation] for TIP)\nRight Arm (Ether Metal)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/ornlarf.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='venenacoenubia', aliases=['venena'])
async def venena(ctx):
    embed = discord.Embed(title='Venena Coenubia')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='7', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='')
    embed.add_field(name='Element', value='VENENA: Fire;\nPILLAR: Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='VENENA: 300\nPILLAR: 290', inline=True)
    embed.add_field(name='M.Def', value='VENENA: 300\nPILLAR: 290', inline=True)
    embed.add_field(name='P.Res', value='VENENA: 6;\nPILLAR: 5', inline=True)
    embed.add_field(name='M.Res', value='VENENA: 6;\nPILLAR: 5', inline=True)
    embed.add_field(name='Prorate', value='N:Venena20;Pillar10\nP:Venena10;Pillar5\nM:Venena5;Pillar20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='VENENA: [NORMAL: 75;\nBREAK: 225];\nPILLAR: 109', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nHead (Lil Empress Horn, SHIELD, DAGGER, ARROW)\nRight Neck (Lil Empress Crystal, ARM", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/venena1.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='quasar', aliases=['demonic'])
async def quasar(ctx):
    embed = discord.Embed(title='Demonic Quasar')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Morga Wasteland: Deepest Area')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='925', inline=True)
    embed.add_field(name='M.Def', value='925', inline=True)
    embed.add_field(name='P.Res', value='7', inline=True)
    embed.add_field(name='M.Res', value='7', inline=True)
    embed.add_field(name='Prorate', value='N:5 P:5 M:5', inline=True)
    embed.add_field(name='Crit Res', value='25', inline=True)
    embed.add_field(name='Flee', value='410', inline=True)
    embed.add_field(name='Retaliation', value="At 75-100% HP: Immune to S, no retaliation against FT.\nAt 50-75% HP: Immune to FT, no retaliation against S.\nAt 25-50% HP: Retaliates only to T.\nAt 10-25% HP: Immune to F, retaliates to T.\nAt 0-10% HP, immune to FTS.\n\nAt 75%, 50%, and 25% HP, the boss will gain invincibility for a short period of time and attack with a full map AOE fractional spikes attack.\nAt 10% HP, the boss will gain invincibility for a short period of time and cast a full map meteor attack that drops 30 seconds after it was casted.\nBoss retaliation is in the form of fractional spikes that deal about 30% of MaxHP and inflicts [Weaken] (25-50% HP) or [Dizzy] (10-25% HP).", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Demon Mask),\nLeft Arm (KN),\nTorso (BWG)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/quasar.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

################ Main Quest BAB 8 ###############
@bot.command(name='shampy', aliases=['sham'])
async def shampy(ctx):
    embed = discord.Embed(title='Shampy')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Turnus Mine: Hall')
    embed.add_field(name='Element', value='SHAMPY: Water;\nRED+COMRABY: Fire;\nBLUE+COMRABY: Water;\nYELLOW+COMRABY: Wind;', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='SHAMPY: 261;\nCOMRABY: 136;', inline=True)
    embed.add_field(name='M.Def', value='SHAMPY: 290;\nCOMRABY: 202;', inline=True)
    embed.add_field(name='P.Res', value='SHAMPY: 5;\nCOMRABY: 5;', inline=True)
    embed.add_field(name='M.Res', value='SHAMPY: 5;\nCOMRABY: 5;', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:20  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='SHAMPY: 434;\nCOMRABY: 300', inline=True)
    embed.add_field(name='Retaliation', value="FTS: OK", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nBack Hair,\nWand/Right Arm,\nHead (SHIELD)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/shampy.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='titancrystal', aliases=['titan'])
async def titancrystal(ctx):
    embed = discord.Embed(title='Titan Crystal')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Decaying Ruins')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='NORMAL: 593; BREAK+BODY: 400', inline=True)
    embed.add_field(name='M.Def', value='NORMAL: 447; BREAK+BODY: 306', inline=True)
    embed.add_field(name='P.Res', value='NORMAL: 25; BREAK+BODY: 5', inline=True)
    embed.add_field(name='M.Res', value='NORMAL: 25; BREAK+BODY: 5', inline=True)
    embed.add_field(name='Prorate', value='N:20  P:30  M:25', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='111', inline=True)
    embed.add_field(name='Retaliation', value="FTS: Damage to the boss is capped at 1 while interrupted.\nFREEZE: Damage to the boss increases by 4 times for 10 sec.\n\nAt 50% HP, the boss moves to the edge of the map and casts a bunch of meteors AOEs.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Arm (Corroded Trunk, KTN),\nLeft Arm (Corroded Trunk, KN),\nTorso (Rare Diopside)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/crystaltitan.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='momfluck', aliases=['mom'])
async def momfluck(ctx):
    embed = discord.Embed(title='Mom Fluck')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Forgotten Cave')
    embed.add_field(name='Element', value='MOM_FLUCK: Water;\nFLUCK: Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='MOM_FLUCK: 226;\nFLUCK: 139;', inline=True)
    embed.add_field(name='M.Def', value='MOM_FLUCK: 226;\nFLUCK: 139;', inline=True)
    embed.add_field(name='P.Res', value='MOM_FLUCK: 6;\nFLUCK: 5', inline=True)
    embed.add_field(name='M.Res', value='MOM_FLUCK: 6;\nFLUCK: 5', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:15  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='MOM_FLUCK: 226;\nFLUCK: 206;', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Vivid Crest),\nFloating Ring/Body (Fluck Egg),\nTail", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/momfluck.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='mardula', aliases=['mardu'])
async def mardula(ctx):
    embed = discord.Embed(title='Mardula')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Hall of Blessings Gods')
    embed.add_field(name='Element', value='PH1: Light; PH1+BREAK+SPEAR: Wind; PH2: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='158', inline=True)
    embed.add_field(name='M.Def', value='394', inline=True)
    embed.add_field(name='P.Res', value='6', inline=True)
    embed.add_field(name='M.Res', value='6', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='470', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Back/Left Ribbon of MD (Broken Holy Scale),\nTorso (MD),\nSpear (HB)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/mardula.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='seelezauga', aliases=['seele'])
async def seelezauga(ctx):
    embed = discord.Embed(title='Seele Zauga')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Shrine of the Goddess of Species')
    embed.add_field(name='Element', value='SEELE: Light;\nBLUE/RED_GUARDIAN: Light;', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='SEELE: 320;\nBLUE/RED_GUARDIAN: 155;', inline=True)
    embed.add_field(name='M.Def', value='SEELE: 320;\nBLUE/RED_GUARDIAN: 155;', inline=True)
    embed.add_field(name='P.Res', value='SEELE: 6;\nBLUE/RED_GUARDIAN: 6;', inline=True)
    embed.add_field(name='M.Res', value='SEELE: 6;\nBLUE/RED_GUARDIAN: 6;', inline=True)
    embed.add_field(name='Prorate', value='N:SEELE: 5;BLUE/RED_GUARDIAN: 50;\nP:N:SEELE: 10;BLUE/RED_GUARDIAN: 50\nM:N:SEELE: 20;BLUE/RED_GUARDIAN: 50', inline=True)
    embed.add_field(name='Crit Res', value='25', inline=True)
    embed.add_field(name='Flee', value='240', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nLeft Arm (High Grade Frill Fabric, ADD),\nRight Waist (ARM)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/seele.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='kingpiton', aliases=['piton'])
async def kingpiton(ctx):
    embed = discord.Embed(title='King Piton')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Elf Mountains: Shrine')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='NORMAL: 790;\nBREAK+1: 690;\nBREAK+2: 590;\nBREAK+3: 490', inline=True)
    embed.add_field(name='M.Def', value='242', inline=True)
    embed.add_field(name='P.Res', value='NORMAL: 15;\nBREAK+1: 10;\nBREAK+2: 5;\nBREAK+3: 0', inline=True)
    embed.add_field(name='M.Res', value='NORMAL: 15;\nBREAK+1: 10;\nBREAK+2: 5;\nBREAK+3: 0', inline=True)
    embed.add_field(name='Prorate', value='N:30  P:30  M:30', inline=True)
    embed.add_field(name='Crit Res', value='10', inline=True)
    embed.add_field(name='Flee', value='122', inline=True)
    embed.add_field(name='Retaliation', value="The boss has a damage cap of 500k.\nThe boss's DEF, PRES, and MRES decrease for each broken part.\nAlso, every broken part increases FTS cooldown by 10 seconds.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts: Right Arm, Left Arm, Torso (King Piton Fur)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/kingpiton.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='finsternthedarkdragon', aliases=['finstern'])
async def finsternthedarkdragon(ctx):
    embed = discord.Embed(title='Finstern the Dark Dragon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='8', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Dark Dragon Shrine: Near the Top')
    embed.add_field(name='Element', value='FINSTERN: Dark;\nOBSCUROPHANY: Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='250', inline=True)
    embed.add_field(name='M.Def', value='250', inline=True)
    embed.add_field(name='P.Res', value='FINSTERN: [PH1: 6; PH2: 16; PH2+FTS: 6]', inline=True)
    embed.add_field(name='M.Res', value='FINSTERN: [PH1: 6; PH2: 16; PH2+FTS: 6]', inline=True)
    embed.add_field(name='Prorate', value='N:100  P:1  M:10', inline=True)
    embed.add_field(name='Crit Res', value='[PH1: 0; PH2: 125; PH2+FTS: 0]', inline=True)
    embed.add_field(name='Flee', value='25', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Leg (KTN),\nLeft Wing (OHS),\nTail (Dark Gemstone)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/finstern.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='tuscog', aliases=['tus'])
async def tuscog(ctx):
    embed = discord.Embed(title='Tuscog')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Eryldan Street: Near the Forest of Ein')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1: 423; PH2: 339', inline=True)
    embed.add_field(name='M.Def', value='PH1: 253; PH2: 253', inline=True)
    embed.add_field(name='P.Res', value='6', inline=True)
    embed.add_field(name='M.Res', value='6', inline=True)
    embed.add_field(name='Prorate', value='N:20  P:5  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='PH1: 253; PH2: 630', inline=True)
    embed.add_field(name='Retaliation', value="2 Phases. Transition @50% HP\n\nBoss becomes Pink during PH2.\n\nFTS:\nPH1: OK\nPH2: Retaliates with an 8m radius, enemy-centered spike\nbed (P, Knockback) when FTS while HP<50%\n\nImmune to [Fear]", inline=False)
    embed.add_field(name='Parts Destruction:', value="", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/tuscog.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)



@bot.command(name='erodedpilz', aliases=['pilz'])
async def erodedpilz(ctx):
    embed = discord.Embed(title='Eroded Pilz')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Morthell Swell: Deep Area')
    embed.add_field(name='Element', value='PURPLE: Fire;\nGREEN: Neutrl', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='NORMAL: 602;\nGREEN: 1033;\nBREAK+RIGHT: 431;\nBREAK+RIGHT+GREEN: 861', inline=True)
    embed.add_field(name='M.Def', value='NORMAL: 496;\nNORMAL+GREEN: 826;\nBREAK+LEFT: 330;\nBREAK+LEFT+GREEN: 660', inline=True)
    embed.add_field(name='P.Res', value='NORMAL: 26;\nBREAK+RIGHT: 6;\nBREAK+HEAD: 20;\nBREAK+RIGHT+HEAD: 0', inline=True)
    embed.add_field(name='M.Res', value='NORMAL: 26;\nBREAK+RIGHT: 6;\nBREAK+HEAD: 20;\nBREAK+RIGHT+HEAD: 0', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:20  M:5', inline=True)
    embed.add_field(name='Crit Res', value='NORMAL/PURPLE: 20;\nGREEN: 40', inline=True)
    embed.add_field(name='Flee', value='258', inline=True)
    embed.add_field(name='Retaliation', value="2 Phases\nnPhase Transition @ 40% HP: If the boss is in NORMAL/PURPLE mode at the 40% HP mark, it will switch to GREEN (high defense) mode. Else, it stays in GREEN mode.\n\nFor all Phases: After 30 sec of being in GREEN mode, the boss will revert back to NORMAL/PURPLE mode, unless a phase transition occurs.\nThe phase transition resets the GREEN mode timer back to 30 sec.\n\nBreaking the boss's parts reduces its defenses and resistances.\n\nFTS:\nGREEN: Immune\nPURPLE:\nPH1: If FTS while HP >= 40%, boss changes to GREEN mode.\nPH2: If FTS while HP < 40% HP, the boss will change to GREEN", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Corroded Mushroom Cap),\nRight Mushroom (Corroded Mushroom Cap),\nLeft Leg (Broken Mushroom Nail)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/eroded.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='pyxtica', aliases=['pyx'])
async def pyxtica(ctx):
    embed = discord.Embed(title='Pyxtica')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Fractum Sector: Area 3')
    embed.add_field(name='Element', value='PURPLE: Dark; RED: Fire; GREEN: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PURPLE: 437; RED: 437; PURPLE+FATIGUE: 315; GREEN: 315', inline=True)
    embed.add_field(name='M.Def', value='PURPLE: 437; RED: 437; PURPLE+FATIGUE: 315; GREEN: 315', inline=True)
    embed.add_field(name='P.Res', value='PURPLE: 7; RED: 7; GREEN: -43', inline=True)
    embed.add_field(name='M.Res', value='PURPLE: 7; RED: 7; GREEN: 7', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='PURPLE: 15; RED: 50; GREEN: 500', inline=True)
    embed.add_field(name='Flee', value='654', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (MD),\nTorso (THS),\nTail (Pyxtica's Tail)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/pyxtica.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='kuzto', aliases=['kuz'])
async def kuzto(ctx):
    embed = discord.Embed(title='Kuzto')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Labilans Sector: Square')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='KUZTO: 535;\nLAURUS: 357;\nTORETTA: 178;', inline=True)
    embed.add_field(name='M.Def', value='KUZTO: 535;\nLAURUS: 178;\nTORETTA: 357;', inline=True)
    embed.add_field(name='P.Res', value='KUZTO: 7;\nLAURUS: 14;\nTORETTA: 7;', inline=True)
    embed.add_field(name='M.Res', value='KUZTO: 7;\nLAURUS: 7;\nTORETTA: 14;', inline=True)
    embed.add_field(name='Prorate', value='N:20  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='25', inline=True)
    embed.add_field(name='Flee', value='267', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nRight Thigh (ARM),\nLeft Arm (Mystical Nut)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/kuzto.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='sapphireroga', aliases=['sroga'])
async def sapphireroga(ctx):
    embed = discord.Embed(title='Sapphire Roga')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Avant Plastida: Deepest Area')
    embed.add_field(name='Element', value='SAPPHIRE_ROGA: [PURPLE: Dark; RED: Fire; GREEN: Neutral];', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value=':[PURPLE: 315; RED: 315; GREEN: 315];', inline=True)
    embed.add_field(name='M.Def', value=':[PURPLE: 315; RED: 315; GREEN: 315];', inline=True)
    embed.add_field(name='P.Res', value='[PURPLE: 7; RED: 70; GREEN: -75];', inline=True)
    embed.add_field(name='M.Res', value='[PURPLE: 7; RED: 7; GREEN: 7];', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:10  M:5', inline=True)
    embed.add_field(name='Crit Res', value='[PURPLE: 20; GREEN: 300; RED: 0];', inline=True)
    embed.add_field(name='Flee', value='140', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Sapphire Roga Horns),\nLeft Arm (SHIELD),\nRight Arm (OHS)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/sapphireroga.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='gravicep', aliases=['gravi'])
async def gravicep(ctx):
    embed = discord.Embed(title='')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Recetacula Sector: Depot Rooftop')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='AGGRO<=7m: 552; AGGRO>7m; 185', inline=True)
    embed.add_field(name='M.Def', value='AGGRO<=7m: 185; AGGRO>7m; 734', inline=True)
    embed.add_field(name='P.Res', value='AGGRO<=7m: 21; AGGRO>7m; 7', inline=True)
    embed.add_field(name='M.Res', value='AGGRO<=7m: 7; AGGRO>7m; 21', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:100  M:100', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='AGGRO<=7m: 275; AGGRO>7m; 550', inline=True)
    embed.add_field(name='Retaliation', value="AGGRO<=7m: FT Immune and Guard rate up.\nAGGRO>7m: S: Immune and Evasion rate up", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Arm (STF),\nRight Arm (KTN),\nHead/Torso (Gravicep Accessory Chip)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/gravicep.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='repthon', aliases=['rep'])
async def repthon(ctx):
    embed = discord.Embed(title='Repthon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Deltzon Research Zone: Deepest Area')
    embed.add_field(name='Element', value='PURPLE: Dark;\nRED: Fire;\nYELLOW: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PURPLE: 467;\nRED: 935;\nYELLOW: 467', inline=True)
    embed.add_field(name='M.Def', value='PURPLE: 467;\nRED: 935;\nYELLOW: 935', inline=True)
    embed.add_field(name='P.Res', value='7', inline=True)
    embed.add_field(name='M.Res', value='7', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='PURPLE: 25;\nRED: 25;\nYELLOW: 150', inline=True)
    embed.add_field(name='Flee', value='333', inline=True)
    embed.add_field(name='Retaliation', value="The boss starts out in PURPLE mode\n\nWhile in PURPLE mode, if 100k+ damage is inflicted to the boss while its HP is above 60%, the boss will change to RED mode\nThe boss will change back from RED to PURPLE mode after 15 sec.\n\nWhen HP reaches below 60% while in RED mode or when dealing 100k+ damage while HP is below 60% in PURPLE mode, the boss will change to YELLOW mode.\nWhile in YELLOW mode, the boss will retaliate with a Mana Explosion inflicting attack when it is FTS.\nThe boss will revert back from YELLOW to PURPLE mode after 15 sec.\nThere is a 500k damage cap during the RED and YELLOW modes.\n\nFTS:\nPURPLE: OK\nRED: Immune\nYELLOW: Retaliates to FTS\nThe boss has a long FTS cooldown", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Citric Essence),\nFuselage/Left Wing (MD),\nTail (HB)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/repthon.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='venenameta', aliases=['nemet'])
async def venenameta(ctx):
    embed = discord.Embed(title='Venena Metacoenubia')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='9', inline=True)
    embed.add_field(name='MQ Locked', value='Yes (Area Lock)', inline=True)
    embed.add_field(name='Map', value='Neo Plastida')
    embed.add_field(name='Element', value='VENENA: Fire;\nSEDEM: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='VENENA: 820;\nSEDEM: 655', inline=True)
    embed.add_field(name='M.Def', value='VENENA: 820;\nSEDEM: 655', inline=True)
    embed.add_field(name='P.Res', value='VENENA: 7;\nSEDEM: 7', inline=True)
    embed.add_field(name='M.Res', value='VENENA: 7;\nSEDEM: 7', inline=True)
    embed.add_field(name='Prorate', value='N:VENENA: 1;SEDEM: 10 \nP:VENENA: 1; SEDEM: 5\nM:VENENA: 5; SEDEM: 20', inline=True)
    embed.add_field(name='Crit Res', value='VENENA: 5;\nSEDEM: 25', inline=True)
    embed.add_field(name='Flee', value='VENENA: 436;\nSEDEM: 283', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts: Head/Top of Crown (ARM),\nTorso (Empress Ogre Fang, OHS, BW, STF, KN, HB),\nLeft Arm (Empress Ogre Crystal, THS, BWG, MD, SHIELD, KTN)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/venena2.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


################### MAIN QUEST BAB 10####################

@bot.command(name='pisteus', aliases=['pist'])
async def pisteus(ctx):
    embed = discord.Embed(title='Pisteus')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='10', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Ducia Coast: Depths')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='386', inline=True)
    embed.add_field(name='M.Def', value='483', inline=True)
    embed.add_field(name='P.Res', value='7', inline=True)
    embed.add_field(name='M.Res', value='7', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:10  M:15', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='432', inline=True)
    embed.add_field(name='Retaliation', value="T: Immune.\nS: OK when inflicted while HP > 30% HP. Boss runs away and retaliates with a large fin attack (M, Freeze) when Stunned at <= 30% HP.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Fin,\nLeft Fin,\nHead (Pisteus Horns)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/pisteus.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='arachnidemon', aliases=['arach'])
async def arachnidemon(ctx):
    embed = discord.Embed(title='Arachnidemon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='10', inline=True)
    embed.add_field(name='MQ Locked', value='Yes(Area Lock)', inline=True)
    embed.add_field(name='Map', value='Arche Valley: Depths')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='512', inline=True)
    embed.add_field(name='M.Def', value='392', inline=True)
    embed.add_field(name='P.Res', value='7', inline=True)
    embed.add_field(name='M.Res', value='7', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:20  M:20', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='351', inline=True)
    embed.add_field(name='Retaliation', value="FTS: OK. Cooldown duration increases when HP < 50%", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTail,\nLeft Arm,\nHead (Radiant Miracle Water)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/arachnidemon.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='blackshadow', aliases=['bs'])
async def blackshadow(ctx):
    embed = discord.Embed(title='Black Shadow')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='10', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Rokoko City Ruins')
    embed.add_field(name='Element', value='PURPLE: Dark;\nRED: Fire', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='398', inline=True)
    embed.add_field(name='M.Def', value='598', inline=True)
    embed.add_field(name='P.Res', value='PURPLE: 7;\nRED: 27', inline=True)
    embed.add_field(name='M.Res', value='PURPLE: 7;\nRED: 27', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:10  M:10', inline=True)
    embed.add_field(name='Crit Res', value='10', inline=True)
    embed.add_field(name='Flee', value='297', inline=True)
    embed.add_field(name='Retaliation', value="PURPLE: OK\nRED: FTS success rate is reduced by 50%", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nLeft Chest (Black Shadow Cape Fragment),\nMantle/Cloak (Black Shadow Cape Fragment)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/blackshadow.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='hexter', aliases=['hex'])
async def hexter(ctx):
    embed = discord.Embed(title='Hexter')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='10', inline=True)
    embed.add_field(name='MQ Locked', value='Yes(Area Lock)', inline=True)
    embed.add_field(name='Map', value="Witch's Woods Depths")
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='607', inline=True)
    embed.add_field(name='M.Def', value='606', inline=True)
    embed.add_field(name='P.Res', value='8', inline=True)
    embed.add_field(name='M.Res', value='8', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:25', inline=True)
    embed.add_field(name='Crit Res', value='NORM: 20;\nCRITRES: 100', inline=True)
    embed.add_field(name='Flee', value='303', inline=True)
    embed.add_field(name='Retaliation', value="At the start of the battle and every 60 seconds afterwards, the boss will go to the center of the map and enter CRITRES mode for a period of time. When entering CRITRES mode, the boss will release multiple slow moving fins that go around the map while moving outwards. These fins deal heavy magic damage, so it is best to just go at the upper left/right corners of the map to avoid these fins. After the fins are released, the boss will then summon a plethora of meteors. Shortly after releasing all of the fins and meteors, the boss will return back to its normal form.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Flame Horn),\nFuselage/Left Wing,\nTail", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/hexter.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='irestida', aliases=['ires'])
async def irestida(ctx):
    embed = discord.Embed(title='Irestida')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='10', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Nov Diela: Center')
    embed.add_field(name='Element', value='IRESTIDA: [BLUE: Neutral; GREEN/ORANGE: Wind];\nFLYSTIDA/WALKASTIDA: Dark;', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='922', inline=True)
    embed.add_field(name='M.Def', value='310', inline=True)
    embed.add_field(name='P.Res', value='8', inline=True)
    embed.add_field(name='M.Res', value='8', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:50', inline=True)
    embed.add_field(name='Crit Res', value='[NORMAL: 100; FREEZE: 0];', inline=True)
    embed.add_field(name='Flee', value='310', inline=True)
    embed.add_field(name='Retaliation', value="T: Immune\nFS: Immune above 75% HP", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Upper Torso,\nRight Hand (Irestida's Bubble),\nTail (Irestida's Tail)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/irestida.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

############### MAIN QUEST BAB 11#####################
@bot.command(name='reliza', aliases=['reli'])
async def reliza(ctx):
    embed = discord.Embed(title='Raliza')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Manna Waterfront')
    embed.add_field(name='Element', value='PH1+PH2: Dark;\nPH3: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='420', inline=True)
    embed.add_field(name='M.Def', value='630', inline=True)
    embed.add_field(name='P.Res', value='PH1+PH2: 8;\nPH3: -42', inline=True)
    embed.add_field(name='M.Res', value='PH1+PH2+PH3: 8', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:10', inline=True)
    embed.add_field(name='Crit Res', value='PH1+PH2: 30;\nPH3: 500', inline=True)
    embed.add_field(name='Flee', value='640', inline=True)
    embed.add_field(name='Retaliation', value="F: Retaliates with a player-centered attack that inflicts mana explosion during PH1 and PH3.\nT: Retaliates with a player-centered attack that inflicts mana explosion during PH2 and PH3.\nS: OK\nFEAR: Immune", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Arm (Crimson Silk),\nRight Wing (ADD: Iron Witch Wings),\nTorso (ARM)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/reliz.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='gemma', aliases=['gema'])
async def gemma(ctx):
    embed = discord.Embed(title='Gemma')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Fugitive Lake Swamp')
    embed.add_field(name='Element', value='RED: Fire; YELLOW: Earth; GREEN: Wind', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='728', inline=True)
    embed.add_field(name='M.Def', value='728', inline=True)
    embed.add_field(name='P.Res', value='NORM: 16; SHELL: 96', inline=True)
    embed.add_field(name='M.Res', value='NORM: 16; SHELL: 96', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:5  M:10', inline=True)
    embed.add_field(name='Crit Res', value='20', inline=True)
    embed.add_field(name='Flee', value='465', inline=True)
    embed.add_field(name='Retaliation', value="T: Immune\nFTS: Immune during SHELL mode\n\nDIZZY: The boss turns YELLOW, retaliates with a spinning attack that inflicts Dizzy, and becomes Earth element.DIZZY: The boss turns YELLOW, retaliates with a spinning attack that inflicts Dizzy, and becomes Earth element.\nPARALYSIS: The boss turns GREEN, retaliates with a spinning attack that inflicts Paralysis, and becomes Wind element.\nIGNITE: The boss turns RED, retaliates with a spinning attack that inflicts Ignite, and becomes Fire element.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nCore/Head (Gemma's Jewel),\nRight Side of Fuselage (STF),\nTail (OHS)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/gemma.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='ferzen', aliases=['ferz'])
async def ferzen(ctx):
    embed = discord.Embed(title='Ferzen the Rock Dragon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='', inline=True)
    embed.add_field(name='MQ Locked', value='', inline=True)
    embed.add_field(name='Map', value='Guardian Forest: Giant Tree')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='NORM: 1055;\nBREAK+HEAD: def-52;\nBREAK+TAIL: def-52;\nBREAK+TORSO: def-104', inline=True)
    embed.add_field(name='M.Def', value='NORM: 740;\nBREAK+HEAD: mdef-28;\nBREAK+TAIL: mdef-28;\nBREAK+TORSO: mdef-54', inline=True)
    embed.add_field(name='P.Res', value='8', inline=True)
    embed.add_field(name='M.Res', value='8', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:10  M:20', inline=True)
    embed.add_field(name='Crit Res', value='20', inline=True)
    embed.add_field(name='Flee', value='314', inline=True)
    embed.add_field(name='Retaliation', value="Breaking the boss's parts reduces its defenses.\nAt 20% HP, the boss will gain invincibility for a period of time, release floor spikes centered around its body, and summon four large, circular AOE attacks.\nWhen the aggro holder is outside of the boss's attack range, the boss will start moving towards the aggro holder.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTorso,\nHead (Terrestrial Tears),\nTail (Mithril Ore)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/ferzen.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='juniordragonzyvio', aliases=['junior'])
async def juniordragonzyvvio(ctx):
    embed = discord.Embed(title='Junior Dragon Zyvio')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Storage Yard: Arena')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='640', inline=True)
    embed.add_field(name='M.Def', value='535', inline=True)
    embed.add_field(name='P.Res', value='8', inline=True)
    embed.add_field(name='M.Res', value='8', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:10  M:5', inline=True)
    embed.add_field(name='Crit Res', value='20', inline=True)
    embed.add_field(name='Flee', value='640', inline=True)
    embed.add_field(name='Retaliation', value="S: Immune to S while in Normal mode and HP >= 50%.\nAlso Immune to S while in Rage mode and HP < 50%\nFT: Immune to FT while in Normal mode and HP < 50%.\nAlso Immune to FT while in Rage mode and HP > 50%\n\nThe boss has a damage limit of 999999. If the boss receives damage above 500k in one instance, the boss will go into Rage mode and summon 2 Zimius mobs (max 2 at a time).\nWhile in Rage mode, the boss's Evasion rate increases, but the damage limit is lifted.\nAt 50% HP, the boss becomes [Invincible] for a period of time, goes into Rage mode, and summons 2 Zimius mobs (max 2 at a time). Rage mode lasts for 30 seconds.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead,\nRight Arm,\nBase of Tail (Junior Dragon Black Thorn)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/zyvio.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='wardragonturba', aliases=['turba'])
async def wardragonturba(ctx):
    embed = discord.Embed(title='War Dragon Turba')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Prime Ramus: Village')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='596', inline=True)
    embed.add_field(name='M.Def', value='705', inline=True)
    embed.add_field(name='P.Res', value='8', inline=True)
    embed.add_field(name='M.Res', value='8', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:5  M:10', inline=True)
    embed.add_field(name='Crit Res', value='40', inline=True)
    embed.add_field(name='Flee', value='480', inline=True)
    embed.add_field(name='Retaliation', value="FTS: Increased cooldown during PH2 (HP <= 50%)\nT: Immune during PH1 (HP > 50%)\nS: When stunned during PH2, the boss will: gain\n[Invincible] for a short period of time, go to the center of the map, summon a bunch of spike beds, and then release an annulus-shaped, foe-centered spike bed AOE, where the safe areas are inside the inner circle (by the boss) and outside the outer circle.\n\nWhen the boss's HP crosses 50%, the boss will enter PH2 and perform the same actions as its retaliation for being stunned during PH2 (described above). Breaking the boss's right arm significantly reduces the boss's guard rate. The boss also has a straight line laser attack that inflicts absolute [Petrify].", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts: Head (War Dragon Horn), Torso (MD), Right Arm (KTN)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/wardragonturba.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='vlamtheflamedragon', aliases=['vlam'])
async def vlamtheflamedragon(ctx):
    embed = discord.Embed(title='Vlam the Flame Dragon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Divido Spring')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1: 880;\nPH2: 440:\nPH3: 220', inline=True)
    embed.add_field(name='M.Def', value='PH1: 880;\nPH2: 440:\nPH3: 220', inline=True)
    embed.add_field(name='P.Res', value='PH1: 8;\nPH2: 0:\nPH3: -16', inline=True)
    embed.add_field(name='M.Res', value='PH1: 8;\nPH2: 0:\nPH3: -16', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:10  M:15', inline=True)
    embed.add_field(name='Crit Res', value='30', inline=True)
    embed.add_field(name='Flee', value='410', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 3 phases:\n\nPH1: HP > 66%. Immune to F. TS are both OK.\nPH2: HP > 33% & HP ≤ 66%. Immune to S. FT are both OK.\nPH3: HP ≤ 33%. Immune to TS. F is OK.\n\nThe boss has a high FTS cooldown. The boss's floor attacks deal heavy MaxHP fractional damage (about 75% fractional damage without any reductions). The boss also has attacks that inflict absolute ailments.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Wing (BOW),\nHead (HB),\nTail (Toxic Dragon Caudal Claw)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/vlam.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='velum', aliases=['vel'])
async def velum(ctx):
    embed = discord.Embed(title='Velum')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Arstida Depths')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='892', inline=True)
    embed.add_field(name='M.Def', value='892', inline=True)
    embed.add_field(name='P.Res', value='CYAN/BLUE/RED: 8;\nPURPLE: 75', inline=True)
    embed.add_field(name='M.Res', value='CYAN/BLUE/RED: 8;\nPURPLE: 75', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:10', inline=True)
    embed.add_field(name='Crit Res', value='25', inline=True)
    embed.add_field(name='Flee', value='330', inline=True)
    embed.add_field(name='Retaliation', value="The boss starts out in CYAN form. After 8 seconds, it will either remain in CYAN form or change to RED/BLUE form depending on the aggro holder's distance to the boss:\n\nCYAN: 6m <= dist < 7m\nBLUE: dist >= 7m\nRED: dist < 6m\n\nAfter 20 sec of being in RED/BLUE form, it will revert back to CYAN form and change color again after 8 sec if the distance conditions are met. This periodic color change repeats throughout the battle. FTS does not reset the 20 sec timer of a color form.\n\nBreaking the boss's parts reduces its guard rate.\nCYAN: FTS is OK\nRED: Retaliates to F\nBLUE: Retaliates to T\nPURPLE: Immune to FTS. Retaliates to [Fear]\n\nWhile in PURPLE form, the boss's guard rate is extremely high.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Knee (Velum's Armor),\nLeft Arm (OHS),\nRight Shoulder (Shield; Can be seen via Tumble or via Stun during charge attack)3 Parts:\nRight Knee (Velum's Armor),\nLeft Arm (OHS),\nRight Shoulder (Shield; Can be seen via Tumble or via Stun during charge attack)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/velum.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='oculasignio', aliases=['ocul'])
async def oculasignio(ctx):
    embed = discord.Embed(title='Oculasignio')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Mt. Vulcani: Summit')
    embed.add_field(name='Element', value='OCULASIGNIO: Dark;\nTEPIPOTAMUS: Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='N: 987; BREAK+BODY: 395', inline=True)
    embed.add_field(name='M.Def', value='N: 987; BREAK+BODY: 395', inline=True)
    embed.add_field(name='P.Res', value='[N: 30; BREAK1: 20; BREAK2: 10; BREAK3: 0', inline=True)
    embed.add_field(name='M.Res', value='[N: 30; BREAK1: 20; BREAK2: 10; BREAK3: 0', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='OCULASIGNIO: 30;\nTEPIPOTAMUS: 20', inline=True)
    embed.add_field(name='Flee', value='310', inline=True)
    embed.add_field(name='Retaliation', value="T: Immune above 50% HP\nFS: Immune below 50% HP\n\nBreaking the boss's parts reduces its PRES/MRES by 10% for each part.\nBreaking the boss's Body reduces its DEF/MDEF by 60%.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Hand,\nFuselage/Body (Evil Pearl),\nHead (Easier to break with Tumble)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/oculasignio.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='gordel', aliases=['gor'])
async def gordel(ctx):
    embed = discord.Embed(title='Gordel')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='11', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value="Milcaska Falls: Weredragon's Mouth")
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='NORM: 1717;\nBREAK+TORSO: 1145', inline=True)
    embed.add_field(name='M.Def', value='NORM: 1717;\nBREAK+TORSO: 1145', inline=True)
    embed.add_field(name='P.Res', value='NORM: 39;\nBREAK+TAIL: 19', inline=True)
    embed.add_field(name='M.Res', value='NORM: 39;\nBREAK+TAIL: 19', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:5', inline=True)
    embed.add_field(name='Crit Res', value='40', inline=True)
    embed.add_field(name='Flee', value='350', inline=True)
    embed.add_field(name='Retaliation', value="The boss has two phases:\nPH1: HP>=50%\n\PH2: HP<50%\n\nF: OK during PH1. Immune to F during PH2\nT: During PH1, if F is not in cooldown and the boss is Tumbled, F will be forced into cooldown. Immune to T during PH2.\nS: Immune to S during PH1. OK during PH2", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTorso (MD),\nLeft Arm (THS),\nTail (Gordel's Caudal Armor)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/gordel.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

############### Main Quest 12 ##################
@bot.command(name='guardgolem', aliases=['gg'])
async def guardgolem(ctx):
    embed = discord.Embed(title='Guard Golem')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value="Weredragon's Throat")
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1: 1160;\nPH2: 0;\nPH3: 0', inline=True)
    embed.add_field(name='M.Def', value='PH1: 1160;\nPH2: 0;\nPH3: 0', inline=True)
    embed.add_field(name='P.Res', value='PH1: 25;\nPH2: 80;\nPH3: 0', inline=True)
    embed.add_field(name='M.Res', value='PH1: 25;\nPH2: 80;\nPH3: 0', inline=True)
    embed.add_field(name='Prorate', value='N:0  P:0  M:0', inline=True)
    embed.add_field(name='Crit Res', value='20', inline=True)
    embed.add_field(name='Flee', value='450', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 3 phases:\nPH1 (Blue): High Guard Rate. FTS is OK\nPH2 (Yellow): High Resistance. Immune to FTS during start of phase; OK afterwards.\nPH3 (Red): High Evasion Rate and motion speed. Immune to FTS.\n\nFear: Immune\nParalysis: During PH3, inflicting [Paralysis] on the boss will interrupt its actions for 5 seconds.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nShield,\nBack (Weredragon Golem Core),\nRight Arm", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/guardgolem.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='burningdragonigneus', aliases=['igneus'])
async def burningdragonigneus(ctx):
    embed = discord.Embed(title='Burning Dragon Igneus')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Boma Moja: Village Center')
    embed.add_field(name='Element', value='Fire', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1: 823;\nPH2: 823', inline=True)
    embed.add_field(name='M.Def', value='PH1: 823;\nPH2: 823', inline=True)
    embed.add_field(name='P.Res', value='PH1: 9;\nPH2: 27', inline=True)
    embed.add_field(name='M.Res', value='PH1: 9;\nPH2: 27', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:15  M:20', inline=True)
    embed.add_field(name='Crit Res', value='20', inline=True)
    embed.add_field(name='Flee', value='360', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 2 phases:\nPH1: 50-100% HP\nPH2: 0-50% HP\FTS: The boss will go into Rage Mode for 10 seconds and then return to normal.\nUpon recovering from FTS, the boss will start emitting shock waves until Rage Mode ends.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead,\nTorso,\nLeft Wing (Burning Dragon Claw)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/igneus.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='trickterdragonmimyugon', aliases=['mimyugon'])
async def trickterdragonmimyugon(ctx):
    embed = discord.Embed(title='Trickter Dragon Mimyugon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Operation Zone: Cockpit Area')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='2620', inline=True)
    embed.add_field(name='M.Def', value='2620', inline=True)
    embed.add_field(name='P.Res', value='9', inline=True)
    embed.add_field(name='M.Res', value='9', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:10  M:15', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='360', inline=True)
    embed.add_field(name='Retaliation', value="PH1: Immune to S. FT is OK\nPH2: Immune to TS. F is OK\n\nFor every broken part: Base DEF/MDEF is reduced by 572", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTorso,\nHead (Trickster Kerato),\nLeft Wing (Trickster Wings)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/mimyugon.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='wackeddragonfazzino', aliases=['fazzino'])
async def wickeddragonfazzino(ctx):
    embed = discord.Embed(title='Wicked Dragon Fazzino')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Propulsion System Room')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='FAZZINO: 488;\nELECITA: 352', inline=True)
    embed.add_field(name='M.Def', value='FAZZINO: 854;\nELECITA: 470', inline=True)
    embed.add_field(name='P.Res', value='FAZZINO: 9;\nELECITA: 8', inline=True)
    embed.add_field(name='M.Res', value='FAZZINO: 9;\nELECITA: 8', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='FAZZINO: 40;\nELECITA: 25', inline=True)
    embed.add_field(name='Flee', value='FAZZINO: 360;\nELECITA: 350', inline=True)
    embed.add_field(name='Retaliation', value="ELECITA:\nFTS: OK\n\nF: OK\nTS: Immune unless both ELECITA mobs are defeated. OK otherwise", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Wing,\nRight Wing,\nHead (Wicked Dragon Twisted Horn)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/wickeddragonfazzino.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='brassdragonreguita', aliases=['reguita'])
async def brassdragonreguita(ctx):
    embed = discord.Embed(title='Brass Dragon Reguita')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Boma Konda: Village Center')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='500', inline=True)
    embed.add_field(name='M.Def', value='875', inline=True)
    embed.add_field(name='P.Res', value='10', inline=True)
    embed.add_field(name='M.Res', value='10', inline=True)
    embed.add_field(name='Prorate', value='N:7  P:3  M:5', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='390', inline=True)
    embed.add_field(name='Retaliation', value="On initiation, the boss will release a full map AOE (fixed M, Curse); this attack can be safely interrupted by Tumble.On initiation, the boss will release a full map AOE (fixed M, Curse); this attack can be safely interrupted by Tumble.\n\nDealing ≥1M damage to the boss causes the boss to have a 300k damage limit for 10 sec\nThe boss has 2 phases (@50%HP). Attack patterns change in PH2.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nStaff (BWG),\nLeft Wing (KTN),\nTail (Brass Dragon Tail)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/brassdragonreguita.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='walican', aliases=['wali'])
async def walican(ctx):
    embed = discord.Embed(title='Walican')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Jabali Kubwa: Summit')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='494', inline=True)
    embed.add_field(name='M.Def', value='988', inline=True)
    embed.add_field(name='P.Res', value='MODE1: 9;\nMODE2: 59', inline=True)
    embed.add_field(name='M.Res', value='MODE1: 9;\nMODE2: 89', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:10  M:5', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='445', inline=True)
    embed.add_field(name='Retaliation', value="2 Phases\n\nPH1:\nBoss switches between MODE1 & MODE2 depending on the aggro holder's distance from the boss (boss checks in between its attacks):\n\nIf Aggro<6m: MODE1\nIf Aggro≥6m: MODE2\nFTS:\nMODE1; OK\nMODE2:\nPH1: [Invincible], full map AOE retaliation (current HP FR, abs Slow), ends MODE2 and rechecks aggro distance\nPH2: OK, ends MODE2 and rechecks aggro distance", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Walican Horn),\nLeft Wing (THS),\nTail (BOW)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/walican.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='dominaredor', aliases=['domi'])
async def dominaredor(ctx):
    embed = discord.Embed(title='Dominaredor')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='12', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Frozen Falls: Depths')
    embed.add_field(name='Element', value='DOMINAREDOR: Dark;\nCOENUBIA: Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1+PH2: 1265;\nPH2+RETAL: 634', inline=True)
    embed.add_field(name='M.Def', value='PH1+PH2: 1265;\nPH2+RETAL: 634', inline=True)
    embed.add_field(name='P.Res', value='PH1: 50;\nPH2: 20;\nPH2+RETAL: 10', inline=True)
    embed.add_field(name='M.Res', value='PH1: 50;\nPH2: 20;\nPH2+RETAL: 10', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='PH1: 30;\nPH2: 40', inline=True)
    embed.add_field(name='Flee', value='460', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 2 phases (transition @50% HP)\n\nPH1:\nFour ball COENUBIAS:\nTL White: Heals 25% of boss's HP every 10 sec\nTR Purple: Vortex (CurHP FR, Freeze)\nBL Purple: Meteor (Magic, Stun)\nBR Dark Purple: Triangular fins (MaxHP FR, Fear)\n\nFTS:\nCOENUBIA: Immune\nDOMINAREDOR: OK\nPH2:\nBoss's HP is locked until any 2 COENUBIA is defeated. Any COENUBIAS defeated after the first 2 adds 10% P/MRES to the boss (max +20%).\n\nFTS:\nIf the number of defeated COENUBIAS since the start of PH2 ≤ 2, FTS the boss is OK.\nIf the number defeated > 2, the boss retaliates to FTS", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead/Heart,\nTail (HB),\nLeft Wing (MD)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/dominaredor.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

################## Main Quest Bab 13 #####################

@bot.command(name='zapo', aliases=['zap'])
async def zapo(ctx):
    embed = discord.Embed(title='Zapo')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Puerta Islands: Adit')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='896', inline=True)
    embed.add_field(name='M.Def', value='641', inline=True)
    embed.add_field(name='P.Res', value='10', inline=True)
    embed.add_field(name='M.Res', value='10', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:5  M:10', inline=True)
    embed.add_field(name='Crit Res', value='30', inline=True)
    embed.add_field(name='Flee', value='575', inline=True)
    embed.add_field(name='Retaliation', value="The boss has 2 phases.\n\nPH1:\nFTS: OK\nPH2:\nFTS: Immune while doing the rush to vortex attack pattern. OK otherwise.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Hand (DAGGER),\nRight Torso/Spear (ARM),\nBack/Shield", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/zapo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='redashdragonrudis', aliases=['rudis'])
async def redashdragonrudis(ctx):
    embed = discord.Embed(title='Red Ash Dragon Rudis')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Espuma Dome: Entrance')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='647', inline=True)
    embed.add_field(name='M.Def', value='906', inline=True)
    embed.add_field(name='P.Res', value='10', inline=True)
    embed.add_field(name='M.Res', value='10', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='388', inline=True)
    embed.add_field(name='Retaliation', value="Any damage past the boss's 50% HP is nullified (forced HP lock) When the boss's HP<50%, the boss gains a rare attack pattern where it releases a bunch of meteors all over the arena.\n\nFTS:\nIf Head part is not broken:\nFT: OK\nS: Immune\n\nIf Head part is broken:\nFS: OK\nT: Immune", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Extremely Scary Face),\nLeft Wing (OHS),\nTail (STF)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/redashdragonrudis.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='donprofundo', aliases=['don'])
async def donprofundo(ctx):
    embed = discord.Embed(title='Don Profundo')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Abandoned District: Ruins Summit')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value="DON PROFUNDO: 787;\nPROFUNDO: 488", inline=True)
    embed.add_field(name='M.Def', value='DON PROFUNDO: 1047;\nPROFUNDO: 488', inline=True)
    embed.add_field(name='P.Res', value='DON_PROFUNDO: 20;\nDON_PROFUNDO+SHELL: 90;\nPROFUNDO: 9', inline=True)
    embed.add_field(name='M.Res', value='DON_PROFUNDO: 20;\nDON_PROFUNDO+SHELL: 90;\nPROFUNDO: 9', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:5  M:1', inline=True)
    embed.add_field(name='Crit Res', value='DON_PROFUNDO: 30;\nPROFUNDO: 20', inline=True)
    embed.add_field(name='Flee', value='400', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nTorso (Abyssal Creature Exoskeleton),\nRight Arm Above Saw,\nBack Left Spike on Shoulder", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/donprofundo.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='vatudo', aliases=['vatu'])
async def vatudo(ctx):
    embed = discord.Embed(title='Vatudo')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Deep Sea: Deepest Zone')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='1060', inline=True)
    embed.add_field(name='M.Def', value='795', inline=True)
    embed.add_field(name='P.Res', value='NORMAL: 15;\nINTERRUPTED: 10;', inline=True)
    embed.add_field(name='M.Res', value='NORMAL: 15;\nINTERRUPTED: 10;', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:3  M:1', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='400', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Shoulder (BOW),\nRight Arm (KTN),\nBack/Tip of Tentacle Hair (Vatudo's Tactile Hair)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/vatudo2.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='ragingdragonbovinari', aliases=['bovinari'])
async def bovinari(ctx):
    embed = discord.Embed(title='')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Little Shrine of Grace: Sanctuary')
    embed.add_field(name='Element', value='Wind', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='938', inline=True)
    embed.add_field(name='M.Def', value='938', inline=True)
    embed.add_field(name='P.Res', value='PH1: 10;\nPH2: 20;\nPH2+FT: 30;', inline=True)
    embed.add_field(name='M.Res', value='PH1: 10;\nPH2: 20;\nPH2+FT: 30;', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:5  M:5', inline=True)
    embed.add_field(name='Crit Res', value='PH1: 20;\nPH2: 25;\nPH2+FT: 30;', inline=True)
    embed.add_field(name='Flee', value='400', inline=True)
    embed.add_field(name='Retaliation', value="", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (Bovinari Crystal Horn),\nRoot of Tail (THS),\nTip of Tail (HB)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/bovinari.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)



@bot.command(name='humida', aliases=['humi'])
async def humida(ctx):
    embed = discord.Embed(title='Humida')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Giant Plastida')
    embed.add_field(name='Element', value='HUMIDA/BALL: [MODE1: Water; MODE2: Dark];', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='HUMIDA: [MODE1: 1897; MODE2: 813];\nBALL: [MODE1: 1500; MODE2: 500]', inline=True)
    embed.add_field(name='M.Def', value='HUMIDA: [MODE1: 813; MODE2: 1897];\nBALL: [MODE1: 500; MODE2: 1500]', inline=True)
    embed.add_field(name='P.Res', value='HUMIDA: [MODE1: 30; MODE2: 10];\nBALL: [MODE1: 15; MODE2: 5]', inline=True)
    embed.add_field(name='M.Res', value='HUMIDA: [MODE1: 10; MODE2: 30];\nBALL: [MODE1: 5; MODE2: 15]', inline=True)
    embed.add_field(name='Prorate', value='N:5  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='HUMIDA: [MODE1: 30; MODE2: 40]\nBALL: 20', inline=True)
    embed.add_field(name='Flee', value='HUMIDA: 530;\nBALL: 200', inline=True)
    embed.add_field(name='Retaliation', value="FTS:\nHUMIDA:\nMODE1: Immune to S\nMODE2: Immune to T\nDuring PH2: Also Immune to F\n\nBALLS: FTS is OK", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nBack Left Shoulder (MD,visible at a distance),\nRight Arm (BWG),\nTorso (Dire Coenubia Crystal)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/humida.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='torexesa', aliases=['torex'])
async def torexesa(ctx):
    embed = discord.Embed(title='Torexesa')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='13', inline=True)
    embed.add_field(name='MQ Locked', value='Yes(Area Lock)', inline=True)
    embed.add_field(name='Map', value='Aquacity: Parliament Hall')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='1143', inline=True)
    embed.add_field(name='M.Def', value='1143', inline=True)
    embed.add_field(name='P.Res', value='PH1/PH2/PH3: 20;\nPH4: -15', inline=True)
    embed.add_field(name='M.Res', value='PH1/PH2/PH3/PH4: 20', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='PH1/PH2/PH3: 35;\nPH4: 100', inline=True)
    embed.add_field(name='Flee', value='610', inline=True)
    embed.add_field(name='Retaliation', value="4 Phases (4 HP bars)\n\nFTS:\nF: Immune during PH2 and PH4\nT: OK\nS: Immune during PH1, PH3, and PH4\n\nPH4:\nForced minimum damage of 9999\n\nPhase Transitions:\nFor every phase transition, the boss temporarily gains [Invincible]", inline=False)
    embed.add_field(name='Parts Destruction:', value="None", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/torexesa.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)



############################# MAIN QUEST BAB 14 ############################


@bot.command(name='mulgoon', aliases=['mulgon'])
async def mulgoon(ctx):
    embed = discord.Embed(title='Mulgoon')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Menabra Plains')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='MULGOON_LEFT_HAND: 1097;\nMULGOON_RIGHT_HAND: 1097;\nGARPUS: 810;\nANESTRO: 675', inline=True)
    embed.add_field(name='M.Def', value='MULGOON_LEFT_HAND: 1097;\nMULGOON_RIGHT_HAND: 1097;\nGARPUS: 810;\nANESTRO: 675', inline=True)
    embed.add_field(name='P.Res', value='MULGOON_LEFT_HAND: [PH1: 0; PH2-PH4: 10];\nMULGOON_RIGHT_HAND: 10;\nGARPUS: 10;\nANESTRO: 10', inline=True)
    embed.add_field(name='M.Res', value='MULGOON_LEFT_HAND: [PH1: 0; PH2-PH4: 10];\nMULGOON_RIGHT_HAND: 10;\nGARPUS: 10;\nANESTRO: 10', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='MULGOON_LEFT_HAND: 40;\nMULGOON_RIGHT_HAND: 40;\nGARPUS: 25;\nANESTRO: 25', inline=True)
    embed.add_field(name='Flee', value='MULGOON_LEFT_HAND: 420;\nMULGOON_RIGHT_HAND: 420;\nGARPUS: 220;\nANESTRO: 620', inline=True)
    embed.add_field(name='Retaliation', value="FTS:\bMULGOON LEFT & RIGHT HAND: Immune to FT. S is OK.\bGARPUS/ANESTRO: FTS OK", inline=False)
    embed.add_field(name='Parts Destruction:', value="6 Parts:\n3 Fingers on Left Mulgoon Hand,\n3 Fingers on Right Mulgoon Hand", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/mulgoon.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)



@bot.command(name='deformis', aliases=['defor'])
async def deformis(ctx):
    embed = discord.Embed(title='Deformis')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Eumano Village Ruins: Central')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='PH1: 830;\nPH2: 208', inline=True)
    embed.add_field(name='M.Def', value='PH1: 830;\nPH2: 208', inline=True)
    embed.add_field(name='P.Res', value='11', inline=True)
    embed.add_field(name='M.Res', value='11', inline=True)
    embed.add_field(name='Prorate', value='N:3  P:3  M:3', inline=True)
    embed.add_field(name='Crit Res', value='30', inline=True)
    embed.add_field(name='Flee', value='PH1: 208;\nPH2: 830', inline=True)
    embed.add_field(name='Retaliation', value="PH1:\nFS OK.\nRetaliates to T\n\n\nPH2:\nT is OK. Retaliates to FS.\nRetaliation:\nBoss releases a straight line laser (M, Mana Explosion, full map range) while rotating 330 deg CW.\nThe boss is immune to FTS during this retaliation.\nThe safe area during this retaliation is next to the right edge of the straight line AOE.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nLeft Arm,\nRight Arm,\nBack (ARROW, Corroded Petal, Easy to see when Tumbled)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/deformis.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='menti', aliases=['men'])
async def menti(ctx):
    embed = discord.Embed(title='Menti')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Umidus Valley: Area 3Umidus Valley: Area 3')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='3360', inline=True)
    embed.add_field(name='M.Def', value='3360', inline=True)
    embed.add_field(name='P.Res', value='NORMAL: 51;\nBREAK+HEAD: 11;', inline=True)
    embed.add_field(name='M.Res', value='NORMAL: 51;\nBREAK+HEAD: 11;', inline=True)
    embed.add_field(name='Prorate', value='N:2  P:2  M:3', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='410', inline=True)
    embed.add_field(name='Retaliation', value="FT: Boss's P/MRES become 99% while interrupted\nS: Immune\n\nIgnite: Damage to boss +25%FT: Boss's P/MRES become 99% while interrupted\nS: Immune\n\nIgnite: Damage to boss +25%\n\nBreaking the boss's head reduces its resistances by 40%Breaking the boss's head also causes it to immediately move on to the next attack pattern.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead (visible at ~4m from the front, F is more effective, Inlaid Purple Eye),\nBody,\nTail", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/menti.pnghttps://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/menti.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='biskyva', aliases=['bis'])
async def biskyva(ctx):
    embed = discord.Embed(title='biskyva')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='No(World Lock)', inline=True)
    embed.add_field(name='Map', value='Aquastida: Central')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='1130', inline=True)
    embed.add_field(name='M.Def', value='1130', inline=True)
    embed.add_field(name='P.Res', value='12', inline=True)
    embed.add_field(name='M.Res', value='12', inline=True)
    embed.add_field(name='Prorate', value='N:6  P:4  M:10', inline=True)
    embed.add_field(name='Crit Res', value='40', inline=True)
    embed.add_field(name='Flee', value='510', inline=True)
    embed.add_field(name='Retaliation', value="FTS: OK for all phases\nBody Part Destruction:\nHead: M/DEF+25%\nTorso: M/DEF-12.5%\nTail: M/DEF-12.5%", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead,\nTorso (Corroded Green Crystal),\nTail", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/biskyva.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='piscruva', aliases=['pisc'])
async def piscruva(ctx):
    embed = discord.Embed(title='Piscruva')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Vicus Mutans: Square')
    embed.add_field(name='Element', value='Water', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='1145', inline=True)
    embed.add_field(name='M.Def', value='715', inline=True)
    embed.add_field(name='P.Res', value='PH1: 15;\nPH2: [SHELL: 45; NORMAL: 15];', inline=True)
    embed.add_field(name='M.Res', value='PH1: 10;\nPH2: [SHELL: 30; NORMAL: 10];', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:3  M:5', inline=True)
    embed.add_field(name='Crit Res', value='0', inline=True)
    embed.add_field(name='Flee', value='', inline=True)
    embed.add_field(name='Retaliation', value="2 Phases\nPhase transition @80% HP\n\nWhen transitioning to PH2, the boss will temporarily gain [Invincible] and switch to SHELL mode.\n\nFTS:\nPH1: FTS OK\nPH2:\nSHELL: F OK. Immune to TS.\nNORMAL: FT OK. Immune to S.", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nHead,\nLower Body,\nTai", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/piscruva.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)


@bot.command(name='supremeevilcrystalbeast', aliases=['supreme'])
async def supremeevilcrystalbeast(ctx):
    embed = discord.Embed(title='Supreme Evil Crystal Beast')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='14', inline=True)
    embed.add_field(name='MQ Locked', value='Yes', inline=True)
    embed.add_field(name='Map', value='Lixaro Ghost Town: Mansion')
    embed.add_field(name='Element', value='Dark', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='910', inline=True)
    embed.add_field(name='M.Def', value='1013', inline=True)
    embed.add_field(name='P.Res', value='20', inline=True)
    embed.add_field(name='M.Res', value='20', inline=True)
    embed.add_field(name='Prorate', value='N:1  P:1  M:1', inline=True)
    embed.add_field(name='Crit Res', value='35', inline=True)
    embed.add_field(name='Flee', value='440', inline=True)
    embed.add_field(name='Retaliation', value="3 Phases.\nPhase Transition at 80% and 40% HP\n\nFTS:\nPH1: Immune to FS. T is OK\nPH2: Immune to T. FS are OK\nPH3: FTS OK\n\nPhase Transition:\nBoss temporarily gains [Invincible] and turns Light Green.\nWhile the boss is Light Green, its HP is locked.\nHitting the boss 10x (PH1→PH2) or 15x (PH2→PH3) will cause it to switch back to normal mode (Purple)", inline=False)
    embed.add_field(name='Parts Destruction:', value="2 Parts:\nBody (Orichalcum Ore),\nLeft Arm (Evil Crystal Beat Direclaw)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/supremeecb.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

###################### MAIN QUEST BAB 15 #########################

@bot.command(name='bakuzan', aliases=['baku'])
async def bakuzan(ctx):
    embed = discord.Embed(title='Bakuzan')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='15', inline=True)
    embed.add_field(name='MQ Locked', value='No (World Lock)', inline=True)
    embed.add_field(name='Map', value='Afval Uplands: Summit')
    embed.add_field(name='Element', value='Neutral', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='1460', inline=True)
    embed.add_field(name='M.Def', value='585', inline=True)
    embed.add_field(name='P.Res', value='10', inline=True)
    embed.add_field(name='M.Res', value='10', inline=True)
    embed.add_field(name='Prorate', value='N:10  P:20  M:20', inline=True)
    embed.add_field(name='Crit Res', value='BAKUZAN: 35;\nBANDIT_LACKEY: 20;', inline=True)
    embed.add_field(name='Flee', value='440', inline=True)
    embed.add_field(name='Retaliation', value="The boss is accompanied by 4 BANDIT_LACKEY mobs.\nThe boss retaliates with an 11m radius, enemy-centered spike bed (MaxHP FR) every time 10 BANDIT_LACKEY mobs are defeated.\nDefeated BANDIT_LACKEY mobs respawn after 2 sec of being defeated.\nBANDIT_LACKEY in Normal mode is 30700", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nFront Lenses (ADD),\nLeft Leg (Black Steel),\nBack (ARM)", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/bakuzan.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

####################### Event boss ################################


####################### Hanami Event #################################

@bot.command(name='baavgai', aliases=['baav'])
async def baavgai(ctx):
    embed = discord.Embed(title='Baavgai')
    embed.add_field(name='Level boss', value='Normal : ', inline=True)
    embed.add_field(name='MQ Chapter', value='Hanami Event', inline=True)
    embed.add_field(name='MQ Locked', value='No', inline=True)
    embed.add_field(name='Map', value='Mt. Sakuraten Summit')
    embed.add_field(name='Element', value='Earth', inline=True)
    embed.add_field(name='Base HP', value='', inline=True)
    embed.add_field(name='Base EXP', value='', inline=True)
    embed.add_field(name='P.Def', value='E: [PH1: 600; PH2: 900];\nN: [PH1: 660; PH2: 990];\nH: [PH1: 720; PH2: 1080];\nVH: [PH1: 3780; PH2: 4170]', inline=True)
    embed.add_field(name='M.Def', value='E: [PH1: 800; PH2: 1200];\nN: [PH1: 880; PH2: 1320];\nH: [PH1: 960; PH2: 1440];\nVH: [PH: 4040; PH2: 4560]', inline=True)
    embed.add_field(name='P.Res', value='E: [PH1: 8; PH2: 10];\nN: [PH1: 8; PH2: 13];\nH: [PH1: 9; PH2: 14];\nVH: [PH1: 10; PH2: 15]', inline=True)
    embed.add_field(name='M.Res', value='E: [PH1: 8; PH2: 10];\nN: [PH1: 8; PH2: 13];\nH: [PH1: 9; PH2: 14]\nVH: [PH1: 10; PH2: 15]', inline=True)
    embed.add_field(name='Prorate', value='N:15  P:15  M:10', inline=True)
    embed.add_field(name='Crit Res', value='E: 20;\nN: 30;\nH: 30;\nVH: 30;', inline=True)
    embed.add_field(name='Flee', value='E: [PH1: 370; PH2: 400];\nN: [PH1: 400; PH2: 600];\nH: [PH1: 430; PH2: 645];\nVH: [PH1: 460; PH2: 690];', inline=True)
    embed.add_field(name='Retaliation', value="E to VH:\n2 phases; transitions @50% HP\nDamage above 50% of the boss's HP is ignored\n\n@50% HP, the boss temporarily gains [Invincible] and releases rotating fins (maxHP FR)Number of fins released depends on the difficulty:\nE: 1x (abs Item Disabled)\nN: 2x (abs Item Disabled, Silence)\nH/VH: 4x (abs Item Disabled, Silence, Bleed)\n\nThe boss also releases fins as part of its normal attack patterns\nImmune to FTS while releasing fins\n\nVH:\nThe boss has two modes: MODE1 & MODE2.\nIf a part is broken, boss will release a no warning FR attack (fixed 1 damage, abs Knockback) to all players then go to MODE2.\nWhile in MODE2, damage limit is 100k\nIf the boss receives a total of 1M damage while in MODE2, it will go back to MODE1\n[Invincible] while switching modes\nBreaking parts reduces the boss's defenses:\nRight hand: -3k DEF\nSword hilt: -3k MDEF\n\nFTS Retal:\n\nE to H\nFT: OK\nS: Immune\n\nVH:\nImmune to S\nMODE1: FT is OK\nMODE2 (DMG Limit): Retaliates to FT with a no warning attack\nto all players (maxHP FR, abs Mana Explosion)", inline=False)
    embed.add_field(name='Parts Destruction:', value="3 Parts:\nRight Hand,\nSword Hilt Above Left Shoulder,\nLeft Side of Head", inline=False)
    embed.set_image(url='https://raw.githubusercontent.com/jrabella93/TSXen/main/images/boss/baavgai.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    embed.set_footer(text='FTS = Flinch/Tumble/Stun\nEASY = 0.1 * def | flee\nHARD = 2 x def | flee\nNIGHTMARE = 4 x def | flee\nULTIMATE = 6 x def | flee.')
    await ctx.send(embed=embed)

######################### Xtall MQ ######################################



@bot.command(name='xbosscolon', aliases=['xcolon'])
async def xbosscolon(ctx):
    embed = discord.Embed(title='Boss Colon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357539664520548392/image.png?ex=67f092d5&is=67ef4155&hm=a94a85fdf958886140ebb300255da2eff69a341fb9a864fd932fe4b9d6121444&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xexcavatedgolem', aliases=['xexcavated'])
async def xexcavatedgolem(ctx):
    embed = discord.Embed(title='Excavated  Golem')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357539790534217849/image.png?ex=67f092f3&is=67ef4173&hm=965af76b3757ac3bc39114c25769bf4bd62c081d60905ccccc577ca7db6ea8f5&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xeeriecrystal', aliases=['xeerie'])
async def xeeriecrystal(ctx):
    embed = discord.Embed(title='Eerie Crystal')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357539911061999836/image.png?ex=67f09310&is=67ef4190&hm=9af9238a8d9e3e982dadd58a5dec16818d9158a43c047eba100c5888a2d11e04&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xminotour', aliases=['xmino'])
async def xminotaur(ctx):
    embed = discord.Embed(title='Minotaur')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540020587855943/image.png?ex=67f0932a&is=67ef41aa&hm=815d648d7709e19cd8d11fe876d8e5d611bd7e535a0add2f3d1f455db1d21468&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xbrutaldragondecel', aliases=['xdecel'])
async def xbrutaldragondecel(ctx):
    embed = discord.Embed(title='Brutal Dragon Decel')
    embed.add_field(name='Upgrade', value='Decel>York>Tuscog>Black Shadow>Torexesa', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540141685670072/image.png?ex=67f09347&is=67ef41c7&hm=459e01fe49235d8c8441b657c01969f854db513af41089fc48e401f12ab93401&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



    ############################## Xtall BAB 2 #############################



@bot.command(name='xbbgoblin', aliases=['xgoblin'])
async def xbbgoblin(ctx):
    embed = discord.Embed(title="B.B. Goblin")
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540301807292596/image.png?ex=67f0936d&is=67ef41ed&hm=df1738c47d2336f6eb489a1778e6c5ac37f6d1e13bc02112e179640fed4287b8&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xflarevvolg', aliases=['xvolg'])
async def xflarevolg(ctx):
    embed = discord.Embed(title='Flare Volg')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540417041596446/image.png?ex=67f09389&is=67ef4209&hm=72157dc1a863031f442ccf26044a6af3c3f968a7c820d63a8b957494f7b584c3&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwarmonger', aliases=['xwarmo'])
async def xwarmonger(ctx):
    embed = discord.Embed(title='Warmonger')
    embed.add_field(name='Upgrade', value='Warmonger>Proto Leon>King Piton>Igneus>', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357655056274423879/image.png?ex=67f0fe4d&is=67efaccd&hm=9573f35054b999494ddfa3777caa3e64bfeaeac42ed1c2c4c36b770b35b96a28&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



@bot.command(name='xmauez', aliases=['xmauz'])
async def xmauez(ctx):
    embed = discord.Embed(title='Mauez')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540526018003064/image.png?ex=67f093a3&is=67ef4223&hm=83a02330405d8d01b165512d9e89d5b17eb952b56af44d336d09b1e7d1583980&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xooze', aliases=['xoze'])
async def xooze(ctx):
    embed = discord.Embed(title='Ooze')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540616401195009/image.png?ex=67f093b8&is=67ef4238&hm=da09882f8a9d9b5262eb4aeaba0361622fe39ef362f19b9d756648a6f4cc8888&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xganglef', aliases=['xgang'])
async def xganglef(ctx):
    embed = discord.Embed(title='Ganglef')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540743282954482/image.png?ex=67f093d7&is=67ef4257&hm=26ff701db293ad4bd4c2a511e6a2fa532676d300c0703acd4bbbd4a5944ac55e&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



############################### Xtall BAB 3 ###################################



@bot.command(name='xdemonsgate', aliases=['xgate'])
async def xdemonsgate(ctx):
    embed = discord.Embed(title="Demon's Gate")
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540850854400072/image.png?ex=67f093f0&is=67ef4270&hm=c51a543919fdfa24e45cf32898e08720ae82295bc0b7ebf936d75b9a63e69020&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbossroga', aliases=['xroga'])
async def xbossroga(ctx):
    embed = discord.Embed(title='Boss Roga')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357540930004975648/image.png?ex=67f09403&is=67ef4283&hm=e630b56b9294f9a116ffd35828e903cc5ce368d38a14ff6ca3e4e20a9387795b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xancientempress', aliases=['xempress'])
async def xancientempress(ctx):
    embed = discord.Embed(title='Ancient Empress')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541074289295612/image.png?ex=67f09426&is=67ef42a6&hm=92493ee7a29e08bdf1eb8a89cec6dbc9a0b3facac49deb9b1f4038e747471df9&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmaskedwarrior', aliases=['xmasked'])
async def xmaskedwarrior(ctx):
    embed = discord.Embed(title='Masked Warrior')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541379903062256/image.png?ex=67f0946e&is=67ef42ee&hm=75254e683f46d983394fc54385161a242ccdb267801abcf82edac161e9d066ac&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xpillargolem', aliases=['xpillar'])
async def xpillargolem(ctx):
    embed = discord.Embed(title='Pillar Golem')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541514498150661/image.png?ex=67f0948e&is=67ef430e&hm=6aec14cf499b49c06354676b8530e2ce8665e20d589a652befa97412fa321456&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgrassdragonyelb', aliases=['xyelb'])
async def xgrassdragonyelb(ctx):
    embed = discord.Embed(title='Grass Dragon Yelb')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541640717467789/image.png?ex=67f094ad&is=67ef432d&hm=c3a509ccc4719cdbfbb7cd41b9fe1315b9bfc70f89acda7504cb027c71fbfc61&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xnurethoth', aliases=['xnure'])
async def xnurethoth(ctx):
    embed = discord.Embed(title='Nurethoth')
    embed.add_field(name='Upgrade', value='nurethoth>guignol>guard golem>piscruva', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541749253214349/image.png?ex=67f094c6&is=67ef4346&hm=89f7d76fba96caeaebc6b42d8e501e7031d4e879400db2dd69137072712c3846&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



############################# Xtall BAB 4 ########################################



@bot.command(name='xgespenst', aliases=['xgespen'])
async def xgespenst(ctx):
    embed = discord.Embed(title='Gespenst')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541864471003366/image.png?ex=67f094e2&is=67ef4362&hm=f91673005e0c96c461cd225dd58a8ad213e36225bbff004d58a9a02791681d38&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xastol', aliases=['xasto'])
async def xastol(ctx):
    embed = discord.Embed(title='Astol')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541941658652883/image.png?ex=67f094f4&is=67ef4374&hm=94990e634c11d57bb06b3f50b568ccda1de1a73b1814c0f90d7b6d3d566ed219&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xforestwolf', aliases=['xforest'])
async def xrorestwolf(ctx):
    embed = discord.Embed(title='Forest Wolf')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542026052374728/image.png?ex=67f09508&is=67ef4388&hm=93cb4ec7c8e6c600137d6b37b1adb4ca496669f8790232e25afa9a157030d47d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xforestia', aliases=['xforesti'])
async def xforestia(ctx):
    embed = discord.Embed(title='Forestia')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542150979457126/image.png?ex=67f09526&is=67ef43a6&hm=45e92257d5a24d60de20675e7b85d5ec3cb7cb8f4d2d2aa8892e2a50efc240eb&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xjaderaptor', aliases=['xjade'])
async def xjaderaptor(ctx):
    embed = discord.Embed(title='Jade Raptor')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542519373565962/image.png?ex=67f0957e&is=67ef43fe&hm=86c5b466df995fd7810e77a58315ad2686c6e4bd950390a7e0d398756de53c19&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgoovua', aliases=['xgovua'])
async def xgoovua(ctx):
    embed = discord.Embed(title='Goovua')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542731060346920/image.png?ex=67f095b1&is=67ef4431&hm=59deccccaa08289c208c581b61c07b0124d0e454d0dee4b4ffa8d681687cf8eb&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xscrader', aliases=['xscrade'])
async def xscrader(ctx):
    embed = discord.Embed(title='Scrader')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542837838676088/image.png?ex=67f095ca&is=67ef444a&hm=6aae6a99e98016fa3c2d76b9a8d905c78b2e4d4d128b7f96923ac1927152d275&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xblackknightofdelusion', aliases=['xbkod'])
async def xblackknightofdelusion(ctx):
    embed = discord.Embed(title='Black Knight of Delusion')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357542913369833493/image.png?ex=67f095dc&is=67ef445c&hm=6037853e608f4cc1bcb3aaf03ffbd2d336d92d2ac229951b2ea7d5e62be3e218&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xevilcrystalbeast', aliases=['xecb'])
async def xevilcrystalbeast(ctx):
    embed = discord.Embed(title='Evil Crystal Beast')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543021834407936/image.png?ex=67f095f6&is=67ef4476&hm=10e032c9c37ca6b76c862a17ee8b9b8bafd0b6f41f97eb4fe22b5a479d54bc22&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)




#################### Xtall BAB 5 ############################




@bot.command(name='xcerberus', aliases=['xcerbe'])
async def xcerberus(ctx):
    embed = discord.Embed(title='Cerberus')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543140910956625/image.png?ex=67f09612&is=67ef4492&hm=6c145a442c701b4311a1447cc533ce7ff606e1411d00b9834daab58bb72ab8b6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xzolban', aliases=['xzol'])
async def xzolban(ctx):
    embed = discord.Embed(title='Zolban')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543266492616955/image.png?ex=67f09630&is=67ef44b0&hm=582c02e27ad9f6201dab59644febe581d8d58785cb6937ba4e973f8004b7051d&https://cdn.discordapp.com/attachments/696678783465553990/1357543266492616955/image.png?ex=67f09630&is=67ef44b0&hm=582c02e27ad9f6201dab59644febe581d8d58785cb6937ba4e973f8004b7051d&https://cdn.discordapp.com/attachments/696678783465553990/1357543266492616955/image.png?ex=67f09630&is=67ef44b0&hm=582c02e27ad9f6201dab59644febe581d8d58785cb6937ba4e973f8004b7051d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xaranea', aliases=['xara'])
async def xaranea(ctx):
    embed = discord.Embed(title='Aranea')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543352756731975/image.png?ex=67f09645&is=67ef44c5&hm=dcd6443b865131f82c8899592eb40d9ac6a6810f8d34a2cc3c5e25dd8563ada8&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbexiz', aliases=['xbex'])
async def xbexiz(ctx):
    embed = discord.Embed(title='Bexiz')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543429772677291/image.png?ex=67f09657&is=67ef44d7&hm=c2f64ccd5bf328e12e296a0ef3fcec7a6eefbed1730af86039ef68414f1f17c1&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='ximitator', aliases=['xtator'])
async def ximitator(ctx):
    embed = discord.Embed(title='Imitator')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543675260833812/image.png?ex=67f09692&is=67ef4512&hm=e4d8c2230bdae83fd5c366f19d7d9a0c3e57e7e3c374a3b5cffc5f3cc297525f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='ximitacia', aliases=['ximi'])
async def ximitacia(ctx):
    embed = discord.Embed(title='Imitacia')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543743493771324/image.png?ex=67f096a2&is=67ef4522&hm=d714166cbb0b987eedc693620233e106bd8def8925a93cd6f987184456ff4e50&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmemecoleous', aliases=['xmeme'])
async def xmemecoleous(ctx):
    embed = discord.Embed(title='Memecoleous')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551623295078501/image.png?ex=67f09df9&is=67ef4c79&hm=37770ac27c0413baeab6d39025a5fd8602cea1b986cbb42b482db92603cf2f3d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xinzanio', aliases=['xinza'])
async def xinza(ctx):
    embed = discord.Embed(title='Inzanio')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357543950763688169/image.png?ex=67f096d3&is=67ef4553&hm=636d3c5b422f141e9bb0e860d86d4ff62a1aca9063cd7b2e4c065b8fa02481bf&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtwilightdragon', aliases=['xtwilight'])
async def xtwilightdragon(ctx):
    embed = discord.Embed(title='Twilight Dragon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544024101228595/image.png?ex=67f096e5&is=67ef4565&hm=02dc5394ccd9cbc81c94486d4076393894120ef10ef0fc61f3c77e3dfccc9719&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 6 ###########################################




@bot.command(name='xiconos', aliases=['xico'])
async def xiconos(ctx):
    embed = discord.Embed(title='Iconos')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544100982689842/image.png?ex=67f096f7&is=67ef4577&hm=cbbbc40a4db933996f5dce7168babfb6e5d1e57b2868d83a068aeeafeed632d9&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xifrid', aliases=['xifrit'])
async def xifrid(ctx):
    embed = discord.Embed(title='Ifrid')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544186185777443/image.png?ex=67f0970b&is=67ef458b&hm=d604e0e39cc155d72bc8daa5e1f0ca617a84586011e2db3c307f91a8e605818a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xyork', aliases=['xyor'])
async def xyork(ctx):
    embed = discord.Embed(title='York')
    embed.add_field(name='Upgrade', value='Decel>York>Tuscog>Black Shadow>Torexesa', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544276061323345/image.png?ex=67f09721&is=67ef45a1&hm=7e916951a18fc11598591c3a4ee1bacfd71b5c0747ed52a9b1d2fd7e782afe77&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xprotoleon', aliases=['xproto'])
async def xprotoleon(ctx):
    embed = discord.Embed(title='Proto Leon')
    embed.add_field(name='Upgrade', value='Warmonger>Proto Leon>King Piton>Igneus>', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544365819433192/image.png?ex=67f09736&is=67ef45b6&hm=31e35892242e227ace1c3ed53326f84e649945063cdbb25a2327f284f694c041&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtyrantmachina', aliases=['xtyrant'])
async def xtyrantmachina(ctx):
    embed = discord.Embed(title='Tyrant Machina')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544479841845459/image.png?ex=67f09751&is=67ef45d1&hm=474f8f9e539b12a0c6d68666bfd887bda8e9aec58aa88efb910c848ac4bc3136&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmoztomachina', aliases=['xmozto'])
async def xmoztomachina(ctx):
    embed = discord.Embed(title='Mozto Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544551296012410/image.png?ex=67f09762&is=67ef45e2&hm=bd3a3ac53d8fc090900027ca8a4f4cf656ac4722e4dc54975da3659a3781fc55&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 7 ###########################################



@bot.command(name='xlalvada', aliases=['xlal'])
async def xlalvada(ctx):
    embed = discord.Embed(title='Lalvada')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544643289546813/image.png?ex=67f09778&is=67ef45f8&hm=70a6bab0f66d8c15860a4ab6585acfc516e292e084c02039ff7df45e07fb4939&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xzahhakmachina', aliases=['xzahhak'])
async def xzahhakmachina(ctx):
    embed = discord.Embed(title='Zahhak Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544734901665847/image.png?ex=67f0978e&is=67ef460e&hm=87871ef63ce04b49b926fbcd8aa4b8d044e6625910a0c78401e4364576dd6a86&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xguignol', aliases=['xguig'])
async def xguignol(ctx):
    embed = discord.Embed(title='Guignol')
    embed.add_field(name='Upgrade', value='nurethoth>guignol>guard golem>piscruva', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544867940667493/image.png?ex=67f097ae&is=67ef462e&hm=465c246dfb865e002bb5bf74881f3fbeb43ee51d9cf8aaaee236fc60ecc24150&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgwaimol', aliases=['xgwai'])
async def xgwaimol(ctx):
    embed = discord.Embed(title='Gwaimol')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357544989793718363/image.png?ex=67f097cb&is=67ef464b&hm=dc49dde35240116f666dcd4926e12d9757089029218b5023c2636904defe6b71&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xultimatemachina', aliases=['xultimate'])
async def xultimatemachina(ctx):
    embed = discord.Embed(title='Ultimate Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545065957818439/image.png?ex=67f097dd&is=67ef465d&hm=e8ecc1e4257a1436946de5c96290dd4d90362b15c3673aef82a029388194ef88&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xornlarf', aliases=['xorn'])
async def xornlarf(ctx):
    embed = discord.Embed(title='Ornlarf')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545163202756798/image.png?ex=67f097f4&is=67ef4674&hm=c8f46279e7079c5940e63c30986a83765bfba5b5e6ed1743deb5a9130159a257&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvenena', aliases=['xnena'])
async def xvenena(ctx):
    embed = discord.Embed(title='Venena')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545269893533736/image.png?ex=67f0980e&is=67ef468e&hm=c905a16ef3bf1184c34779fdb3eb44a42e9acb1e35051ead25786eec1bfedd67&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmatonsword', aliases=['xmaton'])
async def xmatonsword(ctx):
    embed = discord.Embed(title='Maton Sword')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545341943025936/image.png?ex=67f0981f&is=67ef469f&hm=18c21398dbd2c3b308ddc44ae8a58601cb0517c702247ee6783f23657985a870&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdemonicquasar', aliases=['xdemonic'])
async def xdemonicquasar(ctx):
    embed = discord.Embed(title='Demonic Quasar')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545474781089932/image.png?ex=67f0983f&is=67ef46bf&hm=0f74385ecc2eb5d0b7df842cae009ad66a9a22efe4907bf7035c0e66874c5642&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


########################### Xtall BAB 8 ###########################################


@bot.command(name='xshampy', aliases=['xsham'])
async def xshampy(ctx):
    embed = discord.Embed(title='Shampy')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545581274202112/image.png?ex=67f09858&is=67ef46d8&hm=5f67880a597b93e3e3f3d747fbda50c992be90bf124a447de12bdc6a67bb2cb7&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcrystaltitan', aliases=['xtitan'])
async def xcrystaltitan(ctx):
    embed = discord.Embed(title='Crystal Titan')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545685528084621/image.png?ex=67f09871&is=67ef46f1&hm=fd62a95422ca2dcb8f27546ce5c3e9c04072b123e5b403cb06506dcec938fe64&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmomfluck', aliases=['xmom'])
async def xmomfluck(ctx):
    embed = discord.Embed(title='Mom Fluck')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545802204975204/image.png?ex=67f0988d&is=67ef470d&hm=5fef36d1cbed82080f1c79fb9cabbedf5cc326e459a78c57450ba12b500e5322&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xzelbuse', aliases=['xzel'])
async def xzelbuse(ctx):
    embed = discord.Embed(title='Zelbuse')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549331795804221/image.png?ex=67f09bd6&is=67ef4a56&hm=ab4d5120b7add4160b9377fc1117f1fedfd241cfa808e9e0cdf5a519216741af&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xseelezauga', aliases=['xseele'])
async def xseelezauga(ctx):
    embed = discord.Embed(title='Seele Zauga')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545964780523581/image.png?ex=67f098b3&is=67ef4733&hm=b540c43fa5670f684e5c683568c2fc2de02f886bd5e611d68037a364f8a416cf&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmardula', aliases=['xmardu'])
async def xmardula(ctx):
    embed = discord.Embed(title='Mardula')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357545857335165090/image.png?ex=67f0989a&is=67ef471a&hm=a8f3ddd8d698cd71041add4ececa4c086bc07845f6befdda5326c0fd9010ca3c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xkingpiton', aliases=['xpiton'])
async def xkingpiton(ctx):
    embed = discord.Embed(title='King Piton')
    embed.add_field(name='Upgrade', value='Warmonger>Proto Leon>King Piton>Igneus>', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357546021156032542/image.png?ex=67f098c1&is=67ef4741&hm=32495bffa078331628a0440a8e2d44c43bf0a6fac0df66bccddc772ac55d6036&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xfinstern', aliases=['xfins'])
async def xfinstern(ctx):
    embed = discord.Embed(title='Finstern the Dark Dragon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357546085127553197/image.png?ex=67f098d0&is=67ef4750&hm=130c75aebd8aebc9421e7ca3948e9551665c67e18b24d82617b8e10f20b87891&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 9 ###########################################




@bot.command(name='xtuscog', aliases=['xtus'])
async def xtuscog(ctx):
    embed = discord.Embed(title='Tuscog')
    embed.add_field(name='Upgrade', value='Decel>York>Tuscog>Black Shadow>Torexesa', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357546674981044264/image.png?ex=67f0995d&is=67ef47dd&hm=46c925d859bcec3c25ed9895dcf1e1f6be941c80a50fc4c5e0f62d996f7c6e12&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xerodedpilz', aliases=['xpilz'])
async def xerodedpilz(ctx):
    embed = discord.Embed(title='Eroded Pilz')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547316847968256/image.png?ex=67f099f6&is=67ef4876&hm=92b32ba3a2d15f0b63f7bdbd3fdd4099a4e8eacfe77e82dfc69e3cebe1deaead&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xpyxtica', aliases=['xpyx'])
async def xpyxtica(ctx):
    embed = discord.Embed(title='Pyxtica')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547396753526997/image.png?ex=67f09a09&is=67ef4889&hm=686b526469aa98bf49848cc4d016e5ebbe6880e70d9d4ff50cf2f88bab4c9a85&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xkuzto', aliases=['xkuz'])
async def xkuzto(ctx):
    embed = discord.Embed(title='Kuzto')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547471403749606/image.png?ex=67f09a1b&is=67ef489b&hm=f2179de3da0d14b222bc3c66249494de85dd9386731d2f48ef8197429ae87146&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsapphireroga', aliases=['xsapphire'])
async def xsapphireroga(ctx):
    embed = discord.Embed(title='Sapphire Roga')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547594045456424/image.png?ex=67f09a38&is=67ef48b8&hm=9d7f70b46fdc3e8ce16fe339dababd2ad100d094e60a99237a06a0e0e4baf5d8&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgravicep', aliases=['xgravi'])
async def xgravicep(ctx):
    embed = discord.Embed(title='Gravicep')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547682381697055/image.png?ex=67f09a4d&is=67ef48cd&hm=f0d6747d53f3d04d985ece4e2661d07fde13aa5b3937c1e1e40c32fd5a4382ad&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xrepthon', aliases=['xrep'])
async def xrepthon(ctx):
    embed = discord.Embed(title='Repthon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357547836899590275/image.png?ex=67f09a72&is=67ef48f2&hm=f675b3b1f30e536ed791007355b9c2648d85b990cae190ed19d5727f9f93983f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvenenameta', aliases=['xnemet'])
async def xvenenameta(ctx):
    embed = discord.Embed(title='Venena II')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548030705930420/image.png?ex=67f09aa0&is=67ef4920&hm=d0ebf615356b217585a05d753c593bd95fc7eb4014b5303ebfb78cbb87e84c2d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 10 ###########################################




@bot.command(name='xpisteus', aliases=['xpis'])
async def xpisteus(ctx):
    embed = discord.Embed(title='Pisteus')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548167956267049/image.png?ex=67f09ac1&is=67ef4941&hm=45df5fb0fc0ff88a472becd412ef23d3dbf91c360542ce4bf60d73fed79ccae5&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



@bot.command(name='xarachnidemon', aliases=['xarac'])
async def xarachnidemon(ctx):
    embed = discord.Embed(title='Arachnidemon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548248411406336/image.png?ex=67f09ad4&is=67ef4954&hm=93a35fe6911f2b55cc58ae74aca9c479bf6eeaba0c9621b5ac1115eb1bef26dc&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xblackshadow', aliases=['xbs'])
async def xblackshadow(ctx):
    embed = discord.Embed(title='Black Shadow')
    embed.add_field(name='Upgrade', value='Decel>York>Tuscog>Black Shadow>Torexesa', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548328660762725/image.png?ex=67f09ae7&is=67ef4967&hm=6ce015835bfab62ea857831a84462ae588ed219212f259632abe34e1c176e94e&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xhexter', aliases=['xhex'])
async def xhexter(ctx):
    embed = discord.Embed(title='Hexter')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548402321264751/image.png?ex=67f09af9&is=67ef4979&hm=ba97da3edea4e3e8658165fa8b11478fc2a162c080901c6d89752158f2814f49&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xirestida', aliases=['xires'])
async def xirestida(ctx):
    embed = discord.Embed(title='Irestida')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548473007865866/image.png?ex=67f09b09&is=67ef4989&hm=fb04e21c08071d1831bb7c4d7b22fa916c17b86826cd090d5c22ff3a12cd752a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 11 ###########################################




@bot.command(name='xreliza', aliases=['xclawedironwitch'])
async def xreliza(ctx):
    embed = discord.Embed(title='Clawed Iron Witch')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548748544278718/image.png?ex=67f09b4b&is=67ef49cb&hm=166d29a32baba95c52ba117670fc690db36ff7640d2d1244128c9050c7e5cf7b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgemma', aliases=['xgem'])
async def xgemma(ctx):
    embed = discord.Embed(title='Gemma')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357548952299503876/image.png?ex=67f09b7c&is=67ef49fc&hm=e73efa2e5089bf63d7df7938b97f4e8e94fad598ce32bea1c741f38da233bcc3&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xferzen', aliases=['xferz'])
async def xferzen(ctx):
    embed = discord.Embed(title='Ferzen the Rock Dragon')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549038580400359/image.png?ex=67f09b90&is=67ef4a10&hm=5160c8fe7fa02d458c7a7a4dcf1d0da50bc9d2cea2f30e341f77ff60bc6f884f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xjuniordragonzyvio', aliases=['xzyvio'])
async def xjuniordragonzyvio(ctx):
    embed = discord.Embed(title='Junior Dragon Zyvio')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549130401976393/image.png?ex=67f09ba6&is=67ef4a26&hm=2c5f033dba3fc555ed3308a0efd04c37bfcc5edb558e3a9660cbddef4697ce30&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwardragonturba', aliases=['xturba'])
async def xwardragonturba(ctx):
    embed = discord.Embed(title='War Dragon Turba')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549211377340527/image.png?ex=67f09bba&is=67ef4a3a&hm=6499697400017003e200e76c0e2b31a17bc21353bff7f357753913d906682262&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvlamtheflamedragon', aliases=['xvlam'])
async def xvlam(ctx):
    embed = discord.Embed(title='Vlam the Flame Dragon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549398724186252/image.png?ex=67f09be6&is=67ef4a66&hm=5c8f861f459efa42336a5aaeb4e8fdd4c4d5ae168fb9a01e6cef063aea0f0aa7&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvelum', aliases=['xvlum'])
async def xvelum(ctx):
    embed = discord.Embed(title='Velum')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549457490710679/image.png?ex=67f09bf4&is=67ef4a74&hm=cb3ea57e0a1d8b3e156607d8e5766261c273cd9180644a485fa3e5d15e1d5f1c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xoculasignio', aliases=['xocul'])
async def xoculasignio(ctx):
    embed = discord.Embed(title='Oculasignio')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549514029928529/image.png?ex=67f09c02&is=67ef4a82&hm=2c3d417375517761f035d86103d99258efbbefc6700a2148afc608701059e498&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgordel', aliases=['xgord'])
async def xgordel(ctx):
    embed = discord.Embed(title='Gordel')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549569256198235/image.png?ex=67f09c0f&is=67ef4a8f&hm=baf5fa67af9870b1a1b59b6dc8abd10ea7d84dd247fa477a5ad8237aa4a94fa6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 12 ###########################################




@bot.command(name='xguardgolem', aliases=['xgg'])
async def xguardgolem(ctx):
    embed = discord.Embed(title='Guard Golem')
    embed.add_field(name='Upgrade', value='nurethoth>guignol>guard golem>piscruva', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549640416890990/image.png?ex=67f09c20&is=67ef4aa0&hm=b2452971fc7c2d4e756cbd6f20376c0059133af8baadaca96de980d036e7636d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xburningdragonigneus', aliases=['xigneus'])
async def xburningdragonigneus(ctx):
    embed = discord.Embed(title='Burning Dragon Igneus')
    embed.add_field(name='Upgrade', value='Warmonger>Proto Leon>King Piton>Igneus>', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549721039929364/image.png?ex=67f09c33&is=67ef4ab3&hm=25ae41d74ca720b3c60debae7951b7dd2d6c6ad2909db83778b6a8c9c6f4c20b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtrickterdragonmimyugon', aliases=['xmimyugon'])
async def xtrickterdragonmimyugon(ctx):
    embed = discord.Embed(title='Trickter Dragon Mimyugon')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357549846826844270/image.png?ex=67f09c51&is=67ef4ad1&hm=9478982997cb8e3ddce5188e8966c0244ea9683e05db827255b1e3004eac417f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwickeddragonfazzino', aliases=['xfazzino'])
async def xwickedragonfazzino(ctx):
    embed = discord.Embed(title='Wicked Dragon Fazzino')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357550673411178667/image.png?ex=67f09d16&is=67ef4b96&hm=7934a735e1946378f0669c57bce79a39b2c39eada323a4ffe103e34452e91563&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbrassdragonreguita', aliases=['xreguita'])
async def xbwassdragonreguita(ctx):
    embed = discord.Embed(title='Brass Dragon Reguita')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357550801958076476/image.png?ex=67f09d35&is=67ef4bb5&hm=7d27d44109f3924f826e67b0b00619135de4723887bbdf5283c95536cfb2bba6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwalican', aliases=['xwali'])
async def xwalican(ctx):
    embed = discord.Embed(title='Walican')
    embed.add_field(name='Upgrade', value='Boss Roga>Iconos>Ornlarf>Sapphire Roga>Ferzen>Walican', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357550881251266701/image.png?ex=67f09d48&is=67ef4bc8&hm=a662d022cde968eb465e1ae089fd11c2ee0d6b9eb8afff322b4a15e74fc85e19&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdominaredor', aliases=['xdomi'])
async def xdominaredor(ctx):
    embed = discord.Embed(title='Dominaredor')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551362296119417/image.png?ex=67f09dba&is=67ef4c3a&hm=a2eaad277a9e111edb9e515146f23ea361c19227fb8a5b15c7c4ec3acbcc264d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

################################

@bot.command(name='xvulture', aliases=['xvul'])
async def xvulture(ctx):
    embed = discord.Embed(title='Vulture')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551447809593525/image.png?ex=67f09dcf&is=67ef4c4f&hm=4739ea02cc1dc829c61c0d19dc44c44660bdbec05262cc0f30b90f165b1cd74c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



########################### Xtall BAB 13 ###########################################




@bot.command(name='xzapo', aliases=['xzap'])
async def xzapo(ctx):
    embed = discord.Embed(title='Zapo')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551789079265321/image.png?ex=67f09e20&is=67ef4ca0&hm=05703897106cb223234c85c9b39c2a2a799670f3e66d498c60b71862bbf5ec21&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xrudis', aliases=['xrudi'])
async def xrudis(ctx):
    embed = discord.Embed(title='Red Ash Dragon Rudis')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551868229849128/image.png?ex=67f09e33&is=67ef4cb3&hm=d90876fffe957f81bbd1349a563de46f2dfcd5c183578efdf70b471cf7ba851c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdonprofundo', aliases=['xdon'])
async def xdonprofundo(ctx):
    embed = discord.Embed(title='Don Profundo')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551946529116310/image.png?ex=67f09e46&is=67ef4cc6&hm=715cda09ec96493b907cdc5ce4229e6c660938b66bc1a3befe090895c889fbf3&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvatudo', aliases=['xvatu'])
async def xvatudo(ctx):
    embed = discord.Embed(title='Vatudo')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357552108735430726/image.png?ex=67f09e6c&is=67ef4cec&hm=cfe53dc93210bab34f82dd93ebeef1bfe7983c95cec4433307800c428fde1007&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbovinari', aliases=['xbovi'])
async def xbovinari(ctx):
    embed = discord.Embed(title='Raging Dragon Bovinari')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357552446972493824/image.png?ex=67f09ebd&is=67ef4d3d&hm=c94b502b19c8e2e010e4103f4f27eae6030b0e951618326946912c8b81601bed&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xhumida', aliases=['xhum'])
async def xhumida(ctx):
    embed = discord.Embed(title='Humida')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357552510822514851/image.png?ex=67f09ecc&is=67ef4d4c&hm=6232cd7ef93547dda2a7e2affbc6d0b4c5000a16abf3665cc5a33a5a5e57b850&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtorexesa', aliases=['xtorex'])
async def xtorexesa(ctx):
    embed = discord.Embed(title='Torexesa')
    embed.add_field(name='Upgrade', value='Decel>York>Tuscog>Black Shadow>Torexesa', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357552592485355700/image.png?ex=67f09ee0&is=67ef4d60&hm=36f2d85e414292126bebc2f4a4142059af3572c5408298bc3cc2d50efb59e32b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


########################### Xtall BAB 14 ###########################################



@bot.command(name='xmulgoon', aliases=['xmulgon'])
async def xmulgoon(ctx):
    embed = discord.Embed(title="mulgoon's Hand")
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553055322603520/image.png?ex=67f09f4e&is=67ef4dce&hm=d8c5ae746661b6cc4a92e03913896ed7d96ece3d691b9fe18c1edbcc202a7b02&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdeformis', aliases=['xdefor'])
async def xdeformis(ctx):
    embed = discord.Embed(title='Deformis')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553129268314307/image.png?ex=67f09f60&is=67ef4de0&hm=0ef4a2c59a73721718be59288a653178ed0f30e2ad6191f241f1176017a08ff1&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmenti', aliases=['xmen'])
async def xmenti(ctx):
    embed = discord.Embed(title='Menti')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553223665455164/image.png?ex=67f09f76&is=67ef4df6&hm=0bf91eb3435a15e553167a1e68c3d5a4abb2948d83a98ccd94c158f4bfe10a9b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbiskyva', aliases=['xbisk'])
async def xbiskyva(ctx):
    embed = discord.Embed(title='Biskyva')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553346445312131/image.png?ex=67f09f93&is=67ef4e13&hm=668414742971a61acc05dfd609c53d322bf2ba327d8f06832696633cb0d716d0&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


########################### Xtall BAB 15 ###########################################



@bot.command(name='xsupreme', aliases=['xsecb'])
async def xsupreme(ctx):
    embed = discord.Embed(title='Supreme Evil Crystal Beast')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553925514854610/image.png?ex=67f0a01d&is=67ef4e9d&hm=429cc58317969e149153790d459f47b9d1518ba302c3297cbdef0d154837c3b4&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xpiscruva', aliases=['xpiscru'])
async def xpiscruva(ctx):
    embed = discord.Embed(title='Piscruva')
    embed.add_field(name='Upgrade', value='nurethoth>guignol>guard golem>piscruva', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553823274762360/image.png?ex=67f0a005&is=67ef4e85&hm=6c565c1f709354c4e1e3fcdeb763b380e675ebb34a6fda33e0635c733371e763&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbakuzan', aliases=['xbaku'])
async def xbakuza(ctx):
    embed = discord.Embed(title='Bakuzan')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357554048068354208/image.png?ex=67f0a03b&is=67ef4ebb&hm=e258b0d8bc408666ff8dacbcc76769cb79d6104612ed792d108c0516f4b0b702&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

############################## Xtall Event Boss ###################################################################

################################ Xtall Hanami Event ##############################
@bot.command(name='xblackpeachninja', aliases=['xninja'])
async def xninja(ctx):
    embed = discord.Embed(title='Black Peach Ninja')
    embed.add_field(name='Upgrade', value='Mimesia>\nDreamy Scarlet  Sakura>\nBaavgai>\nBlack Peach  Ninja', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1362329734247088178/image.png?ex=6801ffef&is=6800ae6f&hm=2a2c3ae8ca2ecaf1dfb6535643ccea264fda8a7747877f6ef4003f87721c272a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xsquirinja', aliases=['xsquiri'])
async def xsquirinja(ctx):
    embed = discord.Embed(title='Squirinja')
    embed.add_field(name='Upgrade', value='Mimesia>\nDreamy Scarlet  Sakura>\nBaavgai>\nSquirinja', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1362334569201930280/image.png?ex=68020470&is=6800b2f0&hm=7664850b06979ef9ef932fe6bc13b1a4e57c0b4914d7e49b95d220e6138fbc62&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



################################ Mini Boss Xtall ######################################################################







@bot.command(name='xtortuga', aliases=['xtortu'])
async def xtortuga(ctx):
    embed = discord.Embed(title='Tortuga')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357567902722691152/image.png?ex=67f4a1a2&is=67f35022&hm=12ad3cabf79ca22a277557882860f693b2e2005ee7f2068841589ff9a563e78a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmiraclepotum', aliases=['xmiracle'])
async def xmiraclepotum(ctx):
    embed = discord.Embed(title='Miracle Potum')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568106394030311/image.png?ex=67f4a1d2&is=67f35052&hm=131225c16f82e552a6103686852dc379e76585aa2f35a1b0b18ab09ca4e75ac8&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdarkmushroom', aliases=['xdmushroom'])
async def xdarkmushroom(ctx):
    embed = discord.Embed(title='Dark Mushroom')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357567978945908858/image.png?ex=67f4a1b4&is=67f35034&hm=1464c88ee6b7b9e212e9435f47db4f4238cf1350a1904966f951cede288cf01d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsilverroar', aliases=['xsilver'])
async def xsilverorar(ctx):
    embed = discord.Embed(title='Silver Roar')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568199306248264/image.png?ex=67f4a1e9&is=67f35069&hm=bdcf3254917abfe305f1d165331dbe9421e523b9a982f6f24b2acbeb86f891d7&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmetalstinger', aliases=['xmetal'])
async def xmetal(ctx):
    embed = discord.Embed(title='Metal Stinger')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569899865575574/image.png?ex=67f4a37e&is=67f351fe&hm=da19289bc54f0a4a0c94c1e3b6fe75cb0bb1a776cab6354e5c0d6c6e81c76a26&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xkingpotum', aliases=['xking'])
async def xkingpotum(ctx):
    embed = discord.Embed(title='King Potum')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568325651140689/image.png?ex=67f4a207&is=67f35087&hm=3a1db820271f812f782269074fa698cc9d82637c435fb121e6f7bdcbc47d5e09&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgiantboar', aliases=['xgiant'])
async def xgiantboar(ctx):
    embed = discord.Embed(title='Giant Boar')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568642044399806/image.png?ex=67f4a252&is=67f350d2&hm=0fa522d7f43b3d9f2025de689d03a03b5a476f300384e2def4c0c7076c1bcce6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgoldenskeleton', aliases=['xgolden'])
async def xgoldenskeleton(ctx):
    embed = discord.Embed(title='Golden Skeleton')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568772256432339/image.png?ex=67f4a271&is=67f350f1&hm=002d581fdadb46df2d4ce9960b65f5961c84726477ce87fe3de987eb39285e16&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbigcoryn', aliases=['xbig'])
async def xbigcoryn(ctx):
    embed = discord.Embed(title='Big Coryn')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568866728935504/image.png?ex=67f4a288&is=67f35108&hm=3a311357d78c8146529fc04af3a34e5ec15dab3bcef8a9c09b030c434093da0f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='seltirio', aliases=['xselti'])
async def xseltirio(ctx):
    embed = discord.Embed(title='Seltirio')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357568973452873728/image.png?ex=67f4a2a1&is=67f35121&hm=b54a6dd854ace7a80c7586fea764fa804199036c2570c65aee37f68074907a57&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xstonemercenary', aliases=['xstone'])
async def xstonemerchenary(ctx):
    embed = discord.Embed(title='Stone Mercenary')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569118957473882/image.png?ex=67f4a2c4&is=67f35144&hm=a7501197b2139906c94ab913763bf32152b63bf43298deb9e63a16251d4b5ae5&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xarcoiris', aliases=['xarco'])
async def xarcoiris(ctx):
    embed = discord.Embed(title='Arcoiris')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569236825800787/image.png?ex=67f4a2e0&is=67f35160&hm=30ffe90d23334db2f26c92ab5ddb6d99f42573b5a51d7b0c2108c636c09d705a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmoonlightpotum', aliases=['xmoonlight'])
async def xmoonlightpotum(ctx):
    embed = discord.Embed(title='Moonlight Potum')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569499112407070/image.png?ex=67f4a31f&is=67f3519f&hm=b15f6f1d0ce6773028ce5a916318388ca256e518bed05c58d2832b4e7a429a75&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgigantknight', aliases=['xgigant'])
async def xgigantknight(ctx):
    embed = discord.Embed(title='Gigant Knight')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569608474689658/image.png?ex=67f4a339&is=67f351b9&hm=6a91a85de042effcfcc95c8a2d3fd584a6de20575671288d3e80c130f45d5b71&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcaspy', aliases=['xcasp'])
async def xcaspy(ctx):
    embed = discord.Embed(title='Caspy')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569697796849824/image.png?ex=67f4a34e&is=67f351ce&hm=e966f7657861de79af42500bc1094cde0c869a939ce7539fa4f51f39575efba0&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xviolaccoon', aliases=['xviola'])
async def xviolaccoon(ctx):
    embed = discord.Embed(title='Violaccoon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569798124474491/image.png?ex=67f4a366&is=67f351e6&hm=4a9f11a009c81fca73bd7488d7a74a3cbc92f2c2c3570aee5c00e35282d4a3c4&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xshininggentleman', aliases=['xshining'])
async def xshininggentleman(ctx):
    embed = discord.Embed(title='Shining Gentleman')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357569995118346365/image.png?ex=67f4a395&is=67f35215&hm=f094194bfb0ec9a180b77433f368039d052fe2667d8c2f8209ac1e124009f871&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdeathcolon', aliases=['xdeath'])
async def xdeathcolon(ctx):
    embed = discord.Embed(title='Death Colon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357570113070432317/image.png?ex=67f4a3b1&is=67f35231&hm=9df7f79d382b2357cdb53cf30868b3340da2515269e809b3bbf2cb5884e6f607&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgranny', aliases=['xgrany'])
async def xgranny(ctx):
    embed = discord.Embed(title='Granny')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357570297682989198/image.png?ex=67f4a3dd&is=67f3525d&hm=c15f16bd7640b8cdfe81d97b76dc107c53599025cf835b0ba39c1c8fb38bac89&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgrylle', aliases=['xGrylle'])
async def xgrylle(ctx):
    embed = discord.Embed(title='Grylle')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357570411151229019/image.png?ex=67f4a3f8&is=67f35278&hm=2df8bed24cd47973357ae4c2b8efea82cfbaebb8bf2a96bb18d093829fa6ef28&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xnightmarepotum', aliases=['xnightmare'])
async def xnightmarepotum(ctx):
    embed = discord.Embed(title='Nightmare Potum')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357573924854038669/image.png?ex=67f4a73e&is=67f355be&hm=f63d1f9478db0c2009eaa405d8e0ee7c91d7886bcb241c221110ea4c231da05d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdaddyfinpen', aliases=['xfinpen'])
async def xdaddyfinpen(ctx):
    embed = discord.Embed(title='Daddy Finpen')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574013425287330/image.png?ex=67f4a753&is=67f355d3&hm=157922dd351ceea61a51322e1c0f0a9526af0c780422c2600cb66e13371cc481&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xlapin', aliases=['xLapin'])
async def xlapin(ctx):
    embed = discord.Embed(title='Lapin the Necromancer')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574093246824612/image.png?ex=67f4a766&is=67f355e6&hm=dd9375fed7c084dd8c596d43b05e087d3cff62271436c5ce734756d7b5c465ef&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcorrodedknight', aliases=['xcorroded'])
async def xcorrodedknight(ctx):
    embed = discord.Embed(title='Corroded Knight Captian')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574196624097322/image.png?ex=67f4a77e&is=67f355fe&hm=843a0719f540023976fcb8ae55bfcaa8be7dbb52d1464c815ba35f340036ad31&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsalamander', aliases=['xsalam'])
async def xsalamander(ctx):
    embed = discord.Embed(title='Salamander')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574273492848660/image.png?ex=67f4a791&is=67f35611&hm=7ea37719a6ca1ec79abc3fcddfc2864f9e52f714fa0df42e1288a92b87fab84d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='xevilmagicsword', aliases=['xems'])
async def xevilcrystalsword(ctx):
    embed = discord.Embed(title='Evil Crystal Sword')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574351859482736/image.png?ex=67f4a7a3&is=67f35623&hm=41e90527fcb9af56dc54777aa7fd8b49418751448a9f535041886ce946d48adf&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbuildergolem', aliases=['xbuilder'])
async def xbuildergolem(ctx):
    embed = discord.Embed(title='Builder Golem')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574524652228638/image.png?ex=67f4a7cd&is=67f3564d&hm=cdc9568d7c9149aa3008910dcf9a2c8611111c5ea303feb85474fed3d265d15b&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xdusk', aliases=['xDusk'])
async def xdusk(ctx):
    embed = discord.Embed(title='Dusk Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574641312333864/image.png?ex=67f4a7e9&is=67f35669&hm=364073a64448a3115cc9dc09d8dd56e789ce92f7239b57b7376097843cad42c1&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xodelon', aliases=['xOdelon'])
async def xodelon(ctx):
    embed = discord.Embed(title='Odelon Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574754512666674/image.png?ex=67f4a803&is=67f35683&hm=714bd887d96200d9f7161503115e2007f2cfffbf5a511eae93ab99c05cc41b03&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsuperdeathmushroom', aliases=['xsdm'])
async def xsuperdeathmushroom(ctx):
    embed = discord.Embed(title='Super Death Mushroom')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574882757709956/image.png?ex=67f4a822&is=67f356a2&hm=f920cb0b856c33193ebec1ba121c22ea9024fffffcf737c1c4047fe686636467&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcommandergolem', aliases=['xcg'])
async def xcommandergolem(ctx):
    embed = discord.Embed(title='Commander Golem')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357574965314064516/image.png?ex=67f4a836&is=67f356b6&hm=a7bec43de72e164ae1e6569126e121ca7934232ca13c06c2b63c88f6f14c964a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xlyark', aliases=['xLyark'])
async def xlyark(ctx):
    embed = discord.Embed(title='Lyark Master Specialist')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575053721731223/image.png?ex=67f4a84b&is=67f356cb&hm=d8b3967f4a4541c55b16d92604aaaaf2695f06f3581ea71a20108aad8ffb1ff1&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xamoeba', aliases=['xAmoeba'])
async def xamoeba(ctx):
    embed = discord.Embed(title='Amoeba Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575155542528210/image.png?ex=67f4a863&is=67f356e3&hm=7ab3066edbfc487b8f013b769c706ee041f67178688ff82754a0cbbd3dcf4876&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xvolotur', aliases=['xVolotur'])
async def xvolotur(ctx):
    embed = discord.Embed(title='Volontur')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575244193202256/image.png?ex=67f4a878&is=67f356f8&hm=3cf64f280558937c7333024407114b58f2e458c48688458c882186a8b52ade1a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwanderingwheel', aliases=['xww'])
async def xwanderingwheel(ctx):
    embed = discord.Embed(title='Wandering Wheel')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575333775282337/image.png?ex=67f4a88e&is=67f3570e&hm=1438e4c98384c46a50dbb310434c3b7310ac012865f957662b4fc16b82441a11&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xseraph', aliases=['xSeraph'])
async def xseraph(ctx):
    embed = discord.Embed(title='Seraph Machina')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575405607059506/image.png?ex=67f4a89f&is=67f3571f&hm=6a87478c9e729a037298ad89bef7fd97c849394fd8be1058f75e9eaa90721311&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsolopy', aliases=['xSolopy'])
async def xsolopy(ctx):
    embed = discord.Embed(title='Solopy')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575547433123927/image.png?ex=67f4a8c1&is=67f35741&hm=41614a4a679fc26f0f9ad6b0617f93db8c869c59543ffa6c3598357936ecce54&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xfanadon', aliases=['xFanadon'])
async def xfanadon(ctx):
    embed = discord.Embed(title='Fanadon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575605876428954/image.png?ex=67f4a8ce&is=67f3574e&hm=af37de9a75b94cff53bf2e51b97a10f3399b0079ca4a01e2e2756fd5efbbca2d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xaltoblepas', aliases=['xalto'])
async def xaltoblepas(ctx):
    embed = discord.Embed(title='Altoblepas')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575691217928323/image.png?ex=67f4a8e3&is=67f35763&hm=3071c3ffc4401ec41d29dbbc84662e1bf14343b3e6c5b09d16251d723096e3b7&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbubblebogey', aliases=['xbubble'])
async def xbubblebogey(ctx):
    embed = discord.Embed(title='Bubble Bogey')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575759895466075/image.png?ex=67f4a8f3&is=67f35773&hm=a29f802db75a67492a564541523e21c9e3af9685156ad78490276f53e3e16baf&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

    
@bot.command(name='xmithurnalynx', aliases=['xmithurna'])
async def xmithurna(ctx):
    embed = discord.Embed(title='Mithurna Lynx')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575856482160740/image.png?ex=67f4a90a&is=67f3578a&hm=2f59c48e3c2c1430a668339e4e6b23f523f4a6f4b82c3b98fafb92ff330adaf8&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcarbuncle', aliases=['xcarbu'])
async def xcarbuncle(ctx):
    embed = discord.Embed(title='Carbuncle')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575922311630908/image.png?ex=67f4a91a&is=67f3579a&hm=283ec94cd27da83e80b05f588ef57fcb16d349a329f95542f81538ee3c0b6333&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgoldenia', aliases=['xGoldenia'])
async def xgoldenia(ctx):
    embed = discord.Embed(title='Goldenia')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357575999671238786/image.png?ex=67f4a92c&is=67f357ac&hm=f8277d1323a99471036024f1e11852a97f627e17058cd9551d9d7311c0432fae&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xthuggolem', aliases=['xthug'])
async def xthuggolem(ctx):
    embed = discord.Embed(title='Thug Golem')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576057737449543/image.png?ex=67f4a93a&is=67f357ba&hm=adf909355634154bcbb1a11f74cf3d2e9c5b07a0fe7d9ffde7608b221f83943d&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgrimuckus', aliases=['xgrim'])
async def xgrimuckus(ctx):
    embed = discord.Embed(title='Grimuckus')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576134522306640/image.png?ex=67f4a94d&is=67f357cd&hm=1928e621f9214925fee800b7f77557f8254e4ce3d31cd8b564192e7d1bca5229&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xfrenzyviola', aliases=['xfrenzy'])
async def xfrenzyviola(ctx):
    embed = discord.Embed(title='Frenzy Viola')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576339850530996/image.png?ex=67f4a97d&is=67f357fd&hm=12fd2cd26bb26a08e4fa70c96ca9d92ff71710b0a1769c007cc669d26e6e2809&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xarmasite', aliases=['xArmasite'])
async def xarmasite(ctx):
    embed = discord.Embed(title='Armasite')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576429067440198/image.png?ex=67f4a993&is=67f35813&hm=056210dd04b118e5e270b2e89d54fb555410caf5106d97b14021e045f3d2227a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xmegaalpoca', aliases=['xmega'])
async def xmegaalpoca(ctx):
    embed = discord.Embed(title='Mega Alpoca')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576489461219428/image.png?ex=67f4a9a1&is=67f35821&hm=12fa3a789ad08fd650d77e4b42bbc540bdccfaf4f26d30669791bf27902bf796&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xblood', aliases=['xbsc'])
async def xblood(ctx):
    embed = discord.Embed(title='Blood Smeared Crystal')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576721116823782/image.png?ex=67f4a9d8&is=67f35858&hm=d45d84532ebfd757200c247fa4f0fa73839f381c8a6a78eed767c8325e1b792f&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xcanemofish', aliases=['xcanemo'])
async def xcanemofish(ctx):
    embed = discord.Embed(title='Canemofish')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576814448607242/image.png?ex=67f4a9ef&is=67f3586f&hm=5186fb4322cd8bdb09865b4f1beea931e2585668d6af591babf37b28cee0be29&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


bot.command(name='xdemoniceye', aliases=['xdemonic'])
async def xdemoniceye(ctx):
    embed = discord.Embed(title='Demonic Eye')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576870706811010/image.png?ex=67f4a9fc&is=67f3587c&hm=b48b3896c01d30cfde769b8316c134f0004774f89c72227c002c96ca8f1e26e5&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtardigrademon', aliases=['xtardi'])
async def xtardigrademon(ctx):
    embed = discord.Embed(title='Tardigrademon')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357576955444203601/image.png?ex=67f4aa10&is=67f35890&hm=9d51e29f25602cd626240ff9efb31e9ff9b8d165c858d86b01cdb8f70c046e30&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xsandbannditsleader', aliases=['xsandbandit'])
async def xsandbanditsleader(ctx):
    embed = discord.Embed(title='Sand Bandits Leader')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577074222694440/image.png?ex=67f4aa2d&is=67f358ad&hm=673536bb1c2a9aced1ea3f862341b6ae510c87066905caaa6af9f1659ae1d650&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xageladanios', aliases=['xagel'])
async def xageladanios(ctx):
    embed = discord.Embed(title='Ageladanios')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577168430960660/image.png?ex=67f4aa43&is=67f358c3&hm=1e23536c03f1f964b8d7cc64a97461969c44d644cb9f050e63cfd365ae1563a3&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtappler', aliases=['xTappler'])
async def xtappler(ctx):
    embed = discord.Embed(title='Tappler')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577270700544060/image.png?ex=67f4aa5b&is=67f358db&hm=cfabc084700554f3586526feaebdf7c1115606389856cbb532f1d90f712bfaf9&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xespectro', aliases=['xespec'])
async def xespectro(ctx):
    embed = discord.Embed(title='Espectro')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577363478548560/image.png?ex=67f4aa72&is=67f358f2&hm=9c6307f28a08cedf677c252d882a17413c2bb224fc8ac26b95e162acbf10efce&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgrimreaper', aliases=['xreaper'])
async def xgrimreaper(ctx):
    embed = discord.Embed(title='Grim Reaper Screcrow')
    embed.set_image(url='')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xlordofnezim', aliases=['xnezim'])
async def xlordofnazim(ctx):
    embed = discord.Embed(title='Lord of Nezim')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577574330404884/image.png?ex=67f4aaa4&is=67f35924&hm=910faa9529ee3905fcf47f5b8d548de7dc5d2a5ffd8c57626720a82ba25ec0a6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xtrocostida', aliases=['xtroco'])
async def xtrocostida(ctx):
    embed = discord.Embed(title='Trocostida')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577658132860928/image.png?ex=67f4aab8&is=67f35938&hm=0bbeb3c410208ac8b6101df216ada6fc3c917cddf56242db982b9da7d8278d5c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xrhinosaur', aliases=['xrhino'])
async def xrhinosaur(ctx):
    embed = discord.Embed(title='Rhinosaur')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577717737848955/image.png?ex=67f4aac6&is=67f35946&hm=d6d106a8cda72759a96c11061b14cb7fc00baa9230b4ba1c14aff76b1cea5172&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xarbogazella', aliases=['xarbo'])
async def xarbogazella(ctx):
    embed = discord.Embed(title='Arbogazella')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577816237150352/image.png?ex=67f4aadd&is=67f3595d&hm=a4c71c7cabd50c0b5170bf7fa31be0ecd42e2a6caa5f923eadc3ae2565cb26ab&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbullamius', aliases=['xbull'])
async def xbullamius(ctx):
    embed = discord.Embed(title='Bullamius')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357577919714562129/image.png?ex=67f4aaf6&is=67f35976&hm=761ba79ecacf4d7aefa038ad6df734e7775d4620b4c03b531f78a9727789c7d1&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xgordo', aliases=['xGordo'])
async def xgordo(ctx):
    embed = discord.Embed(title='Gordo')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357578013679554671/image.png?ex=67f4ab0d&is=67f3598d&hm=5c25d0de1a16261c4c4659a3ee9ff2b2ca183854c1614bbbc16aff9e9539cb58&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xblazingur', aliases=['xblazing'])
async def xblazingur(ctx):
    embed = discord.Embed(title='Blazingur')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357578081921011972/image.png?ex=67f4ab1d&is=67f3599d&hm=c7670e5ef6e44b8e282c121719aacb1732b8c9691c9495fa7cd5de13507f9093&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xglaucius', aliases=['xglau'])
async def xglaucius(ctx):
    embed = discord.Embed(title='Glaucius')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357578710202716190/image.png?ex=67f4abb3&is=67f35a33&hm=0fe538f239fd8554ae2a411bd5f484116785f947de05bcf6ce7c4d38be823a6a&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xignitrus', aliases=['xignit'])
async def xignitrus(ctx):
    embed = discord.Embed(title='Ignitrus')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357578823419564183/image.png?ex=67f4abce&is=67f35a4e&hm=4b13dcd6809fc01874b8017532eb29f49d87bcc08b2fc5c54525040fd5a24972&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xrampion', aliases=['xRampion'])
async def xrampion(ctx):
    embed = discord.Embed(title='Rampion')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357578902976860291/image.png?ex=67f4abe1&is=67f35a61&hm=52cad6c20843008b37cbcefd548fe6ef5142e2b8091590c0c5a1f93cca4fc041&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xwolkissa', aliases=['xwolkis'])
async def xwolkissa(ctx):
    embed = discord.Embed(title='Wolkissa')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1357554153794179152/1357579013136318704/image.png?ex=67f4abfb&is=67f35a7b&hm=d4f9be38e7d0b4b7950f1b39bcb95ee53fce317160b9a0c939f289aa4f6392f9&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


###################### Mini Boss Stat Tabel ###########################


@bot.command(name='miniboss1', aliases=['Miniboss1'])
async def miniboss1(ctx):
    embed = discord.Embed(title='Tabel Detail Mini Boss')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1358672146003394680/1358672234004222033/mini_boss1.png?ex=67f4b19f&is=67f3601f&hm=8e3eb5c218f430aa9b36de884d3d19ec917e8666e12fed91e32ccbbfadc6276c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='miniboss2', aliases=['Miniboss2'])
async def miniboss2(ctx):
    embed = discord.Embed(title='Tabel Detail Mini Boss')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1358672146003394680/1358672226336899173/mini_boss2.png?ex=67f4b19d&is=67f3601d&hm=df18506c8c58383a90e6e1ca767e4dcd026d97ac0ab9b36f6473834c659ec8b6&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='miniboss3', aliases=['Miniboss3'])
async def miniboss3(ctx):
    embed = discord.Embed(title='Tabel Detail Mini Boss')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1358672146003394680/1358672212223070268/mini_boss_3.png?ex=67f4b19a&is=67f3601a&hm=8afae5f71364e1dc3d2855328dae121ef29c2e18edae2cd912e9c7d233071697&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='buffland', aliases=['Buffland'])
async def buffland(ctx):
    embed = discord.Embed(title='Tabel Detai Buff Land')
    embed.set_image(url='https://cdn.discordapp.com/attachments/1358672146003394680/1358672202114793583/food_level_toram.png?ex=67f4b197&is=67f36017&hm=a56c43a35591ec567642b9b9374e8d913887fc92e241767f99221708b83031a0&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)




####################################### DROP LIST #############################################




##################################### DROP 14 ################################################






@bot.command(name='droppiscruva', aliases=['dropPiscruva', 'droppiscru', 'droppisc', 'dropPiscru', 'dropPisc'])
async def droppiscruva(ctx):
    class droppiscruvaView(View):
        @discord.ui.button(label='Puscruva Bow STAT', style=discord.ButtonStyle.primary)
        async def PuscruvaBowSTAT(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Puscruva Bow')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362426610627903568/image.png?ex=68025a28&is=680108a8&hm=b61159b8329f04871898bf4ffb773fff5a9708a3c3b92497390bc24c8435667b&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Puscruva Bow APP', style=discord.ButtonStyle.primary)
        async def PuscruvaBowAPP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Puscruva Bow')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362426610988355734/image.png?ex=68025a28&is=680108a8&hm=192e654e2aa8738484fde4bb61540b196cdc9fb2b786ae7e72cddcc1d4f86106&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Puscruva Gun STAT', style=discord.ButtonStyle.danger)
        async def PuscruvaGunSTAT(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Puscruva Gun')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362426609709351094/image.png?ex=68025a28&is=680108a8&hm=d0a787a3dc4ee1f7b86b8b7a83d5c526fd43cbcc6bbe47e11d944fd9bc378535&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Puscruva Gun APP', style=discord.ButtonStyle.danger)
        async def PuscruvaGunAPP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Puscruva Gun')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362426610057220207/image.png?ex=68025a28&is=680108a8&hm=f03d14928894dc9be7af611a15a01b055b7232ae8a8959dde828dd010af1bd07&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Xtall', style=discord.ButtonStyle.danger)
        async def xtallpiscruva(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Piscruva')
            embed.add_field(name='Upgrade', value='Nurethoth>\nGuignol>\nGuard Golem>\nPiscruva', inline=True)
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362426611282215054/image.png?ex=68025a28&is=680108a8&hm=5429b71dca3809e34a63a37e614e04c44502a1b0b45ee5455a03bbc35f8152eb&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

    view = droppiscruvaView()
    await ctx.send("Pilih salah satu kategori untuk Drop boss Piscruva:", view=view)




###################################### DROP 15 ###############################################

@bot.command(name='dropsupreme', aliases=['dropsecb', 'dropsupreme evil crystal beast', 'dropsupremeevilcrystalbeast'])
async def dropsupreme(ctx):
    class dropsupremeView(View):
        @discord.ui.button(label='Evil Crystal Beast Spear STAT', style=discord.ButtonStyle.primary)
        async def Evil_Crystal_Beast_Spear_STAT(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Evil Crystal Beast Spear')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362411519215669499/image.png?ex=68024c1a&is=6800fa9a&hm=d3a5dd4ae11f51fbc4656b845bb501b6c881a90fcab1cc6bbc4756b7d30df206&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Evil Crystal Beast Spear APP', style=discord.ButtonStyle.primary)
        async def Evil_Crystal_Beast_Spear_APP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Evil Crystal Beast Spear')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362411518896898089/image.png?ex=68024c1a&is=6800fa9a&hm=38320343f78e89a222ac86ba9a6ac03444825c12a92f27d11c3967b386f21d36&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Evil Crystal Beast Wings STAT', style=discord.ButtonStyle.danger)
        async def Evil_Crystal_Beast_Wings_STAT(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Evil Crystal Beast Wings')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362411519866048572/image.png?ex=68024c1a&is=6800fa9a&hm=ba2adf99c90e53a55f7cf180a64f74d11ad9f3f7143c493a70442cd792bd76f7&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Evil Crystal Beast Wings APP', style=discord.ButtonStyle.danger)
        async def Evil_Crystal_Beast_Wings_APP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Evil Crystal Beast Wings')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362411520230949014/image.png?ex=68024c1a&is=6800fa9a&hm=e0e4cf13ea444e869afa9cae459582c86900e75fcf2b877005d297f1df7d3358&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Xtall', style=discord.ButtonStyle.danger)
        async def xtallsupreme(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Supreme Evil Crystal Beast')
            embed.add_field(name='Upgrade', value='Pillar Golem>\nUltimate Machina>\nVlam the Flame Dragon>\nSupreme Evil Crystal Beast', inline=True)
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362411519513596167/image.png?ex=68024c1a&is=6800fa9a&hm=71f8632ce685bc41ecf92491c4b42ea7805e1b8badf514b1e802740abf18be9c&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

    view = dropsupremeView()
    await ctx.send("Pilih salah satu kategori untuk Drop boss Supreme Evil Crystal Beast:", view=view)

###

@bot.command(name='dropbakuzan', aliases=['dropbaku'])
async def dropbakuza(ctx):
    class dropbakuzaView(View):
        @discord.ui.button(label='Brigand Coat Stat', style=discord.ButtonStyle.primary)
        async def Brigand_Coat_Stat(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Brigand Coat')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362381719315026020/image.png?ex=68023059&is=6800ded9&hm=ba8c8d0c3e1eaeb533ca5f8f5b7f4876ef4dcd5dd86db37ff35a582a778f1aa7&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Brigand Coat APP', style=discord.ButtonStyle.primary)
        async def Brigand_Coat_APP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Brigand Coat APP')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362383286592339998/image.png?ex=680231cf&is=6800e04f&hm=23c5fde099a7421334e741797218e444c325f5532b871e3299f30deb6db8633e&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Mini Cannon', style=discord.ButtonStyle.danger)
        async def Mini_Cannon(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Mini Cannon')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362382016955420792/image.png?ex=680230a0&is=6800df20&hm=fdc74926f34b59738b5f135c5fd14628b56a7d0917bbe38afe97a7572ce9176f&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Mini Cannon APP', style=discord.ButtonStyle.danger)
        async def Mini_Cannon_APP(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Mini Cannon APP')
            embed.set_image(url='https://cdn.discordapp.com/attachments/1362381233727869001/1362383582894755921/image.png?ex=68023216&is=6800e096&hm=ca233f34b3f4d6a3e03a998359657097b1fe13c04ac9a938c1748729105514b6&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

        @discord.ui.button(label='Xtall Bakuzan', style=discord.ButtonStyle.danger)
        async def xtall_bakuzan(self, interaction: discord.Interaction, button: Button):
            embed = discord.Embed(title='Bakuzan')
            embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
            embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357554048068354208/image.png?ex=67f0a03b&is=67ef4ebb&hm=e258b0d8bc408666ff8dacbcc76769cb79d6104612ed792d108c0516f4b0b702&')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
            await interaction.response.send_message(embed=embed, ephemeral=True)

    view = dropbakuzaView()
    await ctx.send("Pilih salah satu kategori untuk Drop boss Bakuza:", view=view)














########################################################################
######################################################################
#######################################################################
#########################  Buff Land Home Code #########################
############################################################################
##########################################################################

@bot.command(name='str', aliases=['streght'])
async def str(ctx):
    embed = discord.Embed(title='Code Alamat STR')
    embed.add_field(name='Name', value='Okaka Rice Ball', inline=False)
    embed.add_field(name='STR', value='4016699\n1110033\n2020303\n2017890\n1010055', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='hp', aliases=['Hp'])
async def hp(ctx):
    embed = discord.Embed(title='Code Alamat hp')
    embed.add_field(name='Name', value='Golden Stir Fry', inline=False)
    embed.add_field(name='HP', value='1011945 Punya si Ghill\n1250015\n4262222\n3040005\n1180755\n1010455', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='mp', aliases=['maxmp'])
async def mp(ctx):
    embed = discord.Embed(title='Code Alamat MP ')
    embed.add_field(name='Name', value='Anake Fried Rice', inline=False)
    embed.add_field(name='MP', value='1032222\\n2010079\n1091111\n1240000\n1027777', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='ampr', aliases=['AMPR'])
async def ampr(ctx):
    embed = discord.Embed(title='Code Alamat AMPR ')
    embed.add_field(name='Name', value='Yakisoba', inline=False)
    embed.add_field(name='AMPR', value='4040404\n4261111\n5010031\n1016969\n4233333', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='crit', aliases=['Crit'])
async def crit(ctx):
    embed = discord.Embed(title='Code Alamat Critical Rate')
    embed.add_field(name='Name', value='Takoyaki', inline=False)
    embed.add_field(name='Critical Rate', value='7010086\n1181140\n1100000\n5119105\n2022020', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='acc', aliases=['Acc'])
async def acc(ctx):
    embed = discord.Embed(title='Code Alamat Accuracy ')
    embed.add_field(name='Name', value='Shoyu Ramen', inline=False)
    embed.add_field(name='ACC', value='2010308\n4261111\n1181220', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='atk', aliases=['Atk'])
async def atk(ctx):
    embed = discord.Embed(title='Code Alamat ATK')
    embed.add_field(name='Name', value='Pizza Diavola', inline=False)
    embed.add_field(name='ATK', value='7170717\n1119876', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='watk', aliases=['Watk'])
async def watk(ctx):
    embed = discord.Embed(title='Code Alamat Weapon Attack ')
    embed.add_field(name='Name', value='Pizza Margherita', inline=False)
    embed.add_field(name='W.Atk', value='3160777\n1067777\n6010024\n1011122', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='vit', aliases=['Vit'])
async def vit(ctx):
    embed = discord.Embed(title='Code Alamat VIT ')
    embed.add_field(name='Name', value='Tuna Mayo Rice Ball', inline=False)
    embed.add_field(name='VIT', value='4032850\n5130123', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='agi', aliases=['Agi'])
async def agi(ctx):
    embed = discord.Embed(title='Code Alamat AGI ')
    embed.add_field(name='Name', value='Mentaiko Rice Ball', inline=False)
    embed.add_field(name='AGI', value='7162029\n1110033\n1220777\n4262222\n2020037', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='dex', aliases=['Dex'])
async def dex(ctx):
    embed = discord.Embed(title='Code Alamat Dex')
    embed.add_field(name='Name', value='Salmon Rice Ball', inline=False)
    embed.add_field(name='DEX', value='2020222\n1010261\n1160000\n1112220\n1107777', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='int', aliases=['Int'])
async def int(ctx):
    embed = discord.Embed(title='Code Alamat INT')
    embed.add_field(name='Name', value='Umeboshi Rice Ball', inline=False)
    embed.add_field(name='INT', value='6010701\n6061294\n5190001\n101049\n1032222', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='maggro', aliases=['minaggrp'])
async def maggro(ctx):
    embed = discord.Embed(title='Code Alamat -Aggro')
    embed.add_field(name='Name', value='White Stew', inline=False)
    embed.add_field(name='-Aggro', value='1010147\n3190038\n1011174\n2020808\n3010018', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='aggro', aliases=['Aggro'])
async def aggro(ctx):
    embed = discord.Embed(title='Code Alamat Aggro')
    embed.add_field(name='Name', value='Beef Stew', inline=False)
    embed.add_field(name='Aggro', value='1010207\n1140008\n1011340\n2020606\n1130832', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='dark', aliases=['Dark'])
async def hp(ctx):
    embed = discord.Embed(title='Code Alamat DTE Dark')
    embed.add_field(name='Name', value='Squid Ink Pasta', inline=False)
    embed.add_field(name='DTE Dark', value='6116116\n5010092\n1190020', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='light', aliases=['Light'])
async def light(ctx):
    embed = discord.Embed(title='Code Alamat DTE Light')
    embed.add_field(name='Name', value='Carbonara', inline=False)
    embed.add_field(name='DTE Light', value='1240000', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='wind', aliases=['Wind'])
async def wind(ctx):
    embed = discord.Embed(title='Code Alamat DTE Wind')
    embed.add_field(name='Name', value='Naporitan', inline=False)
    embed.add_field(name='DTE Wind', value='3030303\n1180020', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='water', aliases=['Water'])
async def water(ctx):
    embed = discord.Embed(title='Code Alamat DTE Water')
    embed.add_field(name='Name', value='Vongole', inline=False)
    embed.add_field(name='Water', value='1110111\n7150030\n7011001', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='earth', aliases=['Earth'])
async def earth(ctx):
    embed = discord.Embed(title='Code Alamat DTE Earth')
    embed.add_field(name='Name', value='Genovese', inline=False)
    embed.add_field(name='Dte Earth', value='2020202\n4233333\n710066', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='pres', aliases=['Pres'])
async def pres(ctx):
    embed = discord.Embed(title='Code Alamat Physical Resistance')
    embed.add_field(name='Name', value='Chocolate Cake', inline=False)
    embed.add_field(name='Physical Resistance', value='1100000\n7010014\n4010051\n2200117\n6010701', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='mres', aliases=['Mres'])
async def mres(ctx):
    embed = discord.Embed(title='Code Alamat Magical Resistance')
    embed.add_field(name='Name', value='Cheese Cake', inline=False)
    embed.add_field(name='Magical Resistance', value='6190007\n2020505\n6234567\n7010016\n1111575', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='frac', aliases=['Frac'])
async def frac(ctx):
    embed = discord.Embed(title='Code Alamat Fractional Barrier ')
    embed.add_field(name='Name', value='Pancake', inline=False)
    embed.add_field(name='Fractional Barrier', value='53010043\n4010024\n6150029\n1010013', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)

@bot.command(name='neutral', aliases=['Neutral'])
async def neutral(ctx):
    embed = discord.Embed(title='Code Alamat DTE Neutral')
    embed.add_field(name='Name', value='Peperoncio', inline=False)
    embed.add_field(name='DTE Neutral', value='3210102   DTE Neutral Lv 10\n3099876   DTE Neutral Lv 7\n1011902   DTE Neutral Lv 7\n6061294   DTE Neutral Lv 7\n1019696   DTE Neutral Lv 6\n1032727   DTE Neutral Lv 5', inline=True)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)



############################################################################
#########################################################################
########################### BUFF CONSUME #################################
###########################################################################


@bot.command(name='consumhp', aliases=['hpbuff'])
async def show_hp_buffs(ctx):
    embed = discord.Embed(title='🍖 Max HP Buffs Menu', color=discord.Color.green())
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/1318582370760265768/1321414339944648734/12.png?ex=67f6eb41&is=67f599c1&hm=c4156615e70851b8da9b8d0d4b9719781bff7f06053c5be6c51d526db69c93d5&format=webp&quality=lossless&width=1560&height=1106&')

    food_buffs = [
    ("Dragon Steak (30 min)", "🟢 Max HP +1500\n🟢 ASPD +250"),
    ("Deep-Fried Bean Curd (10 min)", "🟢 Max HP % +1\n🟢 Accuracy +15"),
    ("Iced Chicken Vita (30 min)", "🟢 Max HP +1000\n🔴 Aggro% -30"),
    ("Dondurma (10 min)", "🔴 Max HP % -15\n🟢 Aggro% +30"),
    ("Salt-Grilled Saury (30 min)", "🟢 Max HP +1000\n🟢 Natural HP Recovery % +100"),
    ("Eggplant Tempura (30 min)", "🟢 Max HP +1000\n🟢 Experience % +10"),
    ("Kiton's Meat (4 min)", "🟢 Max HP +5000"),
    ("Tough Lamb Meat (30 min)", "🟢 Max HP +750\n🟢 STR +5"),
    ("Bone-In Short Rib (20 min)", "🟢 Max HP % +10\n🟢 ATK +25"),
    ("Sugar Cookie (30 min)", "🟢 Max HP +1500\n🟢 Max MP +200"),
    ("Chilled Lamb (30 min)", "🟢 INT +3\n🟢 Max HP +1250"),
    ("Charred Salamander Meat (20 min)", "🟢 Max HP +4000\n🟢 ATK up VIT % +20\n🟢 MATK up VIT % +20")
    ]


    for name, effect in food_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consuhpmrecovery', aliases=['hprecov', 'hpregen'])
async def show_hp_recovery_buffs(ctx):
    embed = discord.Embed(title='🧪 HP Recovery Buffs Menu', description='Recover HP per use 🧪🧪🧪', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/1318582370760265768/1321436793710841856/14.png?ex=67f7002a&is=67f5aeaa&hm=dc6c79baa10facfa483221c359e58534cfb12b22c1287b51fd00a53c2df03bd1&format=webp&quality=lossless&width=889&height=629&')

    recovery_buffs = [
        ("Wedding Wine", "🟢 Recover HP +3000\n🟢 Recover MP +100"),
        ("Swordsbear Treasured Sake", "🟢 Recover HP +12000"),
        ("Pomie Castella", "🟢 Recover HP % +15"),
        ("Winter Caffe Latte", "🟢 Recover HP +3000\n🟢 Recover MP +70"),
        ("Winter Caffe Mocha", "🟢 Recover HP +2000\n🟢 Recover MP +80"),
        ("Winter Macchiato", "🟢 Recover HP +7500\n🟢 Recover MP +25")
    ]

    for name, effect in recovery_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consummp', aliases=['mpbuff'])
async def show_mp_buffs(ctx):
    embed = discord.Embed(title='🔷 Max MP Buffs Menu', color=discord.Color.purple())
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/1318582370760265768/1321430856039923753/Illustration.png?ex=67f6faa3&is=67f5a923&hm=0be9e397a59ee292e968d1f2273008fc31ef3cd01dc2021b61022d799712bdf4&format=webp&quality=lossless&width=1560&height=1106&')

    mp_buffs = [
        ("Mystery Potion (B) (10 min)", "🔴 Max MP -100\n🟢 Motion Speed % +2"),
        ("Aggro Tonic (30 min)", "🟢 Max MP +100\n🟢 Aggro % +20"),
        ("Mashed Sweet Potato (30 min)", "🟢 Max MP +200\n🟢 NMPR % +100"),
        ("Little Bird Tiramisu (15 min)", "🟢 Max MP +200\n🟢 ASPD +100"),
        ("Magiadd VI (30 min)", "🟢 Max MP +600"),
        ("Potum Beans (10 min)", "🟢 Max MP +500\n🟢 AMPR +5"),
        ("Sauteed Lonogo Shrimp (30 min)", "🟢 Max MP +300\n🟢 CSPD +250")
    ]

    for name, effect in mp_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consummprecovery', aliases=['mprecov', 'mpregen'])
async def show_mp_recovery_buffs(ctx):
    embed = discord.Embed(title='🧃 MP Recovery Buffs', description='Recover MP per use and over time 🧃🧃🧃', color=discord.Color.teal())
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/1318582370760265768/1321442585541214298/13.png?ex=67f7058f&is=67f5b40f&hm=2239859659a792d5ac7a87fb2d7a2ad90039b8640599124d995d313a2725a256&format=webp&quality=lossless&width=1560&height=1106&')

    # Recover MP per use
    embed.add_field(name="🔹 Recover MP per use", value="\u200b", inline=False)

    per_use_buffs = [
        ("Forbidden Nut", "🟢 Recover MP 300\n🔴 Max HP % -99\n💬 Must be used at full health to avoid death."),
        ("Coryn's Present", "🟢 Recover MP 300"),
        ("Pom Biscuits", "🟢 Recover MP 150"),
        ("Sakura Liqueur", "🟢 Recover MP 100"),
        ("Whipped Cream", "🟢 Recover MP 100"),
        ("Mellow Mushroom", "🟢 Recover MP 75")
    ]

    for name, effect in per_use_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    # Recover MP over time
    embed.add_field(name="\n🔹 Recover MP over time", value="\u200b", inline=False)

    over_time_buffs = [
        ("Champagne (30 min)", "🟢 Recover MP 100 every 10 seconds"),
        ("Snow Wine (15 min)", "🟢 Recover MP %10 every 10 seconds\n💬 Capped to recover a maximum of 100 MP per tick."),
        ("Mana Catalyst (30 min)", "🟢 AMPR +8"),
        ("Premium Coffee (3 min)", "🟢 Recover MP 50 every 5 seconds")
    ]

    for name, effect in over_time_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumail', aliases=['ailbuff'])
async def show_ailment_buffs(ctx):
    embed = discord.Embed(
        title='🛡️ Ailment Prevention Buffs',
        description='Buffs to help resist or reduce ailments.',
        color=discord.Color.green()
    )
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/1318582370760265768/1323362483188138044/32.png?ex=67f6c15a&is=67f56fda&hm=dea21903fb26cf76345134766c77fbf85ef0e6bfe23e14a97e3796508b4225d3&format=webp&quality=lossless&width=889&height=629&')

    ailment_buffs = [
        ("Mystery Potion (G) (10 min) ", "🟢 Ailment Resistance % -10\n🟢 Max MP +100"),
        ("Romanian Eggplant Dip (30 min)", "🟢 Ailment Resistance % +5")
    ]

    for name, effect in ailment_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumdef', aliases=['defbuff'])
async def show_defense_buffs(ctx):
    embed = discord.Embed(
        title='🛡️ Defense Buffs',
        description='Buffs to increase physical, magical, or guard defenses.',
        color=discord.Color.dark_gold()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326967128821207124/10.png?ex=67f6af71&is=67f55df1&hm=145aad464bf009bf6228d68be3ca2f7c886afd43a9a215856d57dd976775a8a0&format=webp&quality=lossless&width=1560&height=1106&'
    )

    # Optional visual separator
    embed.add_field(name="🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱🧱", value="\u200b", inline=False)

    defense_buffs = [
        ("Mystery Potion Y (10 min)", "🟢 ATK % +1\n🟢 Physical Defense % +10"),
        ("Ginkgo Nut Rice (15 min)", "🟢 Physical Resistance % +25\n🟢 Magic Resistance % +25"),
        ("Goodbye Hat (30 min)", "🟢 Guard Power % +10\n🟢 Guard Recharge % +10\n🟢 VIT +10")
    ]

    for name, effect in defense_buffs:
        embed.add_field(name=name, value=effect, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consummdef', aliases=['mdefbuff'])
async def show_magic_defense_buffs(ctx):
    embed = discord.Embed(
        title='🔮 Magic Defense Buffs',
        description='Buffs to improve magic defense or resistance.',
        color=discord.Color.purple()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326968555802984548/11.png?ex=67f6b0c5&is=67f55f45&hm=59a24ef609b3d1fe89c341036ae2f70a4a065ec536a47c9404aa47b6817f2416&format=webp&quality=lossless&width=1560&height=1106&'
    )

    embed.add_field(name="✨", value="\u200b", inline=False)

    magic_defense_buffs = [
        ("Mystery Potion (P) (10 min)", "🟢 MATK % +1\n🟢 Magic Defense % +10"),
        ("Elf Berry Pot (30 min)", "🟢 Magic Resistance % +12"),
        ("Shiny Powder (30 min)", "🟢 Magic Defense +100\n🟢 Aggro % +10"),
        ("Warm Fur Sheet (30 min)", "🟢 Magic Defense % +15\n🟢 Reduce Damage Floor % +15"),
    ]

    for name, value in magic_defense_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumresis', aliases=['elementres', 'eleressbuff'])
async def show_element_resistance_buffs(ctx):
    embed = discord.Embed(
        title='🌪️ Resistance to Elements Buffs',
        description='Buffs to increase elemental resistance from Takoyaki & Christmas series.',
        color=discord.Color.orange()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326972537653166191/9.png?ex=67f6b47a&is=67f562fa&hm=4c257ea839191bb446b6e279b0aed5aea152018cd877322a7201a23873a52d6d&format=webp&quality=lossless&width=889&height=629&'
    )

    # Takoyaki Series
    embed.add_field(name="🍢 Takoyaki Series", value="\u200b", inline=False)
    takoyaki_buffs = [
        ("Roasted Eggplant (15 min)", "🟢 Critical Rate +10\n🟢 Resistance to Neutral % +20"),
        ("Big Takoyaki (Salt) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Light % +30"),
        ("Big Takoyaki (Ponzu) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Dark % +30"),
        ("Big Takoyaki (Soy Sauce) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Earth % +30"),
        ("Big Takoyaki (Dashi) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Water % +30"),
        ("Big Takoyaki (Sauce) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Fire % +30"),
        ("Big Takoyaki (Scallion) (20 min)", "🟢 Critical Rate +15\n🟢 Resistance to Wind % +30"),
    ]

    for name, value in takoyaki_buffs:
        embed.add_field(name=name, value=value, inline=False)

    # Christmas Series
    embed.add_field(name="🎄 Christmas Series", value="\u200b", inline=False)
    christmas_buffs = [
        ("Iced Chocolate (15 min)", "🟢 Max MP +100\n🟢 Resistance to Light % +25"),
        ("Iced Coffee (15 min)", "🟢 Max MP +100\n🟢 Resistance to Dark % +25"),
        ("Fruit Cake (30 min)", "🟢 Max MP +100\n🟢 Resistance to Earth % +50"),
        ("Ice Cream Cake (30 min)", "🟢 Max MP +100\n🟢 Resistance to Water % +50"),
        ("Chocolate Cake (30 min)", "🟢 Max MP +100\n🟢 Resistance to Fire % +50"),
        ("Cheesecake (30 min)", "🟢 Max MP +100\n🟢 Resistance to Wind % +50"),
    ]

    for name, value in christmas_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumatk', aliases=['atkkbuffs', 'atkbuff'])
async def show_atk_buffs(ctx):
    embed = discord.Embed(
        title='⚔️ ATK Buffs',
        description='Buff makanan & item yang meningkatkan kekuatan serangan (ATK).',
        color=discord.Color.red()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326973929461649578/3.png?ex=67f6b5c6&is=67f56446&hm=74876ffc461f9fae5ab1a7d1755bd652caa5908bde4d5ef34e874eec606776d5&format=webp&quality=lossless&width=889&height=629&'
    )

    atk_buffs = [
        ("Penetrating Oil (30 min)", "🟢 Physical Pierce % +10\n🟢 ATK % +3"),
        ("Morning Star Gummy (10 min)", "🟢 Physical Pierce % +5\n🟢 Critical Rate % +40"),
        ("Energy Pill (30 min)", "🟢 ATK % +5\n🟢 ATK +50"),
        ("Lantern Cake (30 sec)", "🟢 ATK % +10\n🔻 Motion Speed % -10"),
        ("Blade Oil (30 min)", "🟢 Unsheathed ATK % +5\n🟢 Unsheathed ATK +100"),
        ("Matsutake Soup (15 min)", "🟢 Weapon ATK % +10\n🟢 Attack MP Recovery +10"),
        ("Pumpkie Parfait (15 min)", "🟢 ATK % +6"),
        ("Scorching Grass (2 min)", "🟢 Weapon Attack +9\n🟢 Damage to Earth % +2"),
    ]

    for name, value in atk_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consummatk', aliases=['matkbuffs', 'matkbuff'])
async def show_matk_buffs(ctx):
    embed = discord.Embed(
        title='🔮 MATK Buffs',
        description='Buff makanan & item yang meningkatkan Magic Attack (MATK).',
        color=discord.Color.purple()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326975446507585580/7.png?ex=67f6b730&is=67f565b0&hm=96fc984ccd9e306a5e10a259297385045469b92ff944a9c99198738c93448abc&format=webp&quality=lossless&width=1560&height=1106&'
    )

    matk_buffs = [
        ("Mommy Roll Cake (10 min)", "🟢 Magic Pierce % +5\n🟢 Critical Rate % +40"),
        ("Pom's Rice Cake Soup (30 min)", "🟢 Magic Pierce % +5\n🟢 Weapon ATK % +5"),
        ("Dried Walnut (3 min)", "🟢 MATK % +1\n🟢 DEX % +1"),
        ("Bitter Gelatin (5 min)", "🔻 MATK % -4\n🟢 CSPD +800"),
        ("Sparkly Candy (30 sec)", "🟢 MATK % +10\n🔻 Motion Speed % -10"),
        ("Barrier Analyzer Lithograph (30 min)", "🟢 Magic Pierce % +10\n🟢 MATK % +3"),
        ("Sorcerer's Nostrum (30 min)", "🟢 MATK % +5\n🟢 MATK +50"),
    ]

    for name, value in matk_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumele', aliases=['elebuff'])
async def show_damage_to_elements_buffs(ctx):
    embed = discord.Embed(
        title='✨ Damage to Elements Buffs',
        description='Buff makanan & item yang meningkatkan damage terhadap elemen tertentu.',
        color=discord.Color.orange()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326980706810990634/1.png?ex=67f6bc16&is=67f56a96&hm=d7ede370e553592df9703e21664158576fbba7f551f3cb051ae0071489cc2e83&format=webp&quality=lossless&width=889&height=629&'
    )

    damage_buffs = [
        ("Glow Ray Soup (30 min)", "🟢 Damage to Fire % +2\n🟢 Damage to Water % +2\n🟢 Damage to Wind % +2\n🟢 Damage to Earth % +2\n🟢 Damage to Light % +2\n🟢 Damage to Dark % +2"),
        ("Pumpkin Soup (10 min)", "🟢 Damage to Neutral % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Pumpkin Candy (10 min)", "🟢 Damage to Light % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Zombie Cake (10 min)", "🟢 Damage to Dark % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Barmbrack (10 min)", "🟢 Damage to Earth % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Ginger Cake (10 min)", "🟢 Damage to Water % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Pumpkin Cookie (10 min)", "🟢 Damage to Fire % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
        ("Jack Pudding (10 min)", "🟢 Damage to Wind % +5\n🟢 ASPD +100\n🟢 CSPD +100"),
    ]

    for name, value in damage_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumaspd', aliases=['aspdbuffs', 'aspdbuff'])
async def show_aspd_buffs(ctx):
    embed = discord.Embed(
        title='💨 Attack Speed Buffs',
        description='Buff makanan & item yang meningkatkan kecepatan serangan (ASPD) dan kecepatan gerak.',
        color=discord.Color.orange()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326981857526550629/8.png?ex=67f6bd28&is=67f56ba8&hm=f9967ae9f4ba9b8c8c44a284bafdb899d92ec7ff45a3b8963027b9b574972737&format=webp&quality=lossless&width=889&height=629&'
    )

    aspd_buffs = [
        ("Tera Speed Potion (30 min)", "🟢 ASPD +1000"),
        ("Solid Fuel (5 sec)", "🟢 Motion Speed % +10"),
        ("Pear Tart (15 min)", "🟢 ASPD +500\n🟢 AMPR +3"),
        ("Zombie Meat (30 min)", "🔻 ASPD -1000\n🟢 Max HP +10000"),
        ("Coryn's Present (30 sec)", "🟢 ASPD +10000\n🔻 Recoil Damage % +100"),
        ("Chirashi Sushi (30 min)", "🟢 ASPD +500\n🟢 ASPD % +25\n🟢 Defense +75"),
        ("Duck Meat (3 min)", "🟢 Motion Speed +5%")
    ]

    for name, value in aspd_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumcspd', aliases=['castbuffs', 'cspdbuff'])
async def show_cast_speed_buffs(ctx):
    embed = discord.Embed(
        title='✨ Cast Speed Buffs (CSPD)',
        description='Buff makanan & item yang meningkatkan kecepatan casting skill (CSPD).',
        color=discord.Color.purple()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326984767274618970/Untitled46_20250110004227.png?ex=67f6bfde&is=67f56e5e&hm=2a8ec201f1e5f889e170419bf444e57e4ac6715eaa1791561020b7e786d7dfac&format=webp&quality=lossless&width=1560&height=1106&'
    )

    cspd_buffs = [
        ("Spell Headphones (30 min)", "🟢 CSPD +700"),
        ("Grape Jelly (15 min)", "🟢 CSPD +300\n🟢 Max MP +300"),
        ("Inari Sushi (30 min)", "🟢 CSPD +500\n🟢 CSPD % +25\n🟢 MDEF +75"),
    ]

    for name, value in cspd_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumacc', aliases=['accuracybuffs', 'accbuff'])
async def show_accuracy_buffs(ctx):
    embed = discord.Embed(
        title='🎯 Accuracy Buffs',
        description='Buff makanan & item yang meningkatkan akurasi atau critical.',
        color=discord.Color.gold()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326983825502507048/34_1.png?ex=67f6befe&is=67f56d7e&hm=2219e493c36125cd5d67bb1e4fd2bec21ee6adb8084c3641da7a338fc766bccf&format=webp&quality=lossless&width=619&height=629&'
    )

    accuracy_buffs = [
        ("Sauteed Butter Snails (30 min)", "🟢 Accuracy +30\n🟢 Critical Rate +5"),
        ("War Dead Bracelet (30 min)", "🟢 Accuracy +60"),
        ("Black Gelatin (3 min)", "🟢 Critical Rate +10\n🔻 Critical Damage % -10"),
        ("Battie Scone (15 min)", "🟢 Accuracy +5%\n🟢 Long Range Damage +1%"),
    ]

    for name, value in accuracy_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)

@bot.command(name='consumflee', aliases=['fleebuff'])
async def show_flee_buffs(ctx):
    embed = discord.Embed(
        title='🏃‍♂️ Flee Buffs',
        description='Buff makanan & item yang meningkatkan Dodge (Flee).',
        color=discord.Color.orange()
    )
    embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/1318582370760265768/1326985241008803850/2.png?ex=67f6c04f&is=67f56ecf&hm=b82356e4689b76fd67e40851fcfd802f5645ff569973a161ec8f4dc42eed8731&format=webp&quality=lossless&width=889&height=629&'
    )

    flee_buffs = [
        ("Golden Pom Liquor (10 min)", "🟢 Accuracy +50\n🟢 Dodge +50"),
        ("Wood Praline (15 min)", "🟢 Dodge % +10\n🟢 MATK % +1"),
    ]

    for name, value in flee_buffs:
        embed.add_field(name=name, value=value, inline=False)

    await ctx.send(embed=embed)



#####################################################################
########################### Leveling ############################
###################################################################



@bot.command(name='56', aliases=['57', '58', '59', '60', '61', '62'])
async def level56_to_62(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 56–62)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Boss Roga (Normal)** - Lv. 62 - Saham Underground Cave - Deepest Part\n"
        "**Forestia (Hard)** - Lv. 59 - Land Of Chaos\n"
        "**Flare Volg (Hard)** - Lv. 60 - Fiery Volcano: Boss Map\n"
        "\u200b"  # invisible character for spacing
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Big Coryn** - Lv. 60 - Douce Hamlet\n"
        "**Stone Mercenary** - Lv. 60 - Zoktzda Ruins : Abnormal Space\n"
        "**Seltirios** - Lv. 60 - Aulada Ancient Tower"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='63', aliases=['64', '65', '66', '67', '68'])
async def level_63_to_68(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 62–68)', color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Forestia (Nightmare)** - Lv. 69 - Land Of Chaos\n"
        "**Masked Warrior (Normal)** - Lv. 67 - Land Under Cultivation: Hill\n"
        "**Boss Roga (Normal)** - Lv. 62 - Saham Underground Cave - Deepest Part\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Outer World Wolf** - Lv. 70 - Gate to Another World: Area 1\n"
        "**Outer World Wolf** - Lv. 70 - Gate to Another World: Area 2\n"
        "**Big Coryn** - Lv. 60 - Douce Hamlet"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='69', aliases=['70', '71', '72', '73', '74', '75'])
async def level_69_to_75(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 69–75)', color=discord.Color.teal())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Grass Dragon Yelb (Normal)** - Lv. 73 - Albatif Village\n"
        "**Forestia (Nightmare)** - Lv. 69 - Land Of Chaos\n"
        "**Boss Roga (Hard)** - Lv. 72 - Saham Underground Cave - Deepest Part\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Outer World Wolf** - Lv. 70 - Gate to Another World: Area 1 and 2\n"
        "**Arcoiris** - Lv. 70 - Yorl Highlands\n"
        "**Big Mask** - Lv. 70 - Haotas Ravine\n"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='76', aliases=['77', '78', '79', '80', '81', '82'])
async def level_76_to_82(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 76–82)', color=discord.Color.gold())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Jade Raptor (Normal)** - Lv. 79 - Gravel Terrace\n"
        "**Boss Roga (Nightmare)** - Lv. 82 - Saham Underground Cave - Deepest Part\n"
        "**Masked Warrior (Hard)** - Lv. 77 - Land Under Cultivation: Hill\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Violacoon** - Lv. 80 - Darkanon Plain\n"
        "**Shining Gentleman** - Lv. 82 - Lost Town: Square\n"
        "**Outer World Wolf** - Lv. 70 - Gate to Another World: Area 1\n"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='83', aliases=['84', '85', '86', '87', '88', '89', '90', '91', '92', '93'])
async def level_83_to_89(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 83–89)', color=discord.Color.dark_teal())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Jade Raptor (Hard)** - Lv. 89 - Gravel Terrace\n"
        "**Masked Warrior (Nightmare)** - Lv. 87 - Land Under Cultivation: Hill\n"
        "**Pillar Golem (Nightmare)** - Lv. 90 - Lost Town: Magic Barrier\n"
        "**Jade Raptor (Normal)** - Lv. 79 - Gravel Terrace\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Shining Gentleman** - Lv. 82 - Lost Town: Square\n"
        "**Violacoon** - Lv. 80 - Darkanon Plain\n"
        "**Death Colon** - Lv. 84 - Vyshed the Tainted Land: Area 2"
    ), inline=False)

    await ctx.send(embed=embed)

@bot.command(name='94', aliases=['95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106'])
async def level94_to_105(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 94–105)', color=discord.Color.dark_teal())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Jade Raptor (Nightmare)** - Lv. 99 - Gravel Terrace\n"
        "**Boss Roga (Ultimate)** - Lv. 102 - Saham Underground Cave - Deepest Part\n"
        "**Nurethoth (Nightmare)** - Lv. 96 - Gate to Another World: Front\n"
        "**Grass Dragon Yelb (Nightmare)** - Lv. 93 - Albatif Village\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Don Yeti** - Lv. 103 - Polde Ice Valley\n"
        "**Grylle** - Lv. 90 - Wanderer's Plain\n"
        "**Granny** - Lv. 88 - Abyss of No Return: Area 3"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='107', aliases=['108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120'])
async def level107_to_120(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 107–120)', color=discord.Color.dark_gold())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Grass Dragon Yelb (Ultimate)** - Lv. 113 - Albatif Village\n"
        "**Nurethoth (Ultimate)** - Lv. 116 - Gate to Another World: Front\n"
        "**Masked Warrior (Ultimate)** - Lv. 107 - Land Under Cultivation: Hill\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Don Yeti** - Lv. 103 - Polde Ice Valley"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='121', aliases=['122', '123', '124', '125', '126', '127', '128', '129', '130', '131', '132'])
async def level121_to_132(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 121–131)', color=discord.Color.red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Jade Raptor (Ultimate)** - Lv. 119 - Gravel Terrace\n"
        "**Scrader (Ultimate)** - Lv. 125 - Magic Waste Site: Deepest Part\n"
        "**Memecoleous (Nightmare)** - Lv. 120 - Dark Castle: Area 2\n"
        "**Black Knight of Delusion (Ultimate)** - Lv. 128 - Abyss of No Return: Deepest Area\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Lapin The Necromancer** - Lv. 124 - Trace of Dark River\n"
        "**Nightmare Potum** - Lv. 120 - Garden of Beginning"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='133', aliases=['134', '135', '136', '137', '138', '139', '140', '141', '142', '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153'])
async def level133_to_153(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 133–153)', color=discord.Color.dark_red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Cerberus (Ultimate)** - Lv. 137 - Spring of Rebirth: Top\n"
        "**Memecoleous (Ultimate)** - Lv. 140 - Dark Castle: Area 2\n"
        "**Imitator (Ultimate)** - Lv. 146 - Plastida: Deepest Part\n"
        "**Imitacia (Ultimate)** - Lv. 149 - Dark Castle: Grand Hall\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Super Death Mushroom** - Lv. 150 - Monster's Forest: Animal Trail\n"
        "**Odelon Machina** - Lv. 146 - Large Demi Machina Factory: Area 2\n"
        "**Dusk Machina** - Lv. 142 - Small Demi Machina Factory: Area 2"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='154', aliases=['155', '156', '157', '158', '159', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', '173', '174'])
async def level154_to_174(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 154–174)', color=discord.Color.teal())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Mozto Machina (Ultimate)** - Lv. 164 - Large Demi Machina Factory: Deepest Part\n"
        "**Venena Coenubia (Nightmare)** - Lv. 170 - Ultimea Palace: Throne\n"
        "**Tyrant Machina (Ultimate)** - Lv. 161 - Small Demi Machina Factory Core\n"
        "**Tapir (Ultimate)** - Lv. 160 - Blazing Graben: Surface\n"
        "**York (Ultimate)** - Lv. 158 - Huge Crysta Factory: Storage\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Amoeba Machina** - Lv. 158 - Ultimea Sewer: Southeast\n"
        "**Volotur** - Lv. 160 - Suburb of Droma Square: Area 3\n"
        "**Seraph Machina** - Lv. 167 - Buried Tower: Inside"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='175', aliases=['176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '188', '189', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199'])
async def level175_to_199(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 175–199)', color=discord.Color.dark_gold())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Bosses
    embed.add_field(name='**Bosses:**', value=(
        "**Venena Coenubia (Ultimate)** - Lv. 190 - Ultimea Palace: Throne\n"
        "**Ultimate Machina (Ultimate)** - Lv. 179 - Droma Square\n"
        "**Maton Sword (Ultimate)** - Lv. 183 - Buried Tower: Entrance\n"
        "**Gwaimol (Ultimate)** - Lv. 176 - Cuervo Jail: Roof\n"
        "**Ornlarf (Ultimate)** - Lv. 182 - Ultimea Palace: Corridor\n"
        "\u200b"
    ), inline=False)

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Altoblepas** - Lv. 174 - Rokoko Plains\n"
        "**Bubble Bogey** - Lv. 177 - Barbaros Corridor\n"
        "**Mithurna Lynx** - Lv. 177 - Ruins of Mt. Mithurna: Stylobate"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='200', aliases=['201', '202', '203', '204'])
async def level200_to_204(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 198–203)', color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Grimuckus** - Lv. 195 - Wazeero Street\n"
        "**Frenzy Viola** - Lv. 198 - Morthell Swell: Area 3"
    ), inline=False)

    # Boss Monsters
    embed.add_field(name='**Boss Monsters:**', value=(
        "**Venena Metacoenubia** - Lv. 205 (Hard) - Neo Plastida\n"
        "**Kuzto** - Lv. 198 (Nightmare) - Labilans Sector: Square\n"
        "**Seele Zauga** - Lv. 200 (Ultimate) - Shrine of the Goddess of Species\n"
        "**Finstern the Dark Dragon** - Lv. 206 (Ultimate) - Dark Dragon Shrine: Near the Top"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='205', aliases=['206', '207', '208'])
async def level205_to_209(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 203–206)', color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Frenzy Viola** - Lv. 198 - Morthell Swell: Area 3"
    ), inline=False)

    # Boss Monsters
    embed.add_field(name='**Boss Monsters:**', value=(
        "**Venena Metacoenubia** - Lv. 205 (Hard) - Neo Plastida\n"
        "**Seele Zauga** - Lv. 200 (Ultimate) - Shrine of the Goddess of Species\n"
        "**Finstern the Dark Dragon** - Lv. 206 (Ultimate) - Dark Dragon Shrine: Near the Top"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='209', aliases=['210', '211'])
async def level209_to_211(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 209–211)', color=discord.Color.dark_purple())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    # Mini Bosses
    embed.add_field(name='**Mini Bosses:**', value=(
        "**Demonic Eye** - Lv. 212 - Dea Ruinea\n"
        "**Canemofish** - Lv. 210 - Recetacula Sector: Area 1"
    ), inline=False)

    # Boss Monsters
    embed.add_field(name='**Boss Monsters:**', value=(
        "**Venena Metacoenubia** - Lv. 205 (Hard) - Neo Plastida\n"
        "**Finstern the Dark Dragon** - Lv. 206 (Ultimate) - Dark Dragon Shrine: Near the Top"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='212', aliases=['213', '214', '215', '216'])
async def level212_to_216(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 212–216)', color=discord.Color.dark_red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Bosses:**', value=(
        "**Demonic Eye** - Lv. 212 - Dea Ruinea\n"
        "**Canemofish** - Lv. 210 - Recetacula Sector: Area 1\n"
        "**Tardigrademon** - Lv. 213 - Old Lufenas Mansion Ruins"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Arachnidemon** - Lv. 216 (Nightmare) - Arche Valley: Depths\n"
        "**Kuzto** - Lv. 218 (Ultimate) - Labilans Sector: Square"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='217', aliases=['218', '219', '220', '221', '222'])
async def level215_to_222(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 215–222)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Bosses:**', value=(
        "**Ageladanios** - Lv. 218 - Ducia Coast: Area 1\n"
        "**Tappler** - Lv. 218 - Ruins of Urban Elban\n"
        "**Espectro** - Lv. 221 - Arche Valley: Area 1"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Arachnidemon** - Lv. 216 (Nightmare) - Arche Valley: Depths\n"
        "**Kuzto** - Lv. 218 (Ultimate) - Labilans Sector: Square\n"
        "**Gravicep** - Lv. 224 (Ultimate) - Recetacula Sector: Depot Rooftop"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='223', aliases=['224', '225'])
async def level223_to_225(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 223–225)', color=discord.Color.green())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Ageladanios** - Lv. 218 - Ducia Coast: Area 1\n"
        "**Tappler** - Lv. 218 - Ruins of Urban Elban\n"
        "**Espectro** - Lv. 221 - Arche Valley: Area 1\n"
        "**Lord of Nezim** - Lv. 227 - Nezim Wetlands"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Gemma** - Lv. 228 (Hard) - Fugitive Lake Swamp: Depths\n"
        "**Kuzto** - Lv. 218 (Ultimate) - Labilans Sector: Square\n"
        "**Gravicep** - Lv. 224 (Ultimate) - Recetacula Sector: Depot Rooftop"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='226', aliases=['227', '228', '229'])
async def level226_to_229(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 226–229)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Espectro** - Lv. 221 - Arche Valley: Area 1\n"
        "**Lord of Nezim** - Lv. 227 - Nezim Wetlands\n"
        "**Rhinosaur** - Lv. 233 - Fugitive Lake Swamp: Area 3"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Gemma** - Lv. 228 (Hard) - Fugitive Lake Swamp: Depths\n"
        "**Gravicep** - Lv. 224 (Ultimate) - Recetacula Sector: Depot Rooftop"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='230', aliases=['231', '232', '233', '234'])
async def level230_to_235(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 230–235)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Lord of Nezim** - Lv. 227 - Nezim Wetlands\n"
        "**Rhinosaur** - Lv. 233 - Fugitive Lake Swamp: Area 3"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Gemma** - Lv. 228 (Nightmare) - Fugitive Lake Swamp: Depths\n"
        "**Arachnidemon** - Lv. 236 (Ultimate) - Arche Valley: Depths"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='235', aliases=['236', '237', '238', '239'])
async def level235_to_240(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 235–240)', color=discord.Color.dark_green())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Rhinosaur** - Lv. 233 - Fugitive Lake Swamp: Area 3\n"
        "**Bullamius** - Lv. 239 - Storage Yard: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Arachnidemon** - Lv. 236 (Ultimate) - Arche Valley: Depths\n"
        "**Venena Metacoenubia** - Lv. 235 (Ultimate) - Neo Plastida"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='240', aliases=['241', '242', '243', '244'])
async def level240_to_245(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 240–245)', color=discord.Color.purple())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Bullamius** - Lv. 239 - Storage Yard: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Black Shadow** - Lv. 239 (Ultimate) - Rokoko City Ruins\n"
        "**Hexter** - Lv. 242 (Ultimate) - Witch's Woods Depths\n"
        "**Arachnidemon** - Lv. 236 (Ultimate) - Arche Valley: Depths"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='245', aliases=['246', '247', '248', '249', '250'])
async def level245_to_250(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 245–250)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Blazingur** - Lv. 245 - Divido Valley: Area 3\n"
        "**Glaucius** - Lv. 248 - Arstida: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Guard Golem** - Lv. 252 (Nightmare) - Weredragon's Throat\n"
        "**Ferzen the Rock Dragon** - Lv. 251 (Ultimate) - Guardian Forest: Giant Tree"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='251', aliases=['252', '253', '254', '255'])
async def level251_to_255(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 251–255)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Ignitrus** - Lv. 251 - Vulcani Crater Base\n"
        "**Glaucius** - Lv. 248 - Arstida: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Guard Golem** - Lv. 252 (Nightmare) - Weredragon's Throat\n"
        "**Ferzen the Rock Dragon** - Lv. 251 (Ultimate) - Guardian Forest: Giant Tree"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='256', aliases=['257', '258', '259', '260'])
async def level256_to_260(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 256–260)', color=discord.Color.red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Rampion Milcaska** - Lv. 254 - Falls: Army Base\n"
        "**Wolkissa** - Lv. 257 - Weredragon's Throat\n"
        "**Galegon** - Lv. 260 - Boma Moja: Area 3"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**War Dragon Turba** - Lv. 257 (Ultimate) - Prime Ramus: Village\n"
        "**Trickster Dragon Mimyugon** - Lv. 258 (Nightmare) - Operation Zone: Cockpit Area"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='261', aliases=['262', '263', '264', '265'])
async def level261_to_265(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 261–265)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Wolkissa** - Lv. 257 - Weredragon's Throat\n"
        "**Galegon** - Lv. 260 - Boma Moja: Area 3\n"
        "**Brassozard** - Lv. 263 - Operation Zone: Climate Control Area"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**War Dragon Turba** - Lv. 257 (Ultimate) - Prime Ramus: Village\n"
        "**Trickster Dragon Mimyugon** - Lv. 258 (Nightmare) - Operation Zone: Cockpit Area\n"
        "**Vlam the Flame Dragon** - Lv. 260 (Ultimate) - Divido Spring\n"
        "**Velum** - Lv. 263 (Ultimate) - Arstida: Depth"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='266', aliases=['267', '268', '269', '270'])
async def level266_to_270(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 266–270)', color=discord.Color.red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Exdocus** - Lv. 266 - Stairway to Vital Point\n"
        "**Diark** - Lv. 270 - Tower of Clamor: Area 3\n"
        "**Trus** - Lv. 269 - Propulsion System Zone: Power Tank\n"
        "**Brassozard** - Lv. 263 - Operation Zone: Climate Control Area"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Gordel** - Lv. 269 (Ultimate) - Milcaska Falls: Weredragon's Mouth\n"
        "**Oculasignio** - Lv. 266 (Ultimate) - Mt. Vulcani: Summit\n"
        "**Brass Dragon Reguita** - Lv. 270 (Nightmare) - Boma Konda: Village Center\n"
        "**Red Ash Dragon Rudis** - Lv. 269 (Hard) - Espuma Dome: Entrance\n"
        "**Velum** - Lv. 263 (Ultimate) - Arstida: Depth"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='271', aliases=['272', '273', '274', '275'])
async def level271_to_275(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 271–275)', color=discord.Color.red())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Charugon** - Lv. 275 - Boma Konda: Underground Area\n"
        "**Orictoceras** - Lv. 272 - Kabla Jabali\n"
        "**Diark** - Lv. 270 - Tower of Clamor: Area 3\n"
        "**Trus** - Lv. 269 - Propulsion System Zone: Power Tank"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Burning Dragon Igneus** - Lv. 275 (Ultimate) - Boma Moja: Village Center\n"
        "**Guard Golem** - Lv. 272 (Ultimate) - Weredragon's Throat\n"
        "**Gordel** - Lv. 269 (Ultimate) - Milcaska Falls: Weredragon's Mouth\n"
        "**Brass Dragon Reguita** - Lv. 270 (Nightmare) - Boma Konda: Village Center\n"
        "**Red Ash Dragon Rudis** - Lv. 269 (Hard) - Espuma Dome: Entrance"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='276', aliases=['277', '278', '279', '280'])
async def level276_to_280(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 276–280)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Charugon** - Lv. 275 - Boma Konda: Underground Area\n"
        "**Orictoceras** - Lv. 272 - Kabla Jabali\n"
        "**Lilicarolla** - Lv. 278 - Frozen Falls: Area 1\n"
        "**Vodre** - Lv. 281 - Puerta Islands: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Trickster Dragon Mimyugon** - Lv. 278 (Ultimate) - Operation Zone: Cockpit Area\n"
        "**Filrocas** - Lv. 281 (Ultimate) - Royal Dragon Cocoon Chamber\n"
        "**Burning Dragon Igneus** - Lv. 275 (Ultimate) - Boma Moja: Village Center\n"
        "**Guard Golem** - Lv. 272 (Ultimate) - Weredragon's Throat"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='281', aliases=['282', '283', '284', '285'])
async def level281_to_285(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 281–285)', color=discord.Color.orange())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Charugon** - Lv. 275 - Boma Konda: Underground Area\n"
        "**Lilicarolla** - Lv. 278 - Frozen Falls: Area 1\n"
        "**Vodre** - Lv. 281 - Puerta Islands: Area 2\n"
        "**Fantica** - Lv. 284 - Espuma Dome: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Trickster Dragon Mimyugon** - Lv. 278 (Ultimate) - Operation Zone: Cockpit Area\n"
        "**Walican** - Lv. 287 (Ultimate) - Jabali Kubwa: Summit\n"
        "**Wicked Dragon Fazzino** - Lv. 284 (Ultimate) - Propulsion System Room\n"
        "**Filrocas** - Lv. 281 (Ultimate) - Royal Dragon Cocoon Chamber"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='286', aliases=['287', '288', '289', '290'])
async def level286_to_290(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 286–290)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Limacina** - Lv. 290 - Deep Sea: Zone 2\n"
        "**Vodre** - Lv. 281 - Puerta Islands: Area 2\n"
        "**Capo Profundo** - Lv. 287 - Abandoned District: Area 3\n"
        "**Fantica** - Lv. 284 - Espuma Dome: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Mulgoon** - Lv. 291 (Nightmare) - Menabra Plains\n"
        "**Brass Dragon Reguita** - Lv. 290 (Ultimate) - Boma Konda: Village Center\n"
        "**Walican** - Lv. 287 (Ultimate) - Jabali Kubwa: Summit\n"
        "**Wicked Dragon Fazzino** - Lv. 284 (Ultimate) - Propulsion System Room"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='291', aliases=['292', '293', '294', '295'])
async def level291_to_295(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 291–295)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Limacina** - Lv. 290 - Deep Sea: Zone 2\n"
        "**Capo Profundo** - Lv. 287 - Abandoned District: Area 3"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Mulgoon** - Lv. 291 (Nightmare) - Menabra Plains\n"
        "**Dominaredor** - Lv. 293 (Ultimate) - Frozen Falls: Depths\n"
        "**Brass Dragon Reguita** - Lv. 290 (Ultimate) - Boma Konda: Village Center\n"
        "**Walican** - Lv. 287 (Ultimate) - Jabali Kubwa: Summit"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='296', aliases=['297', '298', '299', '300'])
async def level296_to_300(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 296–300)', color=discord.Color.blue())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Meteora** - Lv. 302 - Menabra Plains\n"
        "**Limacina** - Lv. 290 - Deep Sea: Zone 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Mulgoon** - Lv. 291 (Nightmare) - Menabra Plains\n"
        "**Dominaredor** - Lv. 293 (Ultimate) - Frozen Falls: Depths\n"
        "**Brass Dragon Reguita** - Lv. 290 (Ultimate) - Boma Konda: Village Center\n"
        "**Red Ash Dragon Rudis** - Lv. 299 (Ultimate) - Espuma Dome: Entrance"
    ), inline=False)

    await ctx.send(embed=embed)


@bot.command(name='301', aliases=['302', '303', '304', '305'])
async def level301_to_305(ctx):
    embed = discord.Embed(title='Spot Leveling (Lv. 301–305)', color=discord.Color.green())
    embed.set_thumbnail(url='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhpYWlyYnQ5YWo0bzk1Y25idjUzcm1zNGc3a2YzOXAyczN4aTR5MSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/HuZx6u3PtNScexzvwK/giphy.gif')

    embed.add_field(name='**Mini Boss Monsters:**', value=(
        "**Meteora** - Lv. 302 - Menabra Plains\n"
        "**Wiltileaf** - Lv. 305 - Eumano Village Ruins: Area 2"
    ), inline=False)

    embed.add_field(name='**Boss Monsters:**', value=(
        "**Vatudo** - Lv. 305 (Ultimate) - Deep Sea: Deepest Zone\n"
        "**Don Profundo** - Lv. 302 (Ultimate) - Abandoned District: Ruins Summit\n"
        "**Red Ash Dragon Rudis** - Lv. 299 (Ultimate) - Espuma Dome: Entrance"
    ), inline=False)

    await ctx.send(embed=embed)



####################################################################
######################### Element Arrow ############################
#####################################################################



@bot.command(name='firearrow', aliases=['panahapi'])
async def firearrow(ctx):
    embed = discord.Embed(
        title='🔥 Fire Element Arrows',
        description='Berikut adalah daftar panah berelemen api beserta lokasi drop dan statistiknya.',
        color=discord.Color.red()
    )

    embed.add_field(
        name='Flame Arrow',
        value=(
            "**Drop:** Sunion *(Normal Monster Lv 73/76 - Dark Mirror)*\n"
            "**Base ATK:** 34\n"
            "**Base Stability:** 20%\n"
            "**MaxMP:** +100\n"
            "**Element:** 🔥 Fire\n"
            "━━━━━━━━━━━━━━━━━━━"
        ),
        inline=False
    )

    embed.add_field(
        name='Demon Empress Arrow',
        value=(
            "**Drop:** Venena Metacoenubia *(Raid Boss Lv 185-235 - Neo Plastida)*\n"
            "**Base ATK:** 120\n"
            "**Base Stability:** 10%\n"
            "**Accuracy:** +15\n"
            "**Aggro:** -15%\n"
            "**Element:** 🔥 Fire\n"
            "━━━━━━━━━━━━━━━━━━━"
        ),
        inline=False
    )

    embed.add_field(
        name='Blazing Tail Arrow',
        value=(
            "**Drop:** Tailgon *(Normal Monster Lv 213/216 - Tunnel of Trial)*\n"
            "**Base ATK:** 152\n"
            "**Base Stability:** 20%\n"
            "**Fire Resistance:** +10%\n"
            "**Reduce Damage (Bowling):** 20%\n"
            "**Element:** 🔥 Fire\n"
            "━━━━━━━━━━━━━━━━━━━"
        ),
        inline=False
    )

    embed.add_field(
        name='|Limited Event| Love Arrow',
        value=(
            "**Craft:** NPC Blacksmith (Valentine Event Recipe)\n"
            "**Base ATK:** 71\n"
            "**Base Stability:** 20%\n"
            "**Critical Rate:** +5\n"
            "**Element:** 🔥 Fire\n"
            "━━━━━━━━━━━━━━━━━━━"
        ),
        inline=False
    )

    embed.add_field(
        name='Dragon Guard Arrow',
        value=(
            "**Drop:** 7th Road of Megiston: 4th Battle\n"
            "**Base ATK:** 187\n"
            "**Base Stability:** 20%\n"
            "**Critical Rate:** +10\n"
            "**Attack MP Recovery:** +3\n"
            "**Earth Resistance:** -5%\n"
            "**Element:** 🔥 Fire\n"
            "**Note:** *BEST ARROW to deal more damage*\n"
            "━━━━━━━━━━━━━━━━━━━"
        ),
        inline=False
    )

    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='neutralarrow', aliases=['panahnetral'])
async def neutralarrow(ctx):
    embed = discord.Embed(
        title='Neutral Element Arrows',
        description='Daftar panah berelemen Neutral lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.light_grey()
    )

    embed.add_field(
        name='LIL EMPRESS ARROW',
        value=(
            "**Drop:** Venena Coenubia (Raid Boss Lv 140–190 – Ultimea Palace: Throne)\n"
            "**Base ATK:** 83\n"
            "**Stability:** 15%\n"
            "**Physical Pierce:** +10%\n"
            "**DEF:** -30%\n"
            "**ASPD:** +10%\n"
            "**Aggro:** -10%\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='QUARTZ ARROW',
        value=(
            "**Drop:** Rollitida (Lv 191/193 – Fugitive Lake Swamp: Area 2/3)\n"
            "**Base ATK:** 115\n"
            "**Stability:** 20%\n"
            "**Critical Rate:** +10\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='DRILL BOLT',
        value=(
            "**Drop:** Mine Digger (Lv 113 – Ultimea Sewer: South)\n"
            "**Base ATK:** 120\n"
            "**Stability:** 10%\n"
            "**Physical Pierce:** +10%\n"
            "**Critical Damage:** +2\n"
            "**Aggro:** +20%\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='SPIRAL SHELL ARROW',
        value=(
            "**Drop:** Spirulida (Lv 243–245 – Deep Sea Zone 1/2/3)\n"
            "**Base ATK:** 163\n"
            "**Stability:** 20%\n"
            "**Physical Pierce:** +10%\n"
            "**Anticipate:** +10%\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] DREAMY ARROW',
        value=(
            "**Drop:** Dreamy Scarlet Sakura (Nightmare Lv 220 – Hanami Event Boss – Lush Falls: Upstream)\n"
            "**Base ATK:** 136\n"
            "**Stability:** 20%\n"
            "**Natural HP Regen:** +10%\n"
            "**Aggro:** -20%\n"
            "**Stronger vs Neutral:** +5%\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] DRIVER BOLT',
        value=(
            "**Drop:** Inspector Golem (Lv 164 – Winter Event – Joulu House: Depot)\n"
            "**Base ATK:** 200\n"
            "**Stability:** 20%\n"
            "**Accuracy:** -25%\n"
            "**Attack MP Recovery:** +3\n"
            "**Neutral Resistance:** +15%\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] ANNIV FESTIVE ARROW IV',
        value=(
            "**Drop:** Anniv Equipment Box VII\n"
            "**Base ATK:** 200\n"
            "**Stability:** 20%\n"
            "**Attack Speed:** +400\n"
            "**Fractional Barrier:** +10%\n"
            "**Aggro:** -16%\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


@bot.command(name='waterarrow', aliases=['panahair'])
async def waterarrow(ctx):
    embed = discord.Embed(
        title='Water Element Arrows',
        description='Daftar panah berelemen Water lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.blue()
    )

    embed.add_field(
        name='SERREIN ARROW',
        value=(
            "**Drop:** Floragonet (Lv 159/160 – Fractum Sector: Area 1/2)\n"
            "**Base ATK:** 84\n"
            "**Stability:** 20%\n"
            "**Effect:** Tumble Unavailable\n"
            "**Absolute Accuracy:** +1%\n"
            "**Element:** Water\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='DRY WATER ARROW',
        value=(
            "**Drop:** Coofer (Lv 255/256/257 – Umidus Valley: Area 1/2/3)\n"
            "**Base ATK:** 206\n"
            "**MaxHP:** +15%\n"
            "**Aggro:** +30%\n"
            "**Element:** Water\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] OCEAN ARROW',
        value=(
            "**Craft:** NPC Blacksmith (Summer Event Recipe)\n"
            "**Base ATK:** 110\n"
            "**Stability:** 20%\n"
            "**MaxMP:** +200\n"
            "**Attack MP Recovery:** +1\n"
            "**Wind Resistance:** -3%\n"
            "**Element:** Water\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] DRAGON PALACE ARROW',
        value=(
            "**Drop:** Sea Ghost Wooden Box - Falburrow\n"
            "(Summer Event Boss – Saltau's Beach [Night])\n"
            "**Base ATK:** 200\n"
            "**MaxHP:** +25%\n"
            "**Critical Rate:** +25%\n"
            "**Effect:** Stun Unavailable\n"
            "**Special:** -25% damage to Neutral\n"
            "**Element:** Water\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


@bot.command(name='windarrow', aliases=['panahangin'])
async def windarrow(ctx):
    embed = discord.Embed(
        title='Wind Element Arrows',
        description='Daftar panah berelemen Wind lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.green()
    )

    embed.add_field(
        name='TEMPEST ARROW (Boss Drop)',
        value=(
            "**Drop:** Forestia (Lv 39/49/59/69/89 – Land Of Chaos)\n"
            "**Base ATK:** 15\n"
            "**Stability:** 20%\n"
            "**Accuracy:** +10%\n"
            "**Critical Damage:** +1%\n"
            "**Element:** Wind\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='TEMPEST ARROW (Craft)',
        value=(
            "**Craft:** NPC Blacksmith\n"
            "**Base ATK:** 15\n"
            "**Stability:** 20%\n"
            "**Critical Damage:** +1%\n"
            "**Element:** Wind\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='APPLE ARROW',
        value=(
            "**Drop:** Coryn (Lv 154–156 – Dikkit Sector)\n"
            "**Base ATK:** 92\n"
            "**Stability:** 15%\n"
            "**Aggro:** -10%\n"
            "**Element:** Wind\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] QUEEN BEE ARROW',
        value=(
            "**Craft:** NPC Blacksmith (Valentine Event Recipe)\n"
            "**Base ATK:** 150\n"
            "**Stability:** 20%\n"
            "**Additional Melee:** +10\n"
            "**Water Resistance:** +5%\n"
            "**Effect:** Tumble Unavailable\n"
            "**Element:** Wind\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] BAT FANG ARROW',
        value=(
            "**Drop:** Halloween Event – Rissus Valley\n"
            "**Base ATK:** 136\n"
            "**Stability:** 20%\n"
            "**Physical Pierce:** +10%\n"
            "**Critical Rate:** +10\n"
            "**Accuracy:** -20\n"
            "**Element:** Wind\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


@bot.command(name='eartharrow', aliases=['panahbumi'])
async def eartharrow(ctx):
    embed = discord.Embed(
        title='Earth Element Arrows',
        description='Daftar panah berelemen Earth lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.dark_gold()
    )

    embed.add_field(
        name='POINTED ORE ARROW',
        value=(
            "**Drop:** Cavern Rat (Lv 99 – Singolare Ruins: 1st Floor)\n"
            "**Base ATK:** 43\n"
            "**Stability:** 20%\n"
            "**DEF:** +50\n"
            "**Physical Resistance:** +3%\n"
            "**Accuracy:** -1%\n"
            "**Element:** Earth\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='GUARDIAN FOREST ARROW',
        value=(
            "**Drop:** Arbogazella (Miniboss Lv 236 – Guardian Forest: Lost Woods)\n"
            "**Base ATK:** 167\n"
            "**Stability:** 20%\n"
            "**Accuracy:** +50%\n"
            "**Aggro:** -25%\n"
            "**Stronger Against Fire:** -10%\n"
            "**Stronger Against Light:** -20%\n"
            "**Element:** Earth\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='EUMANO ARROW',
        value=(
            "**Drop:** Deformis (Lv 264 – Eumano Village Ruins: Central)\n"
            "**Base ATK:** 226\n"
            "**Stability:** 25%\n"
            "**Long Range Damage:** +1%\n"
            "**Motion Speed:** +3%\n"
            "**Critical Rate:** +5\n"
            "**Element:** Earth\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] CACAO ARROW',
        value=(
            "**Craft:** NPC Blacksmith (Valentine Event Recipe)\n"
            "**Base ATK:** 50\n"
            "**Stability:** 20%\n"
            "**Critical Rate:** +3\n"
            "**Aggro:** -6%\n"
            "**Element:** Earth\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


@bot.command(name='lightarrow', aliases=['panahcahaya'])
async def lightarrow(ctx):
    embed = discord.Embed(
        title='Light Element Arrows',
        description='Daftar panah berelemen Light lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.gold()
    )

    embed.add_field(
        name='FLASH VOLT',
        value=(
            "**Reward:** Sub Quest [Juan - *Unforgettable Taste*, El Scaro]\n"
            "**Base ATK:** 3\n"
            "**Stability:** 15%\n"
            "**Accuracy:** +10\n"
            "**Critical Rate:** +10\n"
            "**Stronger Against Light:** -50%\n"
            "**Element:** Light\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='JOYFUL ARROW',
        value=(
            "**Drop:** Crestollar (Lv 253/256 – Latum Wetlands)\n"
            "**Base ATK:** 100\n"
            "**Stability:** 20%\n"
            "**Max MP:** +100\n"
            "**Element:** Light\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] CANDY ARROW',
        value=(
            "**Craft:** NPC Blacksmith (White Day Event Recipe)\n"
            "**Base ATK:** 56\n"
            "**Stability:** 20%\n"
            "**Magic DEF:** +10%\n"
            "**Magic Resistance:** +10%\n"
            "**Element:** Light\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='HOLY TREE ARROW',
        value=(
            "**Drop:** Santaby (Winter Event, Lv 159 – Tomte Pavilion)\n"
            "**Base ATK:** 100\n"
            "**Stability:** 20%\n"
            "**Dark Resistance:** +10%\n"
            "**Attack MP Recovery:** +1\n"
            "**Element:** Light\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='STARHAMMER ARROW',
        value=(
            "**Drop:** Spectern (Lv 226 – Deusania’s Lab, Halloween Event)\n"
            "**Base ATK:** 187\n"
            "**Critical Rate:** +20\n"
            "**Accuracy:** -10%\n"
            "**Element:** Light\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='SUNNY SPRING ARROW',
        value=(
            "**Craft:** NPC Blacksmith (Hanami Event Recipe)\n"
            "**Base ATK:** 181\n"
            "**Stability:** 20%\n"
            "**Physical Pierce:** +5%\n"
            "**Magical Pierce:** +5%\n"
            "**Guard Break:** +5%\n"
            "**Element:** Light\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


@bot.command(name='darkarrow', aliases=['panahgelap'])
async def darkarrow(ctx):
    embed = discord.Embed(
        title='Dark Element Arrows',
        description='Daftar panah berelemen Dark lengkap dengan lokasi drop dan statistik.',
        color=discord.Color.dark_purple()
    )

    embed.add_field(
        name='TWILIGHT ARROW',
        value=(
            "**Drop:** Twilight Dragon (Lv 90/100/110/120/140 – Fort Solfini: Roof)\n"
            "**Base ATK:** 40\n"
            "**Stability:** 20%\n"
            "**Max HP:** -10%\n"
            "**Ailment Resistance:** +5%\n"
            "**Element:** Dark\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='SPIKY ARROW',
        value=(
            "**Drop:** Ivy (Lv 150–152 – Dark Dragon Shrine: Lower/Middle/Upper)\n"
            "**Base ATK:** 79\n"
            "**Stability:** 20%\n"
            "**Magic Resistance:** +5%\n"
            "**Reduce Damage (Floor):** +5%\n"
            "**Element:** Dark\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='[LIMITED EVENT] TWILIGHT SAKURA ARROW',
        value=(
            "**Drop:** Amalgam (Lv 140/160/180 – Twilight Sakura Castle: Top, Hanami Event)\n"
            "**Base ATK:** 100\n"
            "**Stability:** 20%\n"
            "**Light Resistance:** +5%\n"
            "**Element:** Dark\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='SPECTER ARROW',
        value=(
            "**Drop:** Manomare (Lv 169–172 – Phasma Forest: Area 1/2/3, Halloween Event)\n"
            "**Base ATK:** 120\n"
            "**Stability:** 20%\n"
            "**Additional Magic:** +50\n"
            "**Invincible Aid (Sec):** 1\n"
            "**Element:** Dark\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.add_field(
        name='EVIL GAZE ARROW',
        value=(
            "**Drop:** Corey (Lv 230–234 – Tower of Clamor, Winter Event)\n"
            "**Base ATK:** 190\n"
            "**Stability:** 20%\n"
            "**Accuracy:** +30%\n"
            "**Wind Resistance:** +10%\n"
            "**Element:** Dark\n"
            "*BEST ARROW to deal more damage*\n"
            "────────────────────────────"
        ),
        inline=False
    )

    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )

    await ctx.send(embed=embed)


####################Random############################
@bot.command(name='wishlistrei', aliases=['w'])
async def imitacia(ctx):
    embed = discord.Embed(title='Whishlist REI')
    embed.add_field(name='Level Boss', value='Normal : 109', inline=True)
    embed.add_field(
        name='Wishlist:',
        value=(
            "standie xavier tinggi 185cm\n"
            "standie akrilik yang kota dan bisa buka isinya xavier mandi\n"
            "plushie 30cm,60cm,1m xavier\n"
            "oppai pad xavier\n"))
    embed.set_image(url='https://cdn.discordapp.com/attachments/1189594050307825756/1360525924591866006/IMG_9419.jpg?ex=67fb7001&is=67fa1e81&hm=5b4b20a88a76235b0b203ab9f92f8ca5812b9858d10219ac823889c66b5ff0b7&')
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&'
    )
    await ctx.send(embed=embed)


######################################################################
logging.info("Bot starting...")
token = os.getenv('DISCORD_TOKEN')
if not token:
    logging.error("DISCORD_TOKEN is not found in environment variables.")
    exit(1)
else:
    logging.info(f"Token loaded successfully, attempting to log in...")

try:
    bot.run(token)
except Exception as e:
    logging.error(f"An error occurred while running the bot: {str(e)}")