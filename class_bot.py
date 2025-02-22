# test-bot(bot class)
# This example requires the 'members' and 'message_content' privileged intents to function.
import os
import discord
import requests
import random
from discord.ext import commands
from bot_logic import gen_pass

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
# command prefix 
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})') # type: ignore
    print('------')
# random local meme image
@bot.command()
async def meme(ctx):
    # menampilkan secara random
    img_name = random.choice(os.listdir('meme'))
    with open(f'meme/{img_name}', 'rb') as f:
    # with open(f'meme/enemies-meme.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    await ctx.send(file=picture)
# API to get random dog and duck image 
def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    '''Setiap kali permintaan dog (anjing) dipanggil, program memanggil fungsi get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)
# adding two numbers
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)
# adding two numbers
@bot.command()
async def subtract(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)
    # adding two numbers
@bot.command()
async def multiply(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)
    # adding two numbers
@bot.command()
async def divide(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)
    # adding two numbers
@bot.command()
async def exponent(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left ** right)
# spamming word
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Setiap kali permintaan duck (bebek) dipanggil, program memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)   
# password generator        
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')
@bot.command()
async def bye(ctx):
    await ctx.send('\U0001f642')

@bot.command()
async def kerajinan(ctx):
    await ctx.send('berikut adalah tips membuat kerajinan dari bahan daur ulang https://www.sehataqua.co.id/kerajinan-dari-botol-plastik/')
@bot.command()
async def bahaya(ctx):
    await ctx.send('bahaya polusi sampah plastik https://plasticsmartcities.wwf.id/feature/article/sampah-plastik-ancaman-bagi-lingkungan-dan-kehidupan')
@bot.command()
async def pantauan(ctx):
    await ctx.send('pantauan cuaca harian https://www.bmkg.go.id/cuaca/prakiraan-cuaca/36.74.06.1008')

# coinflip
@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send('It is Head!')
    if num == 2:
        await ctx.send('It is Tail!')

# rolling dice
@bot.command()
async def dice(ctx):
    nums = random.randint(1,6)
    if nums == 1:
        await ctx.send('It is 1!')
    elif nums == 2:
        await ctx.send('It is 2!')
    elif nums == 3:
        await ctx.send('It is 3!')
    elif nums == 4:
        await ctx.send('It is 4!')
    elif nums == 5:
        await ctx.send('It is 5!')
    elif nums == 6:
        await ctx.send('It is 6!')
# overwriting kalimat.txt
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        text = ""
        text += my_string
        t.write(text)
# append kalimat.txt
@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        text = "\n"
        text += my_string
        t.write(text)
# reading kalimat.txt
@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        document = t.read()
        await ctx.send(document)
# welcome message
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore

bot.run('token')
