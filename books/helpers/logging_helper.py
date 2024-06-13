import logging

logger = logging.getLogger(__name__)
logger_debug = logging.basicConfig(
    filename="backend-log.log", filemode="a", encoding="utf-8", level=logging.DEBUG
)
