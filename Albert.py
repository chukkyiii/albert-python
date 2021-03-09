import discord
from keep_alive import keep_alive
from discord.ext import commands


bot = commands.Bot(".")


@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)


@bot.event
async def on_message(message):
    print("User Has Sent A Message!")

    if message.content.startswith("hi"):
        await message.channel.send("hello" + ' ' + str(message.author))

    if message.content.startswith("Who am I"):
        await message.channel.send("You are " + " " + str(message.author))

    if message.content.startswith("Does Adam have bad aim?"):
        await message.channel.send(":clap: Yh definetly!")

    if message.content.startswith("Does Adam have an IQ of 6?"):
        await message.channel.send(":clap: Yes for sure!")

    if message.content.startswith("Hmm what are you"):
        await message.channel.send("I am centient...")

    await bot.process_commands(message)


@bot.command()
async def ping(message):
    await message.send(".ping")


@bot.command()
async def echo(albert, *args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await albert.send(output)


@bot.command()
async def clear(albert, amount=100):
    try:
        await albert.channel.purge(limit=amount)
        print("Message Deleted!")
        await albert.send("Message Deleted!")
    except discord.ext.commands.errors.CommandInvokeError:
        print("I'm not Administrator")


@bot.command()
async def identify(message):
    await message.channel.send(message.author.id)

keep_alive()
token = 'your token'

bot.run(token)

# NOTE: i think a predifined albert with ctx like a normal function
