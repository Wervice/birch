# Birch is a logging library for all your favorite languages
# by Constantin Volke (aka Wervice)

from datetime import UTC, datetime

birch_path = "./birch_log_python"

if not "birch_verbose" in locals():
    birch_verbose = True

if not "birch_path" in locals():
    raise Exception("Birch file path is not set.\nPlease define the variable birch_path")

def get_utc_time():
    # Get current UTC time
    utc_time = datetime.now(UTC)

    # Format the time
    formatted_time = utc_time.strftime('%H:%M:%S:%f %m/%d/%Y')

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
    if level == "verb" or level == "verbose" or level == 0 or level == "V":
        if birch_verbose:
            print(f"[VERBOSE] {get_utc_time()} | {message}")
            with open(birch_path, "a") as birch_log:
                 birch_log.write(f"[VERBOSE]\t{get_utc_time()}\t{message}")

birch("verb", "message")
