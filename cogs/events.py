from discord.ext import commands
import discord

print("Hi")

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Cog loaded.")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f"DEBUG: {member.name} has joined the server!")
        
        role_id = 1487881402740379888
        role = member.guild.get_role(role_id)

        await member.add_roles(role)

async def setup(bot):
    await bot.add_cog(Events(bot))