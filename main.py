import discord
from discord.ext import commands
from random import randint
from dotenv import load_dotenv
import os


load_dotenv()

token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")

intents = discord.Intents.all()

bot = commands.Bot(prefix, intents=intents)

initial_extensions = ["Cogs.help", "Cogs.ping"]

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")


@bot.event
async def on_ready():
    print("")
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"
        )
    )
    print(f"We have used version {discord.__version__}")

@bot.command()
async def info(ctx: commands.Context):
    await ctx.send(f"¡Hola mi nombre es {bot.user.name}!")


@bot.command()
async def embed(
    ctx: commands.Context
):
    
    #Test values
    name: str = "el comienzo de una aventura".capitalize()
    description: str = "Esta es la descripción de la misión."
    experience_reward: int = 100
    gold_reward: int = 100
    teacher: str = str(ctx.author)
    #Test values
    
    embed = discord.Embed(
        title=f'{teacher.capitalize()} has created: "{name}"',
        description=description,
        color=discord.Color.green(),
        )
    
    embed.add_field(name="Recompensa de experiencia", value=experience_reward)
    embed.add_field(name="Recompensa de oro", value=gold_reward)
    embed.set_footer(text=f"Publicado por {teacher}")
    
    await ctx.send(embed=embed)
    
bot.run(token)
