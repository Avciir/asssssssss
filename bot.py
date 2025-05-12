import discord
import asyncio
import os
from discord.ext import commands
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Bot configuration
PREFIX = "!"
STATUSES = [".gg/tradeblox", ".gg/tradeblox", ".gg/tradeblox"]

class StatusBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix=PREFIX, intents=intents)
        self.current_status = 0

    async def cycle_status(self):
        while True:
            try:
                activity = discord.Activity(
                    type=discord.ActivityType.playing,
                    name=STATUSES[self.current_status]
                )
                await self.change_presence(activity=activity)
                self.current_status = (self.current_status + 1) % len(STATUSES)
                await asyncio.sleep(1)
            except Exception as e:
                print(f"Status error: {e}")
                await asyncio.sleep(5)

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")
        self.loop.create_task(self.cycle_status())

bot = StatusBot()

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Bot crashed: {e}")
