import logging
import functools
from typing import Collection

from logging_filter import LoggingFilter


def wrap_log(log_func, logging_filters: Collection[LoggingFilter]):
    @functools.wraps(log_func)
    def wrapper(*args, **kwargs):
        for logging_filter in logging_filters:
            if logging_filter.should_filter(args, kwargs):
                return

        log_func(*args, **kwargs)

    return wrapper


def wrap_logging(logging_filters):
    logging.Logger._log = wrap_log(logging.Logger._log, logging_filters=logging_filters)
