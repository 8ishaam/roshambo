"""Input handling functions
Small utility module for input reading and validation
"""
import re


def get_input(prompt="", pattern=None):
    """Get input with validation if needed
    :returns result (type: str): the input if matches pattern if any, None if no match
    """
    result = raw_input(prompt)
    if (pattern is not None) and (re.match(pattern, result) is None):
        return None
    return result
