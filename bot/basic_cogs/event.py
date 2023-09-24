import discord
from discord.ext import commands
import logging

#Cog for discord event handling
class EventHandler(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self, message:discord.Message):
    #     pass 


    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self,payload: discord.RawReactionActionEvent):
    #     pass

    # Member joins server
    @commands.Cog.listener()
    async def on_guild_join(self, guild:discord.Guild):
        await self.bot.register_commands(force=True, guild_id=guild.id)
        logging.info(f"Joined {guild.name} {guild.id}")

    # Member leaves server
    # @commands.Cog.listener()
    # async def on_guild_remove(self, guild:discord.Guild):
    #     pass
        

def setup(bot:commands.Bot):
    bot.add_cog(EventHandler(bot))