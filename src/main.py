from multiprocessing.connection import wait
from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.presences = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 0000  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command(name="name")
async def send(ctx):
    await ctx.send(ctx.message.author.name)

@bot.command(name="d6")
async def send(ctx):
    await ctx.send(random.randint(1, 6))

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde":
        await message.channel.send("Salut tout seul " + message.author.mention)
    await bot.process_commands(message)

@bot.command(name="admin")
async def roles(ctx, *args):
    permissions = discord.Permissions.all()
    if not discord.utils.get(ctx.guild.roles, name="administrator") :
        await ctx.guild.create_role(name="administrator", permissions=permissions)

    role = discord.utils.get(ctx.guild.roles, name="administrator")
    for r in args:
        user = discord.utils.get(ctx.guild.members, name=r)
        await user.add_roles(role)

@bot.command(name="ban")
async def ban(ctx, arg1):
    user = discord.utils.get(ctx.guild.members, name=arg1)
    await user.ban()

@bot.command(name="count")
async def count(ctx):
    off = 0
    on = 0
    d = 0 
    idle = 0
    for user in ctx.guild.members:
        if str(user.status) == "offline":
            off += 1
        if str(user.status) == "online":
            on += 1
        if str(user.status) == "dnd":
            d += 1
        if str(user.status) == "idle" :
            idle += 1
    await ctx.send("Il y a " + str(off) + " absent")
    await ctx.send("Il y a " + str(on) + " actif")
    await ctx.send("Il y a " + str(d) + " ne pas déranger")
    await ctx.send("Il y a " + str(idle) + " innactif")

    
token = ""
bot.run(token)  # Starts the bot