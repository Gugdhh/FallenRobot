class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20256702
    API_HASH = "c81d1c06212c1c9624f44e159c651a5c"

    CASH_API_KEY = "6TTOZ2XM4I1MUZHQ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://lzsdumzs:hVxl2M4cZyLocKG4CUSGtuUqED44MZRw@tiny.db.elephantsql.com/lzsdumzs"  # A sql database url from elephantsql.com

    EVENT_LOGS = (5673255098)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb://ud7kcz6totsvepy86bb2:d4gmTfoBbpzDmNLzItwG@n1-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017,n2-c2-mongodb-clevercloud-customers.services.clever-cloud.com:27017/b0ojwj6pcvvj30u?replicaSet=rs0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/d39e96c34b7871a8dd0f9.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5775428780:AAFUhpHCqSj2CVr4fghHM80iW3Kq-fTP-L8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "http://api.timezonedb.com/v2.1/list-time-zone"  # Get this value from https://timezonedb.com/api

    OWNER_ID =  5868178288 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "/"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
