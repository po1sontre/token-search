import os
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore
import re

# Initialize colorama for colored output
init(autoreset=True)

# ASCII art
print("""
      ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
     ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌          
     ▐░▌   ▄   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
     ▐░▌ ▐░▌░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
     ▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
     ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
      ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
""")

def select_folder():
    """Opens a folder selection dialog and returns the chosen path."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    folder = filedialog.askdirectory()
    return folder

def search_tokens(folder):
    """Searches for token-like strings in the specified folder and subfolders."""
    tokens_found = []
    print(Fore.YELLOW + f"Searching in: {folder}")
    
    # Regex pattern to match tokens with length between 59 and 64 characters
    token_pattern = r"[A-Za-z0-9-_]{59,64}"

    # Specify the filenames you want to check
    target_files = ["DiscordTokens", "tokens"]
    
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            # Check if the filename matches "DiscordTokens" or "tokens"
            if filename in target_files:  
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    tokens = re.findall(token_pattern, content)
                    tokens_found.extend(tokens)
                    
    return tokens_found

def save_results(tokens_found):
    """Saves found tokens to a file."""
    with open("found_tokens.txt", "w") as f:
        for token in tokens_found:
            f.write(f"{token}\n")
    print(Fore.GREEN + "Tokens saved to 'found_tokens.txt'.")

def show_credits():
    """Displays credits for the program."""
    print(Fore.CYAN + "Discord Token Finder v1.0")
    print(Fore.CYAN + "Developed by: po1sontre")

def main_menu():
    """Main menu for the tool."""
    while True:
        print(Fore.BLUE + "\n--- Discord Token Finder ---")
        print(Fore.BLUE + "1. Start Search")
        print(Fore.BLUE + "2. Show Credits")
        print(Fore.BLUE + "3. Exit")
        
        choice = input(Fore.WHITE + "Choose an option: ")
        
        if choice == '1':
            folder = select_folder()
            if folder:
                tokens = search_tokens(folder)
                if tokens:
                    print(Fore.GREEN + f"Found {len(tokens)} token(s).")
                    save_results(tokens)
                else:
                    print(Fore.RED + "No tokens found.")
        elif choice == '2':
            show_credits()
        elif choice == '3':
            print(Fore.YELLOW + "Exiting program. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
