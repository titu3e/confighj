# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open("{}/Lumine/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 8626831  # integer value, dont use ""
    API_HASH = "db23330a6edf4a517ee186b35cedec71"
    TOKEN = "2129805348:AAEK4sMxaDQfJA5ntFzrsXfxP-uBa9ZKnTU"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1593338093  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "Sungjinwooarc"
    SUPPORT_CHAT = "LumineBotSupport"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1234567890123
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1234567890123
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    ALLOW_CHATS = True

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://aysiasgk:smaU-XqJVmaNnKh9JjlVVjF_92XUMXJa@john.db.elephantsql.com/aysiasgk"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "Xwk6NIJa_StwddnrYJnS0SVA~R~DFvdZJZol_Co_gkR8dNTutMWY75FyU7qg9qG0"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"
    WEATHER_API = ""  # go to openweathermap.org/api to get key
    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    SUDO_USERS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    SUPPORT_USERS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_USERS = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        4  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = "CAACAgIAAxkBAAEDZQ5hpwzzErrjMP2xB-kItRCjZKFesAACVAUAAmX_kgpL3GlC0wLhOSIE"  # banhammer marie sticker id, the bot will send this sticker before banni>    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "NEWU89LO9Y5169RI"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "8RLOW7FIQ5BV"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        None  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = None  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = None  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True