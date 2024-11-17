import os
import sys
from spy_logger import log_command
from utils import execute_command

def main():
    print("Welcome to SpyShell! Type 'exit' to quit.")
    
    while True:
        # Prompt for input
        user_input = input("SpyShell> ")
        
        # Exit condition
        if user_input.lower() == "exit":
            print("Exiting SpyShell.")
            break
        
        # Log the command and execute it
        log_command(user_input)  # Log the command
        output = execute_command(user_input)  # Execute command and get output
        
        # Print output of the command
        print(output)

if __name__ == "__main__":
    main()
