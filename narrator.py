#!/usr/bin/python36
#C:\Users\Macks\AppData\Local\Programs\Python\Python36\python.exe
import discord
import random
from datetime import datetime
from word_gen import MessageGenerator
from mine_gen import Minesweeper
from bulge_gen import Bulgesweeper

client = discord.Client()

generator = MessageGenerator()

valid_users = {'macks':'Pikalover208#1521', 'malcolm':'Meepithmancer#1949',
 'eric':'Yreid#3772', 'graeme':'Triblendlightning#8681',
 'riley':'archiem#9414', 'adam':'ads3500#5349',
 'iain':'iain_theginger#3818', 'everyone':'everyone'}

@client.event
async def on_ready():
    file = open('lastmsg.txt', 'r')
    lastmsg = datetime.strptime(file.readline(),'%Y-%m-%d %H:%M:%S.%f')
    file.close()

    file = open('masterlogs_ogs.txt', 'a', encoding = "utf-8")

    async for message in client.logs_from(client.get_channel('195155264574324748'), limit = 1000000, after = lastmsg):
        if (message.author != client.user) and (len(message.content.replace("\n"," ")) != 0) and not (message.content.startswith("!")):
            file.write(str(message.author) + " " + str(message.content.replace("\n"," ")) + "\n")

    file.close()

    file = open('lastmsg.txt', 'w')
    file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    file.close()

    try:
        with open("GENERATED_FACES\\face_{}.jpg".format(random.randint(1, 5206)), 'rb') as f:
            await client.edit_profile(avatar=f.read())
    except:
        print("Haha no faces for you friendo yeeeeeet")

    await client.change_presence(game = discord.Game(name = "with the fabric of society"))

    source = open('masterlogs_ogs.txt', 'r', encoding = "utf-8")
    generator.import_msgs(source)

    await client.send_message(client.get_channel('195155264574324748'),"I'm done daddy! :weary:")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!genmessage"):
        try:
            user = message.content.split()[1].lower()
            msg = generator.generate_message(valid_users[user])

            await client.send_message(message.channel, msg)

        except KeyError:
            await client.send_message(message.channel, "Not a valid user :no_good:")
    if message.content.startswith("!minesweeper"):
        try:
            size = int(message.content.split()[1])
            if size < 3:
                await client.send_message(message.channel, "Too small.")
            elif size > 14:
                await client.send_message(message.channel, "Too big.")
            else:
                mines = Minesweeper(size)

            await client.send_message(message.channel, mines.msg_board())
        except TypeError:
            await client.send_message(message.channel, "Yeah idk what that is but it's not a number dawg.")
    if message.content.startswith("!bulgesweeper"):
        try:
            size = int(message.content.split()[1])
            if size < 3:
                await client.send_message(message.channel, "Oh daddy that's too small for a widdle princess like me")
            elif size > 14:
                await client.send_message(message.channel, "Unh 😩! Daddy that's too big!")
            else:
                mines = Bulgesweeper(size)

            await client.send_message(message.channel, mines.msg_board())
        except TypeError:
            await client.send_message(message.channel, "\\*notices not an int* OwO what's this")
    if message.content.startswith("!skull"):
        try:
            with open("GENERATED_FACES\\face_{}.jpg".format(random.randint(1, 5206)), 'rb') as f:
                await client.edit_profile(avatar=f.read())
                await client.send_message(message.channel, "Sweet dreams, daddy! :skull:")
        except:
            await client.send_message(message.channel, "Nah, Discord didn't like that one fam. :triumph:")

client.run('MjAxNDA5OTYxNTg1MTQ3OTA0.DzOzfw.tF3GeoQUli39rHmio2BUMNnDdS4')
