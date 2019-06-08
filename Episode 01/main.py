import discord
from discord.ext import commands


class Client(commands.Bot):
	def __init__(self, command_prefix):
		super().__init__(command_prefix)

	async def on_ready(self):
		print("Bot is ready!")


if __name__ == "__main__":
	client = Client(command_prefix=["!"])
	client.run("TOKEN HERE")