import sys
import re
import pathlib
import threading
import pprint

from efocus import wrapper
from efocus.logging_filter import LoggingFilter
from efocus.logger import LOGGER


def should_filter_trace(frame):
    if frame.f_code.co_name.startswith("<"):
        return True

    try:
        trace_file_path = pathlib.Path(frame.f_code.co_filename)
    except TypeError:
        return True

    if pathlib.Path(".").absolute() not in trace_file_path.absolute().parents:
        return True

    for pattern in [
        "<frozen importlib._bootstrap_external>",
        "<frozen importlib._bootstrap>",
    ]:
        if pattern in frame.f_code.co_filename:
            return True

    return False


def run(function_pattern, log_enter):
    if log_enter:
        _trace_invocation(function_pattern)

    wrapper.wrap_logging((LoggingFilter(function_patterns=[function_pattern]),))


def _create_invocation_message(frame):
    message = "\n" + "." * 100 + "\n"
    message += f"'{frame.f_code.co_name}' was invoked by '{frame.f_back.f_code.co_name}':\n"
    if frame.f_locals:
        message += pprint.pformat(frame.f_locals, indent=4) + "\n"

    message += "." * 100
    return message


def _trace_invocation(function_pattern):
    def trace(frame, event, arg):
        if event == "call":
            if should_filter_trace(frame):
                return

            if re.match(function_pattern, frame.f_code.co_name):
                message = _create_invocation_message(frame)
                LOGGER.info(message)

    sys.settrace(trace)
    threading.settrace(trace)
