# داخل strings/filters.py

from pyrogram import filters

def command(command_name: str):
    """
    Decorator to create command filters for the bot.
    Usage: @app.on_message(filters.command("start"))
    """
    def decorator(func):
        async def wrapper(client, message):
            # Check if the command matches
            if message.text and message.text.startswith(f"/{command_name}"):
                return await func(client, message)
        return wrapper
    return decorator
