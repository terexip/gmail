import logging  # يجب أن تستورد مكتبة logging

logging.basicConfig(
    level=logging.INFO,  # استخدم logging بدلاً من logger هنا
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        logging.FileHandler("log.txt"),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:  # استخدم logging هنا أيضاً
    return logging.getLogger(name)
