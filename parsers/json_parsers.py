from helpers.output_helpers import prompt_clean_zsh_history_output

from utils import json_utils
from logs import logs

class jsonParsers:
    def __init__(self):
        return

    def parse(self, filename, mode, content):
        try:
            with open(filename, mode, encoding="utf-8") as f:
                return json_utils.json_action(f, mode, content)

        except FileNotFoundError:
            logs.not_found_error(filename)

        except Exception as why:
            logs.unexpected_error_onload(filename, why)

    def parse_binary(self, filename, case):
        try:
            with open(filename, "rb") as f:
                if case == "shell":
                    prompt_clean_zsh_history_output(f)
    
        except FileNotFoundError:
            logs.not_found_error(filename)

        except Exception as why:
            logs.unexpected_error_onload(filename, why)