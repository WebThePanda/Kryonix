from discord.ext import commands
import discord
from ..utils.premium import serverHasPremium

class Autorole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, member: discord.Member):
        serverHasPremium()
        if ctx.guild in data:
            role = ctx.guild.get_role(1487881402740379888)

            if role:
                await member.add_roles(role)
                await ctx.send(f"Gave {member.display_name} the role '{role}'")
            else:
                await ctx.send(f"Role not found.")
        else:
            ctx.send("This is a premium feature. You can get premium at [Kryonix Patreon]()")

async def setup(bot):
    await bot.add_cog(Autorole(bot))