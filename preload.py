import sys
import re
import logging

import logging_wrapper
from logging_filter import LoggingFilter


def should_filter_trace(co_filename):
    for pattern in [
        "<frozen importlib._bootstrap",
        "Program Files",
        "PythonSoftwareFoundation",
        "logging_filter",
        "logging_wrapper",
    ]:
        if pattern in co_filename:
            return True

    return False


def implement(function_pattern):
    def trace(frame, event, arg):
        if event == "call":
            if should_filter_trace(frame.f_code.co_filename):
                return

            function_name = frame.f_code.co_name
            if not function_name or function_name == "<module>":
                return

            if re.match(function_pattern, function_name):
                try:
                    parameter_message = (
                        f"with parameters {frame.f_locals}" if frame.f_locals else ""
                    )
                except AttributeError as e:
                    print(function_name)
                    exit()

                print(f"{function_name} was called {parameter_message}")

    sys.settrace(trace)
    logging_wrapper.wrap_logging((LoggingFilter(function_patterns=[function_pattern]),))
