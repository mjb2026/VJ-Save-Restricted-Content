import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22515395"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3f142c912294aff53b346ab9fd054d4f")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "692943115"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mayurpawar715390:zCUEmOkLXBI9KK3V@cluster0.jasb6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
