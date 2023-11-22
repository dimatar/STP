from loguru import logger

logger.add(
    "logs.ndjson",
    format="{time} {level} {message}",
    level="INFO",
    serialize=True
)

__all__ = ['logger']
