import discord
from discord.ext import commands

# https://github.com/Pycord-Development/pycord/tree/master/examples/app_commands

class ExampleCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @discord.slash_command(name="hello", description="slash command hello")
    async def hello_slash(self, ctx:discord.ApplicationContext, member: discord.Member = None):
        await self.respond(ctx, member if member else ctx.author)

    @discord.user_command(name="hello", description="user command hello")
    async def hello_user(self, ctx : discord.ApplicationContext, member : discord.Member):
        await self.respond(ctx, member)

    @discord.message_command(name="hello", description="message command hello")
    async def hello_message(self, ctx : discord.ApplicationContext, message : discord.Message):
        await self.respond(ctx, message.author)

    async def respond(self, ctx:discord.ApplicationContext, member: discord.Member):
        embed = discord.Embed(title=f"Hello {member.name}", description="This is a test slash command", color=discord.Color.random())
        embed.set_thumbnail(url=member.display_avatar.url)

        embed.add_field(name="Guild", value=ctx.guild.name)
        embed.add_field(name="Guild Id: ", value=ctx.guild.id)

        embed.add_field(name="Channel", value=ctx.channel.name, inline=False)
        embed.add_field(name="Channel Id", value=ctx.channel.id)

        embed.add_field(name="User", value=member.name, inline=False)
        embed.add_field(name="User Id", value=member.id)

        view = self.View()

        await ctx.respond(embed=embed, view=view)

    class View(discord.ui.View):
        
        def __init__(self):
            super().__init__()

        @discord.ui.button(label="Click", style=discord.ButtonStyle.primary)
        async def click(self, button: discord.ui.Button, interaction: discord.Interaction):
            await interaction.response.defer()

            if button.label == "Click":
                now = 0
            else:
                now = int(button.label.split(":")[1])

            button.label = f"Clicked: {now + 1}"
           
            await interaction.message.edit(view = button.view)



def setup(bot:commands.Bot):
    bot.add_cog(ExampleCog(bot))