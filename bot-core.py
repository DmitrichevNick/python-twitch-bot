import config
import random
from twitchio.ext import commands
import functions
from MessageCollector import MessageCollector 
import asyncio
from threading import Thread
import time 
import nest_asyncio

nest_asyncio.apply()

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=config.TMI_TOKEN, prefix=config.BOT_PREFIX, initial_channels=config.CHANNEL)

    async def event_ready(self):
        print(f"{self.nick} родился")
        
    @commands.command(name='roll')
    async def roll(self, ctx: commands.Context):
        print('roll')
        message_text = ctx.message.content
        rollNum = message_text.split(' ')
        print(rollNum)
        if len(rollNum) > 1 and rollNum[1].isnumeric():
            print(rollNum[1])
            await ctx.channel.send(f"{ctx.author.name} накрутил {random.randrange(0,int(rollNum[1]),1)}!")
        elif len(rollNum) > 1 and rollNum[1].lower() == 'help':
            await ctx.channel.send(f"{ctx.author.name}, you can specify a number to roll between 0 and the number specified. If you do not specify a number, you will roll 100.")
        elif len(rollNum) > 1 and rollNum[1].lower() != 'help':
            await ctx.channel.send(f"{ctx.author.name}, you did not select a number to roll")
        else:
            await ctx.channel.send(f"{ctx.author.name} накрутил {random.randrange(0,100,1)}!")
            
    def start_listen(self):
        while len(self.connected_channels) == 0:
            time.sleep(0.5)
        
        message_collector = MessageCollector()
        message_collector.start()
        message_collector.listen_input(self.connected_channels[0])
           
    @commands.command(name='melody')
    async def melody(self, ctx: commands.Context):
        link = ctx.message.content.split(' ')[1]
        result = functions.download_youtube_song(link)
        if result is not None and len(result) > 0:
            await ctx.channel.send(f"{ctx.author.name} {result}!")
            
if __name__ == "__main__":
    bot = Bot()  
    botThread = Thread(target=bot.run)
    botThread.start()
    
    listenThread = Thread(target=bot.start_listen)
    listenThread.start()
    
    botThread.join()
    listenThread.join()
    