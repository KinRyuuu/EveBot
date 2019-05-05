import os, sys

bot_name = "Eve Bot"
log_channels = {384144475229782037: 574416190802231316}

DEBUG = os.environ.get('BOT_DEBUG', False) is not False
debug_channel_ids = []

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
RESPONSE_DIR = os.path.join(ROOT_DIR, "responses")
COMMAND_DIR = os.path.join(ROOT_DIR, "commands")
