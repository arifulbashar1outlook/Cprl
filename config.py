import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

load_dotenv()


class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = "5459319869:AAFlrfylseUfwTuTwk5dhycP6xyNqz5TEbE"

    # Get these values from my.telegram.org
    API_ID = 17756127
    API_HASH = "8d31d4872622b539217b39bb77ec9615"

    # No need to change
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    ADL_BOT_RQ = {}
    CHUNK_SIZE = 128
    TG_MAX_FILE_SIZE = 4194304000
    HTTP_PROXY = ""
    PROCESS_MAX_TIMEOUT = 3700

    # TG Ids
    LOG_CHANNEL = -1001730056577
    OWNER_ID = 1359572502

    # bot username without @
    BOT_USERNAME = "ColabteleBot"

    # auth users
    AUTH_USERS = [OWNER_ID,]
