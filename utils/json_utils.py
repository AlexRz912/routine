import json

def json_action(filename: str, opening_mode: str, content: dict) -> any:
    if is_reading_mode(content):
        return json.load(filename)
    else:
        json.dump(content, filename, indent=4, ensure_ascii=False)
        return None

def is_reading_mode(data: str) -> bool:
    return data == None