from typing import List
import traceback


class LoggingFilter:
    def __init__(self, functions: List[str]):
        self.functions = functions

    def should_filter(self, args, kwargs) -> bool:
        stack = [s.name for s in traceback.extract_stack()]
        for function in self.functions:
            if function in stack:
                return False

        return True
