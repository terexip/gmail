import logger

logging.basicConfig(
    level=logger.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logger.getLogger("httpx").setLevel(logger.ERROR)
logger.getLogger("pyrogram").setLevel(logger.ERROR)
logger.getLogger("pytgcalls").setLevel(logger.ERROR)


def LOGGER(name: str) -> logger.Logger:
    return logger.getLogger(name)
