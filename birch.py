# Birch is a logging library for all your favorite languages
# by Constantin Volke (aka Wervice)

from datetime import UTC, datetime
from os import path

def get_utc_time():
    # Get current UTC time
    utc_time = datetime.now(UTC)

    # Format the time
    formatted_time = utc_time.strftime('%H:%M:%S:%f')[:-3]+utc_time.strftime(' %m/%d/%Y')

    return formatted_time

def color_text(text, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'cyan': '\033[96m'
    }
    end_color = '\033[0m'  # Reset color
    if color in colors:
        return f"{colors[color]}{text}{end_color}"
    else:
        return -1

def birch(level, message):

    try:
        birch_verbose
    except NameError:
        birch_verbose = True

    try:
        birch_path
    except NameError:
        raise Exception("Birch file path is not set.\nPlease define the variable birch_path")

    if path.exists(birch_path):
        with open(birch_path, "w") as log:
            log.write("Level\t\tTime\t\t\tMessage\n")

    if level == "verb" or level == "verbose" or level == 0 or level == "V":
        if birch_verbose:
            print(color_text(f"[VERBOSE] {get_utc_time()} | {message}", "blue"))
            with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[VERBOSE]\t{get_utc_time()}\t{message}")
    elif level == "succ" or level == "success" or level == 1 or level == "S":
        print(color_text(f"[SUCCESS] {get_utc_time()} | {message}", "green"))
        with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[SUCCESS]\t{get_utc_time()}\t{message}")
    elif level == "warn" or level == "warning" or level == 2 or level == "W":
        print(color_text(f"[WARNING] {get_utc_time()} | {message}", "yellow"))
        with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[WARNING]\t{get_utc_time()}\t{message}")
    elif level == "erro" or level == "error" or level == 3 or level == "E":
        print(color_text(f"[ERROR] {get_utc_time()} | {message}", "red"))
        with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[ERROR]\t\t{get_utc_time()}\t{message}")
    elif level == "fata" or level == "fatal" or level == 4 or level == "F":
        print(color_text(f"\x1b[1m[FATAL ERROR] {get_utc_time()} | {message}\x1b[0m", "red"))
        with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[FATAL ERROR]\t{get_utc_time()}\t{message}")
    else:
        raise Exception("Birch does not know this type of logging level")
