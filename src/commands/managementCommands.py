from helpers import basicResponseHelpers, commandHelpers
import config
import commandRegistry
import os
import re
import asyncio
from models import Service, Server, Chat, User, get_or_create 
from sqlalchemy import func

commands = {}
command = commandRegistry.command
reaction = commandRegistry.reaction
help_text = commandRegistry.help_text

@help_text("Ping")
@command("ping")
async def ping(command, metadata, sendReply):
    return await sendReply("Pong")
