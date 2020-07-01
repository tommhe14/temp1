import discord
from discord.ext import commands
from os import listdir
from os.path import isfile
from os.path import isfile, join
import traceback

cogs_dir = "cogs"

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")
@bot.event
async def on_ready():
        await bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(bot.guilds)} Servers"))
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

@bot.event
async def on_command_error(ctx,error):
	if isinstance(error, commands.CheckFailure):
		await ctx.send("You Don\'t have permmisions to do that!")
	
if __name__ == "__main__":
	for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
		try:
			bot.load_extension(cogs_dir + "." + extension)
		except Exception as e:
			print(f'Failed to load extension {extension}.')
			traceback.print_exc()

bot.run('')
