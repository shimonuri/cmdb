from typing import List
import traceback


class LoggingFilter:
    def __init__(self, functions: List[str]):
        self.functions = functions
        self.has_astrix = any((function == "*" for function in self.functions))

    def should_filter(self, args, kwargs) -> bool:
        if self.has_astrix:
            return False

        stack = [s.name for s in traceback.extract_stack()]
        for function in self.functions:
            if function in stack:
                return False

        return True
