import discord
from discord.ext import commands

#Reloader cog for loading and unloading Cogs directly from discord
class Reloader(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: discord.ApplicationContext):
        if ctx.author.id not in ctx.bot.DEVS:
            msg = await ctx.send(f"{ctx.command.name} is a dev only command")
            await msg.delete(delay=5)
            return False
        return True;

    #A command to load extension directly from discord
    @commands.command(name = "load", aliases=["l"])
    async def  load(self, ctx:commands.Context,extension:str):
        try:
            cog_path = self.bot.custom_cogs[extension]
        except KeyError:
            await ctx.send(f"{ctx.author.mention} your extension doesn't exist", delete_after=5)
        else:
            try:
                self.bot.load_extension('bot.'+cog_path)
            except Exception as exc:
                await ctx.send(f'Failed to load {extension}: {exc}', delete_after=5)
            else:
                await ctx.send(f'{extension} loaded', delete_after=5)
            await self.bot.register_commands()
            await ctx.message.delete(delay=5)

    #A command to unload extension directly from discord
    @commands.command(name = "unload", aliases=["u"])
    async def  unload(self, ctx:commands.Context,extension:str):
        try:
            cog_path = self.bot.custom_cogs[extension]
        except KeyError:
            await ctx.send(f"{ctx.author.mention} your extension doesn't exist", delete_after=5)
        else:
            try:
                self.bot.unload_extension('bot.'+cog_path)
            except Exception as exc:
                await ctx.send(f'Failed to unload {extension}: {exc}', delete_after=5)
            else:
                await ctx.send(f'{extension} unloaded', delete_after=5)
            await self.bot.register_commands()
            await ctx.message.delete(delay=5)
    

    # A command to reload cogs directly from discord
    @commands.command(name = "reload",aliases=["r"])
    async def  reload(self, ctx:commands.Context,extension:str):
        try:
            cog_path = self.bot.custom_cogs[extension]
        except KeyError:
            await ctx.send(f"{ctx.author.mention} your extension doesn't exist", delete_after=5)
        else:
            try:
                self.bot.unload_extension('bot.'+cog_path)
            except:
                pass
            finally:
                try:
                    self.bot.load_extension('bot.'+cog_path)
                except Exception as exc:
                    await ctx.send(f'Failed to reload {extension}: {exc}', delete_after=5)
                else:
                    await ctx.send(f'{extension} reloaded', delete_after=5)
            await self.bot.register_commands()
            await ctx.message.delete(delay=5)


def setup(bot:commands.Bot):
    bot.add_cog(Reloader(bot))
