import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

# ASCII art for display
ascii_art = """
██████   ██████   ██ ███████  ██████  ███    ██ ████████ ██████  ███████ 
██   ██ ██    ██ ███ ██      ██    ██ ████   ██    ██    ██   ██ ██      
██████  ██    ██  ██ ███████ ██    ██ ██ ██  ██    ██    ██████  █████   
██      ██    ██  ██      ██ ██    ██ ██  ██ ██    ██    ██   ██ ██      
██       ██████   ██ ███████  ██████  ██   ████    ██    ██   ██ ███████ 
"""

def find_and_collect_tokens():
    # Open a folder selection dialog
    Tk().withdraw()  # Hides the main tkinter window
    starting_folder = askdirectory(title="Select Folder to Search")
    
    if not starting_folder:
        print("No folder selected. Exiting.")
        return

    discord_tokens = []
    other_tokens = []

    # Walk through the directory tree
    for root, _, files in os.walk(starting_folder):
        for file in files:
            if file.lower() == "discordtokens.txt" or file.lower() == "tokens.txt":
                file_path = os.path.join(root, file)
                try:
                    # Read the contents of the file
                    with open(file_path, "r") as f:
                        tokens = f.readlines()
                        for token in tokens:
                            token = token.strip()  # Remove any surrounding whitespace or newlines
                            if token and len(token) <= 80:  # Ensure token length doesn't exceed 80 characters
                                if file.lower() == "discordtokens.txt":
                                    discord_tokens.append(token)
                                else:
                                    other_tokens.append(token)
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

    # Write Discord tokens to a separate file
    try:
        with open("DiscordTokens.txt", "w") as f:
            for token in discord_tokens:
                f.write(token + "\n")
        print(f"Discord tokens collected successfully in DiscordTokens.txt")
    except Exception as e:
        print(f"Could not write to DiscordTokens.txt: {e}")
    
    # Write other tokens to a separate file
    try:
        with open("Tokens.txt", "w") as f:
            for token in other_tokens:
                f.write(token + "\n")
        print(f"Other tokens collected successfully in Tokens.txt")
    except Exception as e:
        print(f"Could not write to Tokens.txt: {e}")

def delete_old_files():
    # Delete both AllTokens.txt and DiscordTokens.txt files if they exist
    files_to_delete = ["AllTokens.txt", "DiscordTokens.txt", "Tokens.txt"]
    for file in files_to_delete:
        if os.path.exists(file):
            try:
                os.remove(file)
                print(f"Old {file} deleted successfully.")
            except Exception as e:
                print(f"Could not delete {file}: {e}")
        else:
            print(f"{file} does not exist.")

def show_console_menu():
    print(ascii_art)
    print("\nMenu:")
    print("1. Delete Old Tokens Files (AllTokens.txt, DiscordTokens.txt, Tokens.txt)")
    print("2. Collect Tokens from Directory")
    print("3. Exit")

    # Get user input for menu choice
    while True:
        choice = input("Enter your choice (1, 2, 3): ").strip()
        
        if choice == "1":
            delete_old_files()
        elif choice == "2":
            find_and_collect_tokens()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the console-based menu
show_console_menu()
