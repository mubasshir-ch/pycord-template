Default pycord template I use for my bots
=========================================

Create the bot
--------------

- `Create new bot <https://discord.com/developers/applications>`_
- Got to ``Bot`` and click Reset Token and Copy the bot token.
- Turn on all the privilaged intents. (If you don't want to use all intents, modify the code accordingly)
- Go to ``Oauth2 -> URL Generator``, select ``bot`` and ``application.commands``, select required permission and copy the generated url to invite the bot.

Using this template
-------------------

- Remove the ``.git`` folder (view hidden files if you don't see it) and connect to new repository
- Create .env file for ``BOT_TOKEN``, ``MONGODB_URI`` and other sensetive apis
- Create ``.debug_config.json`` for development mode configuration(same format as ``config.json``)
- Install the requirements ``pip install -r requirements.txt`` or ``pip3 install -r requirements.txt`` in linux.

Running the bot
---------------
- Run ``python main.py`` or ``python3 main.py`` in linux.
- To keep it running in background, use ``nohup python3 -u main.py > stdout.log &`` in linux.

Useful links
------------
- `Pycord Documentation <https://docs.pycord.dev/en/master/index.html>`_
- `Pycord Github <https://github.com/Pycord-Development/pycord/>`_
- `Pycord Examples <https://github.com/Pycord-Development/pycord/tree/master/examples>`_
- `Discord Developer Portal <https://discord.com/developers/applications>`_
- `Discord Developer Portal Docs <https://discord.com/developers/docs/intro>`_
