import pickle
import discord
import wikipedia
import random
intents = discord.Intents.all()

client = discord.Client(intents=intents)

cash = {}
filename = 'cash'
cashfile = open(filename,"r+b")
cash = pickle.load(cashfile)
    
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))
    filename = 'cash'
    cashfile = open(filename,"r+b")
    cash = pickle.load(cashfile)
    

@client.event
async def on_message(message):
    print("Cash is {0}".format(cash) )
    
           
    if message.author == client.user:
        return
    if message.content == "Hello!":
        person = message.author.name
        await message.channel.send( "Hello, @" + person  )
        await message.add_reaction(str('👋'))
    if message.content == "$gimmecash":
        if message.author.name == "WhineyMonkey10":
            cash[message.author.id] = 10584575675389067530986739086
            cash[message.author.id] += 3653546346534634634634789067534890672890678924596758
            await message.channel.send("Lol, ur code works monkey #monkeys for life!")
            filename = 'cash'
            cashfile = open(filename,"w+b")
            pickle.dump(cash, cashfile)
            return
        if not message.author.id in cash:
            cash[message.author.id] = 1
        cash[message.author.id] += 1
        await message.channel.send("You have earned 1 dollar")
        filename = 'cash'
        cashfile = open(filename,"w+b")
        pickle.dump(cash, cashfile)
    if message.content == "$cash":
        if not message.author.id in cash:
            cash[message.author.id] = 1
        embed = discord.Embed(title="Cash Status from YOUWANNAPLAYMINECRAFTBOT", type="rich", description="You have {0} dollars".format(cash[message.author.id]))
        await message.channel.send(embed = embed)
    if message.content.startswith("$peekcash"):
        if not message.mentions[0].id in cash:
            cash[message.mentions[0].id] = 1
        embed = discord.Embed(title="Cash Status from YOUWANNAPLAYMINECRAFTBOT", type="rich", description="He has have {0} dollars".format(cash[message.mentions[0].id]))
        await message.channel.send(embed = embed)
    if message.content == "u stink":
        await message.channel.send("NO U")
    if message.content.startswith('$rob'):
        userToRob = message.mentions[0]
        await message.channel.send("Robbing {0}".format(userToRob.name))
        if not message.author.id in cash:
            cash[message.author.id] = 1
        if not userToRob.id in cash:
            cash[userToRob.id] = 1
        if random.randint(1, 2) == 2 or message.author.name == "jakobdev":
            await message.channel.send("You have succesfully robbed {0} ".format(userToRob.name))
            wonCash = cash[userToRob.id]
            cash[userToRob.id] = 0
            cash[message.author.id] += wonCash
            dm =  await userToRob.create_dm()
            await dm.send("Sorry you have been robbed by {0}".format(message.author.name))
        else:
            await message.channel.send("You have failed in your attempt to rob {0} ".format(userToRob.name))
            wonCash = 0
            cash[userToRob.id] += (cash[message.author.id] )
            cash[message.author.id] = wonCash
            dm =  await userToRob.create_dm()
            await dm.send("Good Luck, the police has stopped the nasty robber {0}".format(message.author.name))

        filename = 'cash'
        cashfile = open(filename,"w+b")
        pickle.dump(cash, cashfile)





    if message.content.startswith('$kick'):
        if message.author.guild_permissions.kick_members:
            user = message.mentions[0]
            await message.channel.send("Hi, you will be kicked " + user.name)

            await message.guild.kick(user)  
        else:
            await message.channel.send("You can not ban people u nitwit stop tying to kick people you evil idiot")
    if message.content.startswith('$ban'):
        if message.author.guild_permissions.kick_members:
            user = message.mentions[0]
            await message.channel.send("Hi, you will be banned " + user.name)

            await message.guild.ban(user)  
        else:
            await message.channel.send("You can not ban people u nitwit")
    if message.content.lower().startswith("$annoy"):
        
        await  message.channel.send("Destorying your friend courtesy of Wikipedia")
        if len(message.role_mentions) != 0:
            print(message.role_mentions[0].members)
            usersInRole = message.role_mentions[0].members
            print(usersInRole)
            for d in range(1,10):
    
                for usera in usersInRole:
                    await message.channel.send("Destroying @" + usera.name + " Courtesy of Wikipedia")
                    dmWithUsera = await usera.create_dm()
                    await message.channel.send("Destorying " + "@" + usera.name)
                    await dmWithUsera.send("Good Luck")
                
                    for i in range(1, 10):
                        await dmWithUsera.send(wikipedia.random())
            return

        user = message.mentions[0]
        if user.name == "WhineyMonkey10" or user.name == "jakobdev":
            await message.channel.send("An error has occurred")
            return
        dmWithUser = await user.create_dm()
        await message.channel.send("Destorying " + "@" + user.name)
        await dmWithUser.send("Good Luck")

        for i in range(1, 40):
            await dmWithUser.send(wikipedia.random())
        


    if message.content.lower() == "give me owner":
            role =  message.guild.get_role(810488947133251607)
            dm = await  message.author.create_dm()
            await dm.send(" Thank you for choosing owner airlines we hope you have a good day!")
            await message.author.add_roles(role)
            await message.channel.send("You now sieze the power of the owner!")
client.run('TOKEN') 











































































moneyformonke = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
