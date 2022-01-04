import config
import random
from twitchio.ext import commands
import functions

class Bot(commands.Bot):
    def __init__(self):
      
        super().__init__(token=config.TMI_TOKEN, prefix=config.BOT_PREFIX, initial_channels=config.CHANNEL)

    async def event_ready(self):
        print(f"{self.nick} родился")

    @commands.command(name='roll')
    async def roll(self, ctx: commands.Context):
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

    @commands.command(name='melody')
    async def roll(self, ctx: commands.Context):
        link = ctx.message.content.split(' ')[1]
        result = functions.download_youtube_song(link)
        if result is not None and len(result) > 0:
            await ctx.channel.send(f"{ctx.author.name} {result}!")

    # @commands.command()
    # async def hello(self, ctx: commands.Context):
    #     # Send a hello back!
    #     await ctx.send(f'Hello {ctx.author.name}!')

# bot = commands.Bot(
#     irc_token=config.TMI_TOKEN,
#     client_id=config.CLIENT_ID,
#     nick=config.BOT_NICK,
#     prefix=config.BOT_PREFIX,
#     initial_channels=config.CHANNEL
# )

# bot_name = config.BOT_NICK
# @bot.event
# async def event_ready():
#     print(f"{bot_name} родился")

 
# @bot.event
# async def event_message(ctx):
#     if ctx.author.name.lower() == bot_name.lower():
#         return
#     await bot.handle_commands(ctx)
#     print(f'{ctx.channel} - {ctx.author.name}: {ctx.content}')
     
 

if __name__ == "__main__":
    bot = Bot()
    bot.run()