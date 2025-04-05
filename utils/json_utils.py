import re
import json

def json_action(filename: str, opening_mode: str, content: dict) -> any:
    if is_reading_mode(content):
        return json.load(filename)
    else:
        json.dump(content, filename, indent=4, ensure_ascii=False)
        return None

def is_reading_mode(data: str) -> bool:
    return data == None

def get_history(file):
    history_data = file.read().decode("latin-1")
    history_lines = history_data.split("\n")
    clean_lines = [re.sub(r"^.*?;", "", line) for line in history_lines]
    return "\n".join(clean_lines[-20:]).strip()
    