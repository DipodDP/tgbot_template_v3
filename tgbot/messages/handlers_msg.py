from enum import Enum


class AdminHandlerMessages(str, Enum):
    GREETINGS = "Hello, admin! It's template bot.\n Press /stop to stop bot\n"
    STOPPING = 'Stopping bot...'


class UserHandlerMessages(str, Enum):
    GREETINGS = "Hello! It's template bot."
    HELP = "Try some commands from menu"
