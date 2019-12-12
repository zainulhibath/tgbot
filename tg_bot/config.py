if not __name__.endswith("sample_config"):	import datetime
    import sys	import importlib
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "	import re
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)	from typing import Optional, List
    quit(1)	

from telegram import Message, Chat, Update, Bot, User

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
# Create a new config.py file in same dir and import, then extend this class.	from telegram.error import Unauthorized, BadRequest, TimedOut, NetworkError, ChatMigrated, TelegramError
class Config(object):	from telegram.ext import CommandHandler, Filters, MessageHandler, CallbackQueryHandler
    LOGGER = True	from telegram.ext.dispatcher import run_async, DispatcherHandlerStop, Dispatcher

from telegram.utils.helpers import escape_markdown
    # REQUIRED	
    API_KEY = "928406379:AAF8zPqOyRRlAITbt4Tm2xADQHra5h6XO1c"	from tg_bot import dispatcher, updater, TOKEN, WEBHOOK, OWNER_ID, DONATION_LINK, CERT_PATH, PORT, URL, LOGGER, \
    OWNER_ID = "843714186"  # If you dont know, run the bot and do /id in your private chat with it	    ALLOW_EXCL
    OWNER_USERNAME = "Zainstech"	# needed to dynamically load modules

# NOTE: Module order is not guaranteed, specify that in the config file!
    # RECOMMENDED	from tg_bot.modules import ALL_MODULES
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules	from tg_bot.modules.helper_funcs.chat_status import is_user_admin
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist	from tg_bot.modules.helper_funcs.misc import paginate_modules
    LOAD = []	
    # sed has been disabled after the discovery that certain long-running sed commands maxed out cpu usage	PM_START_TEXT = """
    # and killed the bot. Be careful re-enabling it!	Hi {}, my name is {}! If you have any questions on how to use me, read /help - and then head to @MarieSupport.
    NO_LOAD = ['translation', 'rss', 'sed']	
    WEBHOOK = False	I'm a group manager bot built in python3, using the python-telegram-bot library, and am fully opensource; \
    URL = None	you can find what makes me tick [here](github.com/zainulhibath/tgbot)!

    # OPTIONAL	My owner is @ZainsTech
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.	
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.	Feel free to submit pull requests on github, or to contact my support group, @MarieSupport, with any bugs, questions \
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.	or feature requests you might have :)
    DONATION_LINK = None  # EG, paypal	I also have a news channel, @MarieNews for announcements on new features, downtime, etc.
    CERT_PATH = None	
    PORT = 5000	You can find the list of available commands with /help.
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands	
    STRICT_GBAN = False	Please Join official movies channel of our admin @Movies_Tech
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!	
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker	if you have a channel with more than 500 subscribers you can earn with that channel by registering it to @Tech_ads_bot
    ALLOW_EXCL = False  # Allow ! commands as well as /	

If you're enjoying using me, and/or would like to help me survive in the wild, hit /donate to help fund/upgrade my VPS!

"""
class Production(Config):	
    LOGGER = False	HELP_STRINGS = """

Hey there! My name is *{}*.

I'm a modular group management bot with a few fun extras! Have a look at the following for an idea of some of \
class Development(Config):	the things I can help you with.
    LOGGER = True
