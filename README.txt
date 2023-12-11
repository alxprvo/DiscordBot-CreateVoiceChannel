This is a script of a Discord bot that can create a voice channel for someone and delete it when no longer in use.

If you only want to have the bot on your server, you can use the link below to invite my bot that runs on a server 24/7. 
https://discord.com/api/oauth2/authorize?client_id=1148310916438442055&permissions=16777232&scope=bot

The bot only needs permissions to manage channels and move members do not give it more permissions than it needs and DO NOT make it an administrator.

How it works:
-The bot will automatically create a "Voice Chat" category and a "Create a voice channel" voice channel if they do not already exist.
-You can move the "Voice Chat" category anywhere you want in your server.
-If you want to create a voice channel, join "Create a voice channel" and the bot will create your voice channel and move you into it.
-When a voice channel is empty, it will delete it automatically. If the creator of the channel leave but there are still people in it, the channel will stay until the last person leaves.

___________________________

Below are the instructions if you want to create your own bot with my script.

Here are the instructions to create a bot account:
https://discordpy.readthedocs.io/en/stable/discord.html

Reset your bot token, copy it and paste it in APIKeys.py and save it.

Run the main.py script, as long as the script is running the bot will be online.