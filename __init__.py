import sys

from .bot import Bot

if sys.version_info < (3, 5):
    raise ImportError("Bot requires Python 3.5+ to support asyncio")