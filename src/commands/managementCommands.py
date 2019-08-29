import commandRegistry
import asyncio
import config
import logging
from models import TagReactables

logger = logging.getLogger(__name__)

# Only log debug messages in debug mode
if (config.DEBUG):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

commands = {}
command = commandRegistry.command
reaction = commandRegistry.reaction
restrictions = commandRegistry.restrictions
help_text = commandRegistry.help_text
tag_reactables = commandRegistry.tag_reactables

@help_text("Ping")
@command("ping")
async def ping(command, metadata, sendReply):
    return await sendReply("Pong")


@restrictions(371995067386429442)
@help_text("Vet a member for the server. \n\
           approve: vote to approve the member (requires at least two approvals).\n\
           deny: vote to deny the member (only one deny required, but if a deny occurs \
           after an approve one vetter must change their vote in order to approve or deny)\n\
           respond <message>: send a PM to the member in question.")
@command("vet")
async def vet(command, metadata, sendReply):
    if(command[1][0] == "approve"):
        pass
    elif(command[1][0] == "deny"):
        pass
    elif(command[1][0] == "respond"):
        pass

@restrictions(config.servers.get("TMHC"), config.servers.get("Test"))
@command("addrolereactable")
@help_text("Allow reactions on a message to assign a role. Usage: 'addrolereactable <messageid> <roleid>' in the channel containing the message.")
async def addrolereactable(command, metadata, sendReply):
    if(len(command[1]) < 2):
        return await sendReply("Please specify a messageid and roleid")
    
    messageid = command[1][0]
    roleid = command[1][1]
    guild = metadata.get("client").get_guild(metadata.get("server").id)
    role = guild.get_role(int(roleid)) 
    
    if(role is None):
        return await sendReply("No role with that id was found")

    try:
        message = await metadata["message"].channel.fetch_message(messageid)
    except Exception as e:
        logger.exception(e)
        return await sendReply("No message with that id was found")
   
    emoji = "🔼"
    await message.add_reaction(emoji)

    session = metadata["session"]
    instance = session.query(TagReactables).filter_by(message_id=message.id).first()
    if(instance):
        instance.function_name="toggle_role"
        instance.function_args=roleid
    else:
        instance = TagReactables(message_id=message.id, function_name="toggle_role", function_args=roleid)
    session.add(instance)

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error("Unable to commit to database: " + e)

    return await sendReply("Added role react for "+role.name)

@restrictions(config.servers.get("TMHC"), config.servers.get("Test"))
@tag_reactables()
async def accept_coc(args, event_type, metadata):
    if(event_type != "REACTION_ADD"):
        return
    
    roles = []
    guild = metadata.get("client").get_guild(metadata.get("server").id)

    for role in config.coc_roles[metadata.get("server").id]:
        roles.append(guild.get_role(role))

    try:
        userid = metadata.get("user").id
        await guild.get_member(userid).add_roles(*roles)
    except Exception as e:
        logger.exception(e)


@restrictions(config.servers.get("TMHC"), config.servers.get("Test"))
@tag_reactables()
async def toggle_role(args, event_type, metadata):
    guild = metadata.get("client").get_guild(metadata.get("server").id)
    role = guild.get_role(int(args))
    
    if(event_type == "REACTION_ADD"):    
        try:
            userid = metadata.get("user").id
            await guild.get_member(userid).add_roles(role)
        except Exception as e:
            logger.exception(e)
    elif(event_type == "REACTION_REMOVE"):
        try:
            userid = metadata.get("user").id
            await guild.get_member(userid).remove_roles(role)
        except Exception as e:
            logger.exception(e)


