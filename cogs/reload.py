import discord
from discord.ext import commands

#permiss = [int(line.rstrip('\n')) for line in open("cogs/text/Permissions.txt")]

#def perms():
#	def predicate(ctx):
#		return ctx.message.author.id in permiss
#	return commands.check(predicate)

class reload(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(hidden = True)
	@commands.guild_only()
	@commands.has_permissions(administrator = True)
#	@perms()
	async def reload(self,ctx):
		try:
			self.bot.reload_extension("cogs.sender")
			self.bot.reload_extension("cogs.message")
			self.bot.reload_extension("cogs.help")
			self.bot.reload_extension("cogs.names")

		except commands.ExtensionError as e:
			await ctx.send(f'{e.__class__.__name__}: {e}')
		else:
			await ctx.send(f"\N{GEAR} Reloaded ```ext.(sender)(message)(help)```")
			
def setup(bot):
	bot.add_cog(reload(bot))
