import os

from utils import json_utils
from logs  import logs

def parse(filename, mode, content):
    try:
        with open(filename, mode, encoding="utf-8") as f:
            return json_utils.json_action(f, mode, content)

    except FileNotFoundError:
        logs.not_found_error(filename)
        
    except Exception as e:
        logs.unexpected_error_onload(filename, e)