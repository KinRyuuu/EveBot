from helpers import commandHelpers
import commandRegistry
import re

class EveBot:
    
    #React to things people say (not commands)
    async def doReacts(self, allReactions, message, metadata, sendReply):
        for reaction in allReactions:
            if(reaction in message.lower()):
                #calls the reaction function with the only argument being the message that triggered the reaction
                return await allReactions[reaction]([reaction, [message]], metadata, sendReply)
            else:
                regmatch = re.findall(reaction, message, re.IGNORECASE)

                if(regmatch):
                    return await allReactions[reaction]([reaction, [message]], metadata, sendReply)

    async def read(self, message, metadata, sendReply):
        allCommands = commandRegistry.commandsDict
        allReactions = commandRegistry.reactionsDict
        
        if(metadata.get("user").id != self.user.id):
            # If this message is a command, read it
            if(commandHelpers.is_command(message)):
                command = commandHelpers.get_command(message)
                
                try:
                    return await allCommands[command[0]](command, metadata, sendReply)
                except KeyError as err:
                    print("Couldn't find command " + str(err))
            
            # Scan message looking for content to react to
            return await self.doReacts(allReactions, message, metadata, sendReply)

    
    def __init__(self, thisUser):
        self.user = thisUser
