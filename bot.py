from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    # Ignore messages sent by bots (including our own bot)
    if message.author.bot:
        return

    # Check if the message contains "https://x.com/"
    if "https://x.com" in message.content:
        # Replace "https://x.com/" with a new url in the message content
        new_url = os.getenv("NEW_URL")
        fixed_message = message.content.replace("https://x.com/",new_url)
        await message.channel.send(f"{message.author.mention} {fixed_message}")
        # Delete the original message
        try:
            await message.delete()
        except discord.Forbidden:
            print("No permission to delete message")
        except discord.HTTPException as e:
            print(f"Can't delete message: {e}")
    
    # Ensure that commands are still processed if any are defined
    await bot.process_commands(message)

# Start the bot (insert your bot token)
bot_token = os.getenv("BOT_TOKEN")
bot.run(bot_token)
