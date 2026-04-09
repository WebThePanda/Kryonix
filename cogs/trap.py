from discord.ext import commands
import discord


class Trap(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        trap_channel = 1491687315905446048

        if message.channel.id == trap_channel:
            await message.delete()
            await message.author.ban()

async def setup(bot):
    await bot.add_cog(Trap(bot))