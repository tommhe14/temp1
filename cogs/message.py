import discord
from discord.ext import commands

class send_all(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	@commands.command()	
	async def send(self,ctx,*message_to_send):
		guild = ctx.message.guild
		output = ' '
		author = ctx.message.author
		for word in message_to_send:
			output += word
			output += ' '
		for member in self.bot.get_all_members():
			try:
				embed = discord.Embed(title="",colour = discord.Colour.green())
				embed.add_field(name="**From server:**",value= guild.name)
				embed.add_field(name = "**From Mod/Admin:**",value = author.name)
				embed.add_field(name="**Message:**",value = output)
			#	await ctx.send(embed=embed)
				
				await member.send(embed=embed)
			except (discord.HTTPException, discord.Forbidden,AttributeError):
				continue

	@commands.command(pass_context = True)
	async def play(self,ctx,*,arg):
		await self.bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.playing,name=arg))
		await ctx.send(f"> Now Playing ``{arg}``")

	@commands.command(pass_context = True)
	async def watch(self,ctx,*,arg):
		await self.bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching,name=arg))
		await ctx.send(f"> Watching ``{arg}``")
	
def setup(bot):
	bot.add_cog(send_all(bot))
