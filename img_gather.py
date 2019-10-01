#C:\Users\Macks\AppData\Local\Programs\Python\Python36\python.exe
import discord
import requests

client = discord.Client()

dst_folder = "OGS_SRC_IMGS"

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Retrieving all nudes"))
    i = 0
    j = 0
    f = open('img_urls.txt', 'w')
    async for message in client.logs_from(client.get_channel('195155264574324748'), limit = 1000000):
        for embed in message.embeds:
            # if True: #the worst debugging tool
            try:
                url = embed['thumbnail']['url']
                i += 1
                # with open(dst_folder+"\\src_{}.jpg".format(i), "wb") as f:
                #     f.write(requests.get(url).content)
                #     f.close()
                f.write("{}, ".format(url))
            except:
                print("Whoopsies.")
        channels = client.get_all_channels()
        for attachment in message.attachments:
            channels = client.get_all_channels()
            # if True:
            try:
                url = attachment['url']
                i += 1
                # with open(dst_folder+"\\src_{}.jpg".format(i), "wb") as f:
                #     f.write(requests.get(url).content)
                #     f.close()
                f.write("{}, ".format(url))
            except:
                print("Whoopsies.")
        channels = client.get_all_channels()
        j += 1
        if j % 100 == 0:
            # await client.send_message(client.get_channel('543604746968367104'), "I have to send this message or I die! :weary:")
            print("Wrote message #{}".format(j))
    f.close()
    print("All done!")
    await client.send_message(client.get_channel('543604746968367104'), "Nudes retrieved. :kissing_heart:")
    # async client.send_message(client.get_channel('195155264574324748'),"I'm done something else daddy!")

client.run('MjAxNDA5OTYxNTg1MTQ3OTA0.DzOzfw.tF3GeoQUli39rHmio2BUMNnDdS4')
