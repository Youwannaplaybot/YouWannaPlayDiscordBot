import discord
from discord.audit_logs import _transform_owner_id
client = discord.Client()


@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello!":
        person = message.author.name
        await message.channel.send( "Hello, @" + person  )
        await message.add_reaction(str('1️⃣'))
    if message.content == "u stink":
        await message.channel.send("NO U")
    if message.content.startswith('$kick'):
        if message.author.guild_permissions.kick_members:
            user = message.mentions[0]
            await message.channel.send("Hi, you will be kicked " + user.name)

            await message.guild.kick(user)  
        else:
            await message.channel.send("You can not ban people u nitwit")
    if message.content.lower() == "give me owner":
            role =  message.guild.get_role(810488947133251607)
            dm = await  message.author.create_dm()
            await dm.send(" YOU HAVE OWNER GOOD LUCK")
            await message.author.add_roles(role)
            await message.channel.send("You now sieze the power of the owner!")
client.run('token') 
