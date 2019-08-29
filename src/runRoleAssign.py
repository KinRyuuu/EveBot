# Assign a role to all members in the discord
# Use when someone fucks the roles again
import datetime
import discord
import apikeys
import logging
import config 
import asyncio

logger = logging.getLogger(__name__)

# Only log debug messages in debug mode
if (config.DEBUG):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

class RoleClient(discord.Client):
    async def on_ready(self):
        logger.info("Initiating role assignment..")
        guild = self.get_guild(config.servers.get("TMHC"))
        role = guild.get_role(config.roles["TMHC"]["Member"])
        badrole = guild.get_role(config.roles["TMHC"]["404"])
        user_count = 0 

        for member in guild.members[700:]:
            try:
                if(badrole not in member.roles):
                    if(role not in member.roles):
                        logger.info("Added role to " + member.name)
                        await member.add_roles(role) 
                        await asyncio.sleep(1)
                        user_count += 1
                else:
                    if(role in member.roles):
                        await member.remove_roles(role)
                        logger.info("Removed role from " + member.name)
                        await asyncio.sleep(1)
            except Exception as e:
                logger.error(e)

        logger.info(str(user_count) + " users updated.")
        await self.close()

if(__name__ == "__main__"):
    client = RoleClient()
    client.run(apikeys.discordkey)
