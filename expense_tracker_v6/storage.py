from datetime import datetime
import json
from json import JSONDecodeError

FILE = ".json"


def save_data(new_data):
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    # Load existing history
    try:
        with open(FILE, "r") as f:
            history = json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        history = {}

    # Add new entry
    history[timestamp] = new_data

    # Save back to file
    with open(FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return {}
