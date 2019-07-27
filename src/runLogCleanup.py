import datetime
import discord
import apikeys
import logging
import config 
import time

logger = logging.getLogger(__name__)

# Only log debug messages in debug mode
if (config.DEBUG):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

class CleanupClient(discord.Client):
    async def on_ready(self):
        logger.info("Initiating log cleanup.")
        messages = 0
        channel = self.get_channel(config.log_channels.get(354565059675947009))
        if(channel is None):
            logger.error("Unable to find log channel!")
        
        message_list = []

        async for message in channel.history(limit=None):
            if(datetime.datetime.now().timestamp() - message.created_at.timestamp() > 86400):
                message_list.append(message)
                messages += 1

            if len(message_list) == 100:
                try:
                    await self.delete_messages(message_list)
                    time.sleep(1)
                except:
                    for message in message_list:
                        await message.delete()
                        time.sleep(1)

        for message in message_list:
            await message.delete()
            time.sleep(1)

        logger.info(str(messages) + " messages deleted.")
        await self.close()

if(__name__ == "__main__"):
    client = CleanupClient()
    client.run(apikeys.discordkey)
