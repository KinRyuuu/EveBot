# Eve Bot 

A bot for managing discord servers.

This bot can handle commands invoked either explicitly (e.g ".help"), or implicitly (in order to respond 
to certain words/phrases used within a message, specific regexes), by means of function decorators.

File Structure within src:
- apikeys.py should be created and filled with a single python variable "discordkey" containing the bot token.
- config.py contains settings including debug settings and log channel definitions
- evebot.py contains core (hypothetically discord-independent) processing code
- runLocal.py allows for testing the bot on the commandline locally (commands only)
- runDiscord.py allows for running the bot on discord, and includes discord-specific functionality for logging message 
  edits and deletes to a channel specified in the config.
- models.py contains database models allowing for future stateful commands to be created (monitoring warns, etc)
- commandRegistry.py handles registering commands, reactions, and help text.
- The commands folder contains files containing bot commands which will be automatically registered and loaded
- the helpers folder contains helpful functions for processing commands/files
- the responses folder can be used to contain text files used to respond to specific commands.

Installation:
- create and activate a new python 3.7 virtualenv using `virtualenv venv && source venv/bin/activate` or similar.
- run `pip install -r requirements.txt` to install dependencies.
- create apikeys.py and add your bot token as a "discordkey" variable
- run `python src/runDiscord.py` to run the bot
