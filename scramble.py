import discord
from discord import app_commands

from dotenv import load_dotenv
from pathlib import Path
import os
import random

# ----------- Load secrets file -----------
load_dotenv(dotenv_path=Path('.env'))
BOT_TOKEN = os.getenv('BOT_TOKEN')

# ----------- Boilerplate ------------
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ----------- Client events -----------
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await tree.sync()
    print("Ready!")

# ----------- Dropdown/View Objects ------------
class ChannelDropdown(discord.ui.Select):
    def __init__(self, option_names):
        if len(option_names) == 0:
            option_names.append("There are no voice channels available")

        options = [discord.SelectOption(label=name) for name in option_names]

        super().__init__(placeholder='Select voice channel', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        channel_name = self.values[0]

        voice_channel = discord.utils.get(interaction.guild.channels, name=channel_name)

        if (voice_channel == None):
            await interaction.response.send_message("Channel " + channel_name + " does not exist.")
            return

        if len(voice_channel.members) == 0:
            await interaction.response.send_message("There are no users in " + channel_name + ".")
            return

        display_names = [member.display_name for member in voice_channel.members]
    
        random.shuffle(display_names)

        result = ""
        for i in range(len(display_names)):
            result += str(i+1) + ". " + display_names[i] + "\n"

        await interaction.response.send_message(result)

class ChannelDropdownView(discord.ui.View):
    def __init__(self, option_names):
        super().__init__()
        self.add_item(ChannelDropdown(option_names))

# ----------- Bot commands -----------
@tree.command(name = "scramble", description = "Produces a random presentation order for given voice channel")
async def first_command(interaction: discord.interactions.Interaction):
    view = ChannelDropdownView([channel.name for channel in interaction.guild.voice_channels if channel is not interaction.guild.afk_channel])
    await interaction.response.send_message("Select voice channel to scramble: ", view=view)

# ----------- Launch the bot -----------
client.run(BOT_TOKEN)