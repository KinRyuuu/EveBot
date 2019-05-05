import commandRegistry
import asyncio

commands = {}
command = commandRegistry.command
reaction = commandRegistry.reaction
help_text = commandRegistry.help_text

@help_text("Ping")
@command("ping")
async def ping(command, metadata, sendReply):
    return await sendReply("Pong")
