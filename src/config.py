import os, sys

bot_name = "Eve Bot"

# Log channels for servers in the form (guild_id : channel id), one per guild.
# Message edits and deletes for each guild will be posted here.
log_channels = {
    384144475229782037: 574416190802231316, # Test server
    354565059675947009: 604787076021485589  # TMHC
}

# A list of role ids who are approved to use commands, keyed by guild id
approved_roles = {
    384144475229782037: [574564780350636032], # Test server
    354565059675947009: [501445228553699328, 399654133470199820, 354565435514945536] # TMHC
}

# Whether or not to run in debug mode is determined by the presence of an environment variable
DEBUG = os.environ.get('BOT_DEBUG', False) is not False

# If running in debug mode, the bot will be restricted to channel ids in the following array.
debug_channel_ids = [
    384144475670446081, # Test channels
    574416190802231316
]

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
RESPONSE_DIR = os.path.join(ROOT_DIR, "responses")
COMMAND_DIR = os.path.join(ROOT_DIR, "commands")
