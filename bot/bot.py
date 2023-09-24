import discord
from discord.ext import commands
from discord import ui
import os,json
from pathlib import Path
import os
from dotenv import load_dotenv

from .database.db_setup import Database

# Bot subclass
class BotSubclass(commands.Bot):

    def __init__(self):

        load_dotenv()

        self._TOKEN = os.getenv('BOT_TOKEN')
        # self.db = Database(os.getenv('MONGODB_URI'))

        config_path = "config.json"
        self.ENVIRONMENT = "production"
        if os.path.exists('debug_config.json'): # Use configurations for test server
            config_path = 'debug_config.json'
            self.ENVIRONMENT = "development"

        # Get Tokens and global variables
        with open(config_path, "r") as config:
            self._DATA = json.load(config)

            # self._TOKEN = self._DATA["BOT_TOKEN"]
            self.PREFIX = self._DATA["BOT_PREFIX"]
            self.DEVS = self._DATA['DEVS']
            self.TEST_GUILDS = self._DATA['TEST_GUILDS']


        self.custom_cogs = {
            "admin": "basic_cogs.admin",
            "error": "basic_cogs.error",
            "event": "basic_cogs.event",
            "reloader": "basic_cogs.reloader",
            "example": "basic_cogs.example",
        }
        self._intents = discord.Intents().all()

        super().__init__(command_prefix=self.prefix, intents = self._intents, case_insensitive=True)

    #Bot login,logout and setup

    def setup(self):

        print("Starting to load cogs...")
        for cog_name,cog_path in self.custom_cogs.items():
            try:
                self.load_extension(f"bot.{cog_path}")
                print(f"Extension {cog_name} loaded.")
            except Exception as exc:
                print(f"Failed to load extension {cog_name}: {exc}")
                raise exc
        print('Completed loading cogs')

    def run(self):

        print('Running Bot')
        super().run(self._TOKEN)

    async def shutdown(self):
        print("Closing connection to Discord...")
        await super().close()

    async def close(self):
        print("Closing on keyboard interrupt...")
        await self.shutdown()

    async def on_connect(self):
        print(f"Connected to Discord (latency: {self.latency*1000:,.0f} ms).")

    async def on_resumed(self):
        print("Bot resumed.")

    async def on_disconnect(self):
        print("Bot disconnected.")

    async def on_ready(self):

        
        print(f"Logged in as {self.user}")

        await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{self.PREFIX}help"))
        print(discord.__version__)
        print(f"Running in {self.ENVIRONMENT} mode")

        if self.ENVIRONMENT == "development":
            for guild_id in self.TEST_GUILDS:
                await self.register_commands(force=True, guild_id=guild_id)
            print("Registered commands for test guilds")
        else:
            await self.register_commands(force=True)
            print("Registered commands for all guilds")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or(self.PREFIX)(bot, msg)


    