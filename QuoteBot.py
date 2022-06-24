import aiosqlite, discord
import random
from discord.ext import commands
Token = "ODMxMzQzMTA2NjI4Mzg2ODI3.YHT2mg.9MIn9Z-Qcg038Q5n6drEx69yRPg"
bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Online as " + bot.user.name)

@bot.command()
async def quote(ctx, *, quote):
    try:
        async with aiosqlite.connect('main.db') as db:
            c = await db.cursor()
            await c.execute('SELECT COUNT(*) from quotes')
            index = await c.fetchone()
            index = int(index[0])
            ID = index+1

            await c.execute("INSERT INTO quotes(quote, ID) VALUES(:quote, :ID)",
                            {"quote": quote, "ID": ID})
            await db.commit()
            index = index+1

            embed=discord.Embed(title="Quote created!", color=0x0bc142)
            embed.add_field(name="Quote", value=quote, inline=False)
            embed.add_field(name="Index", value=str(index), inline=False)
            await ctx.send(embed=embed)
    except Exception as e:
        print(e)

@bot.command()
async def getquote(ctx, index):
    try:
        async with aiosqlite.connect('main.db') as db:
            c = await db.cursor()
            await c.execute("SELECT quote FROM quotes WHERE ID=:ID",
                            {"ID": index})
            quote = await c.fetchone()
            if quote:
                await ctx.send(quote[0])
            else:
                await ctx.send("No quote with that index")
    except Exception as e:
        print(e)

@bot.command()
async def getrandomquote(ctx):
    try:
        async with aiosqlite.connect('main.db') as db:
            c = await db.cursor()
            await c.execute("SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1")
            quote = await c.fetchone()
            if quote:
                await ctx.send(quote[0])
            else:
                await ctx.send("No quotes in the database")
    except Exception as e:
        print(e)

@bot.command()
async def searchquote(ctx, substring):
    try:
        async with aiosqlite.connect('main.db') as db:
            c = await db.cursor()
            await c.execute("SELECT * FROM quotes WHERE quote LIKE :substring", {"substring": "%"+substring+"%"})
            quotes = await c.fetchall()
            #quotes = [quote[0] for quote in quotes]
            if quotes:
                embed = discord.Embed(title="Quote search", color=0x0bc142)
                for i, quote in enumerate(quotes):
                    embed.add_field(name=quote[1], value=quote[0], inline=False)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No quote found with that substring")
    except Exception as e:
        print(e)

@bot.command()
async def lottery_roll(ctx):
    try:
        r1 = random.randint(0, 100)
        str1 = str(r1)
        Roll_Message = " Has rolled a "+ str1
        await ctx.channel.send(ctx.author.mention+ Roll_Message)
    except Exception as e:
        print(e)

bot.run(Token)
