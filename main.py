import discord
from discord.ext import commands

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix = "-",
            intents = discord.Intents.all(),
            application_id = 123) #replace 123 with your bot id

    async  def setup_hook(self):
        #add cogs here
        await self.load_extension("cogs.misc")  #misc.py in cogs folder

        await bot.tree.sync(guild=discord.Object(id=123)) #replace 123 with your server id(guild id)

    async def close(self):
        await super().close()
        await self.session.close()

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

bot = MyBot()
bot.run("your_bot_token")