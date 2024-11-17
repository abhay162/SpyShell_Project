import subprocess

def execute_command(command):
    """
    Executes the given shell command and returns the output.
    If the command fails, returns an error message.
    """
    try:
        # Use subprocess to execute system command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        # Return the command's output (stdout and stderr)
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error: {result.stderr}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"
