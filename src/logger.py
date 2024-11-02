import logging


class LoggerBase:
    logger_name: str
    logger: logging.Logger

    def get_logger(self):
        return self.logger

    def info(self, message: str, stack_level: int = 0):
        self.logger.info(message, stacklevel=2 + stack_level)

class ServingLogger(LoggerBase):
    logger_name = (
        f"KOPIS"
    )
    logger = logging.getLogger(logger_name)

    def get_logger(self):
        return self.logger

    def info(self, message: str, stack_level: int = 0):
        self.logger.info(message, stacklevel=2 + stack_level)