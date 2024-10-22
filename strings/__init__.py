import os
from typing import List
import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages[lang]


def get_command(command_name: str, lang: str = "en"):
    """
    Retrieves a command from the language files.
    If the command is not found in the specified language, it falls back to English.
    """
    try:
        return languages[lang][command_name]
    except KeyError:
        return languages["en"].get(command_name, "Unknown command")


for filename in os.listdir(r"./strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./strings/langs/en.yml", encoding="utf8")
        )
        languages_present["en"] = languages["en"]["name"]
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]
    try:
        languages_present[language_name] = languages[language_name]["name"]
    except:
        print("There is some issue with the language file inside bot.")
        exit()
