import os
import tkinter as tk
from tkinter import filedialog
from colorama import init, Fore

# Initialize colorama for colored output
init(autoreset=True)

# ASCII art
print("""
      ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
     ▐░▌       ▐░▌▐░▌          ▐░▌          ▐░▌          ▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          
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
    """Searches for token files in the specified folder and subfolders."""
    tokens_found = []
    print(Fore.YELLOW + f"Searching in: {folder}")
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            if "token" in filename.lower():
                file_path = os.path.join(dirpath, filename)
                with open(file_path, 'r') as f:
                    tokens = f.read().strip()
                    tokens_found.append((file_path, tokens))
    return tokens_found

def save_results(tokens_found):
    """Saves found tokens to a file."""
    with open("found_tokens.txt", "w") as f:
        for path, token in tokens_found:
            f.write(f"File: {path}\nToken: {token}\n\n")
    print(Fore.GREEN + "Results saved to 'found_tokens.txt'.")

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
