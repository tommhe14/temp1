import discord
from discord.ext import commands
import random

class helpp(commands.Cog):
	def __init__(self,bot):
		self.bot = bot
		
	@commands.command(pass_context= True)
	async def help(self,ctx):
		embed = discord.Embed(title = "*coded by tommhe#1886*", color=0xe91e63)
		embed.add_field(name= "!match",value= "Get Live Stream Links To a Match. ``!match`` > team 1 > team 2 ",inline=True)
		embed.add_field(name= "!names",value= "List Of All Games Available",inline=True)
		embed.add_field(name= "!inviteme",value= "Discord Bot Invite Link",inline=True)
		embed.add_field(name= "!membercount / !mc",value= "Amount Of Members In Your Server",inline=True)
		embed.add_field(name= "!say",value= "Make Me Say Some Dumb Shit. Example: !say {your message}",inline=True)
		embed.add_field(name= "!penroulette",value= "Test Your Chances At a Penalty, Are You The Next Penalty King?",inline=True)
		embed.add_field(name= "!ask",value= "Ask Me a Question, But You May Not Like The Answer ;)",inline=True)
		embed.add_field(name= "Stream Central",value= "[Join Our Main Server!](https://discord.gg/CPDZjMp)",inline=True)
		await ctx.send(embed=embed)
		await ctx.message.delete()

	@commands.command(pass_context= True)
	async def soccerstreams(self,ctx):
		await ctx.send(f"(https://soccerstreams-100.com/)")
		await ctx.message.delete()

	@commands.command(pass_context= True)
	async def inviteme(self,ctx):
		await ctx.send(f"https://discord.com/api/oauth2/authorize?client_id=594663400143847424&permissions=26688&scope=bot")
		await ctx.message.delete()

	@commands.command(pass_context= True)
	async def say(self,ctx,*,arg):
		await ctx.send(f"{arg}")
		await ctx.message.delete()

	@commands.command(pass_context=True)
	async def serverslist(self,ctx):
		for guild in self.bot.guilds:
        		await ctx.send(f"``Server Name: {guild.name}``,``Users: {guild.member_count} ``,``Owner: {guild.owner}``")
	
	@commands.command(pass_context= True)
	async def penroulette(self,ctx):
    		variable = [
        		"**What a finish! made the keeper dive the wrong way like a mug!**",
        		"**GOAL! keeper gets a hand to it but it's not enough to stop that rocket!**",
			"**SAVED! You smashed it top bins but the cat makes a heroic save from  out of no where!**",
			"**Tidy finish! keeper had no chance**",
			"**20 yard run up and you still missed it, what a disgrace**",
			"**What was that?! straight at the keeper, he didnt even need to move**",
			"**GOAL! Clean panenka, Pirlo would be proud!**",
			"**MISS! he skies it row Z. Lent back further than matrix. Schoolboy Error**",
			"**You step up..... AND SMASH IT HOME! WHAT A NET RIPPER!**",
			"**MISS! A great attempt, but it hits the post and out, you must be gutted!**",
			"**MISS! Keeper saves it and now is celebrating, wait, WAIT, THE BALL IS CURLING BACK IN, THE KEEPER HASN'T REALISED. ITS A GOAL! WHAT HAVE WE JUST WITNESSED!**",
            "**Calm run up, Keeper points right, and you slot it home left. simiple, sadistic striking.**",
            "**ooo, good finish, keeper went the right way, but not far enough, good penalty son.**",
            "**keepers digging his studs into the penalty spot for this one, not sure he can do that. slow run up.... AND YOU'VE SLIPPED! ROW Z! HEAD IN YOUR HANDS! YOU'VE LET THE TEAM DOWN THERE**",
            "**GOAL!!! no messing, quick run up and to poked home.**"]
    		await ctx.send("{}".format(random.choice(variable)))

	@commands.command(pass_context= True)
	async def mc(self, ctx):
    		guild = ctx.message.guild
    		embed = discord.Embed(title=guild.name, description='', color=0x240D57)
    		embed.add_field(name='Members', value=str(len(guild.members)), inline=True)	
    		await ctx.send(embed=embed)
	
	@commands.command(pass_context= True)
	async def membercount(self, ctx):
    		guild = ctx.message.guild
    		embed = discord.Embed(title=guild.name, description='', color=0x240D57)
    		embed.add_field(name='Members', value=str(len(guild.members)), inline=True)	
    		await ctx.send(embed=embed)

	@commands.command(pass_context= True)
	async def ask(self, ctx):
    		variable = [
        		"yeah haha",
        		"ofc u dumb bitch",
			"i'd say so yeah",
			"absofuckinlutely",
			"i dont fucking know do i!?",
			"dont bet on it pal",
			"i reckon",
			"probs",
			"defo not",
			"<@552583557277679617> says na",
			"you already know the answer mert",
			"heeeeell na",
			"wait what was that? cannae fucking hear u mate",
			"i hate to be the one to tell you....",
            "stupid question, ask me later -_-",
            "can't believe you just asked me that, the nerve...",
            "dont care",
            "if god was real, he would say yes. but he aint so no lmao",
            "i'll go ask your mum, one minute...",
            "to save you from tears, i wont answer that one ;)",
            "https://youtu.be/cMTAUr3Nm6I?t=95",
            "if i say yes, will you stop asking me?",
            "https://cdn.discordapp.com/attachments/684746247202275331/727680095858327624/wBhyhNdtK1C4gAAAABJRU5ErkJggg.png"]
    		await ctx.send("``Answer:`` {}".format(random.choice(variable)))

	@commands.command(pass_context= True)
	async def mc(self, ctx):
    		guild = ctx.message.guild
    		embed = discord.Embed(title=guild.name, description='', color=0x240D57)
    		embed.add_field(name='Members', value=str(len(guild.members)), inline=True)	
    		await ctx.send(embed=embed)
	
	@commands.command(pass_context= True)
	async def membercount(self, ctx):
    		guild = ctx.message.guild
    		embed = discord.Embed(title=guild.name, description='', color=0x240D57)
    		embed.add_field(name='Members', value=str(len(guild.members)), inline=True)	
    		await ctx.send(embed=embed)


def setup(bot):
        bot.add_cog(helpp(bot))