import discord # type: ignore
from discord.ext import commands, tasks
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import asyncio
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


intents = discord.Intents.default()
intents.message_content = True  
bot = commands.Bot(command_prefix='bwa', intents=intents)

scheduler = AsyncIOScheduler()  

notifications = [
    {"time": "23:45:00", "days": ["tue", "thu", "wed"], "sound": "Kano - 【Rabinva】Stella-rium by Geomacher on Smule- Social Singing Karaoke App_5(2).mp3"},
  
]

# Waktu masuk dan keluar voice channel
voice_schedule = [
    {"join_time": "23:45:00", "leave_time": "23:50:00", "days": ["tue", "thu", "wed"], "voice_channel_id": 1005098144251527218},
]


async def play_sound(voice_channel_id, sound_file):
    voice_channel = bot.get_channel(voice_channel_id)
    if voice_channel is not None:
        if not bot.voice_clients:
            voice_client = await voice_channel.connect()
        else:
            voice_client = bot.voice_clients[0]
        audio_source = discord.FFmpegPCMAudio(sound_file)
        if not voice_client.is_playing():
            logging.info(f"Memutar suara {sound_file} di channel {voice_channel.name}")
            voice_client.play(audio_source)
            while voice_client.is_playing():
                await asyncio.sleep(1)


async def join_voice_channel(voice_channel_id):
    voice_channel = bot.get_channel(voice_channel_id)
    if voice_channel is not None and not bot.voice_clients:
        await voice_channel.connect()
        logging.info(f"Bot bergabung ke voice channel {voice_channel.name}")

async def leave_voice_channel(voice_channel_id):
    for vc in bot.voice_clients:
        if vc.channel.id == voice_channel_id:
            await vc.disconnect()
            logging.info(f"Bot meninggalkan voice channel {vc.channel.name}")


for notification in notifications:
    time = notification["time"]
    days = notification["days"]
    sound_file = notification["sound"]
    hour, minute, second = map(int, time.split(':'))
    for day in days:
        scheduler.add_job(play_sound, CronTrigger(day_of_week=day, hour=hour, minute=minute, second=second), args=[1189594050307825756, sound_file])

for schedule in voice_schedule:
    join_time = schedule["join_time"]
    leave_time = schedule["leave_time"]
    days = schedule["days"]
    voice_channel_id = schedule["voice_channel_id"]
    join_hour, join_minute, join_second = map(int, join_time.split(':'))
    leave_hour, leave_minute, leave_second = map(int, leave_time.split(':'))
    for day in days:
        scheduler.add_job(join_voice_channel, CronTrigger(day_of_week=day, hour=join_hour, minute=join_minute, second=join_second), args=[voice_channel_id])
        scheduler.add_job(leave_voice_channel, CronTrigger(day_of_week=day, hour=leave_hour, minute=leave_minute, second=join_second), args=[voice_channel_id])


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

#JS
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
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357541749253214349/image.png?ex=67f094c6&is=67ef4346&hm=89f7d76fba96caeaebc6b42d8e501e7031d4e879400db2dd69137072712c3846&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


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


@bot.command(name='xguardgolem', aliases=['xgg'])
async def xguardgolem(ctx):
    embed = discord.Embed(title='Guard Golem')
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


@bot.command(name='xvulture', aliases=['xvul'])
async def xvulture(ctx):
    embed = discord.Embed(title='Vulture')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357551447809593525/image.png?ex=67f09dcf&is=67ef4c4f&hm=4739ea02cc1dc829c61c0d19dc44c44660bdbec05262cc0f30b90f165b1cd74c&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


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


@bot.command(name='xsupreme', aliases=['xsecb'])
async def xsupreme(ctx):
    embed = discord.Embed(title='Supreme Evil Crystal Beast')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553925514854610/image.png?ex=67f0a01d&is=67ef4e9d&hm=429cc58317969e149153790d459f47b9d1518ba302c3297cbdef0d154837c3b4&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xpiscruva', aliases=['xpiscru'])
async def xpiscruva(ctx):
    embed = discord.Embed(title='Piscruva')
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357553823274762360/image.png?ex=67f0a005&is=67ef4e85&hm=6c565c1f709354c4e1e3fcdeb763b380e675ebb34a6fda33e0635c733371e763&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


@bot.command(name='xbakuza', aliases=['xbaku'])
async def xbakuza(ctx):
    embed = discord.Embed(title='Bakuzan')
    embed.add_field(name='Upgrade', value='Ganglef>Tyrant Machina>Vulture>Mimyugon>Bakuzan', inline=True)
    embed.set_image(url='https://cdn.discordapp.com/attachments/696678783465553990/1357554048068354208/image.png?ex=67f0a03b&is=67ef4ebb&hm=e258b0d8bc408666ff8dacbcc76769cb79d6104612ed792d108c0516f4b0b702&')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/945573573827911680/1357330845920268429/WM_PNG.png?ex=67efd05b&is=67ee7edb&hm=45b4587d235223ee3806eca9d31e499115c9061c560464e322ff580c6ca542f7&')
    await ctx.send(embed=embed)


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