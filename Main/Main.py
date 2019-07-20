# Created by Seth Banker, A.K.A. scar430, A.K.A. a really cool guy B)
# Poorly optimized at the moment, I'm working on it.

import discord
import json
from discord.utils import find
from Intelligence import *

print('Application has started.')

# Pulling data from Main/config.json
with open('config.json', 'r') as f:
    config = json.load(f)

token = config['token'] # login token.
loadFromFile = config['loadFromFile'] # Are we loading trained data or are we going to start training?
version = config['version'] # What version of the bot this is, used in the greeter embed.
features = config['features'] # What features the bot offers, used in ther greeter / updated embeds.

embed = None

class MyClient(discord.Client):

    async def on_ready(self):
        appInfo = await client.application_info()

        print('Logged on as', self.user)
        print(appInfo)

    async def on_guild_join(self, guild):

        print('Joined guild : "{}"'.format(guild.name))

        # Put this in the #general channel, if that is absent then put it in the first channel available
        general = find(lambda x: x.name == 'general',  guild.text_channels)
        if general:
            send = await general.send('', embed=embed)
            await send.pin()
            print('Sent Tutorial.')
            return

    async def on_message(self, message):

        appInfo = await client.application_info()

        # Create the greeter embed
        embed = discord.Embed(title="{}".format(appInfo.name), description="{}".format(appInfo.description), color=0xf64b4b)
        embed.add_field(name="How to talk to Chat Bot", value='''In order to talk to Chat Bot,
         you must begin your message by mentioning the bot and then typing your desired input.
         \nInput :\n`@Chat Bot#9213 Hello!`\nOutput :\n`@User#1234 hello ...`''', inline=False)

        field=""
        # Create the string for the features field
        for num in range(len(features)):
            new = "\n - {}".format(features[num])
            field += new
        
        embed.add_field(name="Current Features", value=field)
        embed.set_footer(text="Created by {}. | {}".format(appInfo.owner.name, version), icon_url='')

        # Don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            print("Pong")
            await message.channel.send('Pong')
            return

        try:
            # When the message isn't empty, the estimated output is not null, and the first mention is Chat Bot, then send the output message.
            if message.content != '' and message.mentions[0] == self.user:

                # get app info prepared in case someone wants help.
                appInfo = await client.application_info()

                # check if the message was a help command first, if not then continue
                if message.content == '{} help'.format(self.user.mention):
                    print('Help was requested ...')
                    await message.channel.send("", embed=embed)
                    print('Help was sent.')
                    return
                else:
                    print("Recieved input...")
                    await message.channel.send("{} ".format(message.author.mention) + evaluateInput(message, encoder, decoder, searcher, voc))
                    print("Sent output.")
                    return

        # Don't worry about this.
        except IndexError:
            return


client = MyClient()
client.run(token)