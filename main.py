import os
import discord
import pytz
from datetime import datetime 

intents = discord.Intents.default()
intents.message_content = True


client = discord.Client(intents=intents)

#function to respond on messages
@client.event
async def on_message(message):
  #to get idea of what we got 
  print('message got: {}, with attachments {} and type is {}'.format(message.content, message.attachments, type(message.content)))

  # if bot sends timestamp or some other comment its free to send text
  if message.author == client.user and not message.content.startswith("$NOTE"):
    return

  #if bot sends note, It'll be deleted
  if message.author == client.user and message.content.startswith("$NOTE"):
    await message.delete()
    
  #if any other member sends text
  if len(message.attachments)==0:
    #if asking for help
    if message.content == '\help watcher':
      await message.channel.send('$help : please refer here --> https://github.com/Adiziel/Watcher#readme')
    else:
      print('Deleting text')
      await message.delete()

  # if message has attachments
  if message.attachments:
    #if message has attachemnt and text, it'll be deleted
    if len(message.content)>0:
      await message.delete()
      await message.channel.send("$NOTE : Please don't put text")
    #if message has only attachment timestamp will be added
    elif len(message.content)==0:
      await message.channel.send("$Timestamp {}".format(datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d/%m/%Y %H:%M:%S")))

  



client.run(os.environ['token'])
