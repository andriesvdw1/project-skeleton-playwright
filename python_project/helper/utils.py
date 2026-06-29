import logging
from enum import Enum
import allure

class LogLevel(Enum):
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

def log_message(logger: logging.Logger, message: str, level: LogLevel, attach_to_allure: bool = True):
    # Dynamically resolve the logging level using getattr to keep the code clean
    log_func = getattr(logger, level.value, logger.info)
    log_func(message)

    if attach_to_allure:
        allure.attach(
            message,
            name=f"Log ({level.value.upper()})",
            attachment_type=allure.attachment_type.TEXT
        )

def take_screenshot(page, name: str = "screenshot"):
    try:
        screenshot_data = page.screenshot(type="png")
        allure.attach(
            screenshot_data,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        return screenshot_data
    except Exception as e:
        # It's usually a good idea to log why the screenshot failed
        logging.error(f"Failed to take screenshot: {e}")
        return None