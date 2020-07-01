import discord
from discord.ext import commands
from typing import Union
import random



class FetchedUser(commands.Converter):
	async def convert(ctx, argument):
		if not argument.isdigit():
			raise commands.BadArgument('Not a valid user ID.')
		try:
			return await ctx.bot.fetch_user(argument)
		except discord.NotFound:
			raise commands.BadArgument('User not found.') from None
		except discord.HTTPException:
			raise commands.BadArgument('An error occurred while fetching the user.') from None
	

class botcmnds(commands.Cog):
	def __init__(self,bot):
		self.bot = bot	
	
	
	
	
	@commands.command(pass_context= True)
	async def av(self,ctx, *, user: Union[discord.Member, FetchedUser] = None):
		embed = discord.Embed()
		user = user or ctx.author
		avatar = user.avatar_url_as(static_format='png')
		embed.set_author(name=str(user), url=avatar)
		embed.set_image(url=avatar)
		await ctx.send(embed=embed)
        
    
    
            	
def setup(bot):
	bot.add_cog(botcmnds(bot))
                    
