import discord
from discord.ext import commands

# Load the bot token from a token file or environment variables
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Load cogs
@bot.event
async def on_ready():
    print(f'\nLogged in as: {bot.user.name} | ID: {bot.user.id}')
    # Load cogs here
    # for cog in cogs:
    #     bot.load_extension(cog)

bot.run(TOKEN)