import discord
import random
from discord.ext import commands
from colorama import init
init()
from colorama import Fore, Back, Style
import music



#prefix and music connect
intents = discord.Intents.default()
print ( Fore.YELLOW )
cogs = [ music ]
client = commands.Bot( command_prefix = commands.when_mentioned_or( '>' ) )
for i in range( len( cogs ) ):
	cogs[ i ].setup( client )
client.remove_command( 'help' )


#activate	
print ( 'Activation...' )
@client.event
async def on_ready():

	await client.change_presence( status = discord.Status.online, activity = discord.Game( '>help' ) )

	print( 'Activation was successful' )
	print( '-----------------------------------------' )



#info command
@client.command( pass_context = True )
async def help( ctx ):
		
	embed = discord.Embed( title = "Информация о командах BARBARIKI БОТ", description ="    ", color = 0x000000 )
	embed.add_field( name = ">help", value = "Просмотр списка команд", inline = False )
	embed.add_field( name = ">report (user) (reason)", value = "Отправить жалобу администрации сервера", inline = False )
		
	await ctx.send( embed = embed )


#cuddle command
@client.command( pass_context = True )
async def cud( ctx , member: discord.Member ):

	await ctx.send( f'{ ctx.message.author.name } обнял(а) { member.mention }! :relaxed:' )
@client.command( pass_context = True )
async def cuddle( ctx ):

	await ctx.send( f'{ ctx.message.author.name } обнял(а) всех! :relaxed:' )


#kick command
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def kick( ctx, member: discord.Member, *, reason = None ):
		
	await member.kick( reason = reason )
		
	await ctx.send( f'{ member.mention } исключён с сервера!' )

	print ( Fore.RED )
	print( f'{ member.name } kicked from the server' )
	print ( Fore.YELLOW )
	print( '***' )
		
		
#ban command
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )
async def ban( ctx, member: discord.Member, *, reason = None ):
		
	await member.ban( reason = reason )
		
	await ctx.send( f'{ member.mention } заблокирован на сервере!' )

	print ( Fore.RED )
	print( f'{ member.name } banned on the server' )
	print ( Fore.YELLOW )
	print( '***' )
		
		
#report command
@client.command( pass_context = True )
async def report( ctx, member: discord.Member, *, reason = None ):
		
	await ctx.send( f'Отправлена жалоба на { member.mention }!' )

	await ctx.author.send( 
		f'Вы отправили жалобу на пользователя { member.mention } по причине "' + reason + '". Жалоба будет рассмотрена администрацией. Вскоре с вами свяжется один из администраторов!' )
		
	print ( Fore.BLUE )
	print( f'Received a complaint against the user { member.name } for the reason "' + reason + '"' )
	print ( Fore.YELLOW )
	print( '***' )



#errors
@ban.error
async def ban_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( 'У вас недостаточно прав на эту команду!' )
@kick.error
async def kick_error( ctx, error ):
	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( 'У вас недостаточно прав на эту команду!' )


	
#run
TOKEN = open( 'token.txt', 'r' )
client.run( *TOKEN )