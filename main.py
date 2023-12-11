import discord
from discord.ext import commands
from APIKeys import *

intents = discord.Intents.all()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# CONST name for category and voice channel.
VOICE_CHAT = 'Voice Chat'  # Category
CREATE_A_VOICE_CHANNEL = 'Create a voice channel'  # Voice channel


# function that creates the category and voice channel needed for that script to work.
async def initialize_voice_channel(guild):
    category = discord.utils.get(guild.categories, name=VOICE_CHAT)
    voice_channel = discord.utils.get(guild.voice_channels, name=CREATE_A_VOICE_CHANNEL)

    # If there's no category matching 'Voice Chat', create it.
    if category is None:
        await guild.create_category_channel(VOICE_CHAT, position=1)

    # If there's no voice channel matching 'Create a voice channel' in 'Voice Chat', create it.
    if voice_channel is None:
        await guild.create_voice_channel(CREATE_A_VOICE_CHANNEL, category=discord.utils.get(guild.categories, name=VOICE_CHAT))  # Create that channel


@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")


@bot.event
async def on_guild_join(guild):
    await initialize_voice_channel(guild)


@bot.event
async def on_voice_state_update(member, before, after):
    guild = member.guild

    # If the user does not have a nickname in the server it will take the global name.
    if member.nick is None:
        member_name = member.global_name
    else:
        member_name = member.nick

    # If someone go in 'Create a voice channel', it creates a channel for that person and move him to his new channel.
    if after.channel and after.channel == discord.utils.get(guild.voice_channels, name=CREATE_A_VOICE_CHANNEL):
        new_channel = await guild.create_voice_channel(f'{member_name}\'s Channel', category=discord.utils.get(guild.categories, name=VOICE_CHAT))
        await member.move_to(new_channel)

    # If a voice channel is empty in 'Voice Chat' and it's not 'Create a voice channel', delete it.
    elif before.channel and before.channel.category == discord.utils.get(guild.categories, name=VOICE_CHAT) and not before.channel.members and before.channel != discord.utils.get(guild.voice_channels, name=CREATE_A_VOICE_CHANNEL):
        await before.channel.delete()


bot.run(discord_token)
