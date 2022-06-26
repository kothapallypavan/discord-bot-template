from discord.ext import commands
import discord

class misc(commands.Cog):
    def __init__(self,bot:commands.Bot) -> None:
        self.client = bot

    #sample command
    @commands.command()
    async def ping(self, ctx: commands.Context):
        pembedVar = discord.Embed(
            description=" Latency  " + f"```{round(self.client.latency * 1000)} ms```"
            ,
            color=0xFF5733)
        await ctx.send(embed=pembedVar)


async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(
        misc(bot),
        guilds=[discord.Object(id=123)] #replace 123 with your server id
    )