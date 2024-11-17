import datetime

def log_command(command):
    """
    Logs the executed command with a timestamp to a log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Command executed: {command}\n"
    
    # Open the log file and append the log entry
    with open("command_log.txt", "a") as log_file:
        log_file.write(log_entry)
