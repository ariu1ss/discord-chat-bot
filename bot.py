import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Define the message to be posted
MESSAGE = (
    "**🔎 Looking for cheaper gems 💎 or Brawl Pass 🎟️? **\n"
    "**Get them cheaper here ⬇️**\n\n"
    "**https://discord.com/channels/1207773158950834176/1261014049647231086**"
)

# Set up the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Start the task to post the message every hour
    post_message.start()

@tasks.loop(hours=1)
async def post_message():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(MESSAGE)
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")

# Run the bot
bot.run(DISCORD_TOKEN)
