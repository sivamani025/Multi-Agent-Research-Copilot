import json
import os
from datetime import datetime


LOG_FILE = "data/history.json"


def save_run(data):

    os.makedirs("data", exist_ok=True)

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE, "r") as f:

            history = json.load(f)

    else:

        history = []

    history.append(data)

    with open(LOG_FILE, "w") as f:

        json.dump(
            history,
            f,
            indent=4
        )