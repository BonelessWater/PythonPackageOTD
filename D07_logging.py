import logging
from rich.logging import RichHandler

# Configure logging to use RichHandler
logging.basicConfig(
    level=logging.INFO,                   # minimum level
    format="%(message)s",                 # let Rich format the timestamp/level
    datefmt="[%X]",                       # optional: Rich will still show its own timestamp style
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger()

logger.debug("🔍 This DEBUG message won’t show (level is INFO)")
logger.info("ℹ️  This is an info message")
logger.warning("⚠️  This is a warning")
logger.error("❌  This is an error")
logger.critical("💥  Critical failure!")
