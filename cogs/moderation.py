from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

    @commands.command()
    async def unban(self, ctx, userID: int):
        user = await self.bot.fetch_user(userID)
        await ctx.guild.unban(user)
        await ctx.send(f"Unbanned {user.mention}")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        await ctx.message.delete()
        
        deleted_messages = await ctx.channel.purge(limit=amount)
        await ctx.send(f"Purged {len(deleted_messages)} message(s).", delete_after=5)


async def setup(bot):
    await bot.add_cog(Moderation(bot))