import discord
from discord.ext import commands

# Admin/Dev only commands (put admin id in DEVS)
class Admin(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: discord.ApplicationContext):
        if ctx.author.id not in ctx.bot.DEVS:
            await ctx.send(f"{ctx.command.name} is a dev only command", delete_after= 5)
            return False
        return True;

    # Pong command
    @commands.command(name = "ping", aliases=["p"])
    async def ping(self, ctx:commands.Context):
        await ctx.send("Pong! Latency: {:.2f}".format(self.bot.latency * 1000), delete_after=5)
    
    # Purge command
    @commands.command(name = "purge", aliases=["pr"])
    async def purge(self, ctx:commands.Context, limit:int = 1):
        
        if not ctx.channel.permissions_for(ctx.guild.me).manage_messages:
            await ctx.send("I don't have permission to delete messages", delete_after=5)
            return
        
        await ctx.channel.purge(limit=limit+1)
        await ctx.send(f"{limit} messages purged", delete_after=5)



def setup(bot:commands.Bot):
    bot.add_cog(Admin(bot))