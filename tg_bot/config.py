from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 843714186  # my telegram ID
    OWNER_USERNAME = "Zainstech"  # my telegram username
    API_KEY = "956165209:AAE44fhRsNKsLFJpt5sxN8Yafh1jXJgARjU"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-374422454' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [843714186]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
