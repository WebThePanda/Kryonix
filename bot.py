import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv
import time

load_dotenv()

aiApiToken = os.getenv("ai-api")
botToken = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

COGS = [
    "cogs.autorole",
    "cogs.events",
    "cogs.game",
    "cogs.levels",
    "cogs.moderation",
]

async def load_cogs():
    for cog in COGS:
        try:
            await bot.load_extension(cog)
            print(f"✅ Loaded {cog}")
        except Exception as e:
            print(f"❌ Failed to load {cog}: {e}")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.command(name="loadCog")
@commands.is_owner()
async def loadCog(ctx, cog):
    cogChannelID = 1488375465285779456
    cogChannel = bot.get_channel(cogChannelID)

    if cogChannel == None:
        await ctx.send("CogChannel is None. Please take a look at your code to fix :)")
    elif ctx.channel.id != cogChannelID:
        await ctx.send(f"Wrong channel. Please try again in {cogChannel.mention}.")
    elif cog == "all":
        loaded = []
        failed = []
        for cog in COGS:
            try:
                if cog not in bot.extensions:
                    await bot.load_extension(cog)
                    loaded.append(cog)
            except Exception as e:
                failed.append(f"`{cog}`: {e}")
        
        msg = ""
        if loaded:
            msg += f"Loaded {len(loaded)} cog(s): {', '.join(f'`{cog}`' for cog in loaded)}\n"
        if failed:
            msg += f"Failed: {', '.join(failed)}\n"
        if not loaded and not failed:
            msg = "All cogs are already loaded."

        await ctx.send(msg)
    else:
        if cog.lower() in bot.extensions:
            await ctx.send(f"{cog.lower()} is already loaded.")
        else:
            try:
                await bot.load_extension("cogs." + cog.lower())
                await ctx.send(f"Successfully loaded `{cog.lower()}`.")
            except commands.ExtensionNotFound:
                await ctx.send(f"No cog named `{cog.lower()}` was found.")
            except Exception as e:
                await ctx.send(f"Failed to load `{cog.lower()}`: {e}")

@loadCog.error
async def loadCog_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to specify a cog to load. If you wanna load all unloaded cogs, do `!loadCog all`")

@bot.command(name="unloadCog")
@commands.is_owner()
async def unloadCog(ctx, cog):
    cogChannelID = 1488375465285779456
    cogChannel = bot.get_channel(cogChannelID)

    if cogChannel == None:
        await ctx.send("CogChannel is None. Please take a look at your code to fix :)")
    elif ctx.channel.id != cogChannelID:
        await ctx.send(f"Wrong channel. Please try again in {cogChannel.mention}.")
    elif cog == "all":
        unloaded = []
        failed = []
        for cog in COGS:
            try:
                if cog not in bot.extensions:
                    await bot.unload_extension(cog)
                    unloaded.append(cog)
            except Exception as e:
                failed.append(f"`{cog}`: {e}")
        
        msg = ""
        if unloaded:
            msg += f"Unloaded {len(unloaded)} cog(s): {', '.join(f'`{cog}`' for cog in unloaded)}\n"
        if failed:
            msg += f"Failed: {', '.join(failed)}\n"
        if not unloaded and not failed:
            msg = "All cogs are already unloaded."

        await ctx.send(msg)
    else:
        if cog.lower() in bot.extensions:
            await ctx.send(f"{cog.lower()} is already unloaded.")
        else:
            try:
                await bot.unload_extension("cogs." + cog.lower())
                await ctx.send(f"Successfully unloaded `{cog.lower()}`.")
            except commands.ExtensionNotFound:
                await ctx.send(f"No cog named `{cog.lower()}` was found.")
            except Exception as e:
                await ctx.send(f"Failed to unload `{cog.lower()}`: {e}")

@unloadCog.error
async def unloadCog_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to specify a cog to unload. If you wanna unload all unloaded cogs, do `!unloadCog all`")

@bot.command(name="reloadCog")
@commands.is_owner()
async def reloadCog(ctx, cog):
    cogChannelID = 1488375465285779456
    cogChannel = bot.get_channel(cogChannelID)

    if cogChannel == None:
        await ctx.send("CogChannel is None. Please take a look at your code to fix :)")
    elif ctx.channel.id != cogChannelID:
        await ctx.send(f"Wrong channel. Please try again in {cogChannel.mention}.")
    else:
        if cog == "all":
            for cog in COGS:
                await bot.reload_extension(cog)

            msg = "All cogs reloaded"
            await ctx.send(msg)
        else:
            await bot.reload_extension("cogs." + cog.lower())
            await ctx.send(f"Reloaded {cog.lower()}")

@reloadCog.error
async def reloadCog_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to specify a cog to reload. If you wanna reload all cogs, do `!reloadCog all`")

@bot.command(name="listCogs")
@commands.is_owner()
async def listCogs(ctx):
    embed = discord.Embed(title="Cogs", color=discord.Color.dark_blue())

    for cog in COGS:
        loaded = cog in bot.extensions
        status = "Loaded" if loaded else "Unloaded"
        embed.add_field(name=cog, value=status, inline=False)
    
    await ctx.send(embed=embed)

async def main():
    async with bot:
        await load_cogs()
        await bot.start(botToken)

asyncio.run(main())