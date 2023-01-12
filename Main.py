import discord
import DiscordOutput as do
import exceptionRecorder as er
import key
import reboot
import DoDB as db
import os

key = key.getKey()
try:
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)
except:
    client = discord.Client()


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            return #ignores the bot's own messages.

        if message.content.lower().startswith('!test') or message.content.lower().startswith('!eval'):
            eval = do.evalHandler(message)
            try:
                if eval.message != True:
                    await message.channel.send(eval.message)
                else:
                    fileName = (str("Eval{}.txt").format(eval.count)) #name of the file sent to discord
                    fileXfer = discord.File("temp"+ eval.charName + ".txt", filename=fileName, spoiler = False)
                    await message.channel.send(file = fileXfer) #sends to discord temp eval file
                    os.remove("temp"+ str(eval.charName) + ".txt") #cleans up the temp eval file
                    if str(message.author) != 'Slavell#8770' or str(message.author) != 'Sajuuk#4711':
                        pass
                    else:
                        db.setEval(eval.charName, eval.author, "Pass")
            except:
                db.setEval(eval.charName, eval.author, "Fail")


        if message.content.lower().startswith('!add'):
            add = do.addHandler(message)
            await message.channel.send(add.message)
            

        if message.content.lower().startswith('!my name is'):
            get = do.nameHandler(message)
            await message.channel.send(get.message)
        
        if message.content.lower().startswith('!get names'):
            get = do.getHandler(message)
            await message.channel.send(get.message)
            

        if message.content.lower().startswith("reboot") or message.content.lower().startswith("restart") and message.author == "Slavell#8770" or message.author == "Sajuuk#4711":
            await message.channel.send("Stood too close to the rabbit, eh? Chaos is now rising up.")
            reboot.reboot()
    except:
        er.basicHandler()



client.run(key)