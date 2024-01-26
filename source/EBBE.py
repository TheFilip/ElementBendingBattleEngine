from main import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter.scrolledtext import ScrolledText
import sys, os, webbrowser, random, requests

# Define the version of your application
APP_VERSION = "0.1a"  # Change this to your actual version




# Save the original stdout for later use
original_stdout = sys.stdout

ROUNDNUMBER = 1  # Default round number

# Keep track of selected characters and their counts
selected_characters = {}

def reset_stdout():
    sys.stdout = original_stdout

def update_available_characters():
    available_characters = [character for character in characterList if character not in selected_characters]
    return available_characters

def generate_simulation():
    global selected_characters
    selected_characters = {}  # Reset the dictionary

    # Retrieve the selected player objects from the dropdowns
    available_characters = update_available_characters()
    team_a_players = [character for i in range(5) if left_comboboxes[i].get() != 'None' and (character := next((char for char in available_characters if char and char.name == left_comboboxes[i].get()), None)) is not None]
    team_b_players = [character for i in range(5) if right_comboboxes[i].get() != 'None' and (character := next((char for char in available_characters if char and char.name == right_comboboxes[i].get()), None)) is not None]

    # Check if each team has at least one player
    if not team_a_players or not team_b_players:
        messagebox.showwarning("Team Incomplete", "Each team must have at least one player.")
        return

    # Check if characters are not already selected
    if any(player in selected_characters for player in team_a_players + team_b_players if player is not None):
        messagebox.showwarning("Duplicate Selection", "Each character can only be selected once.")
        return

    # Check if any player has been selected more than once, excluding None
    selected_players = [player for player in team_a_players + team_b_players if player is not None]
    if len(set(selected_players)) != len(selected_players):
        messagebox.showwarning("Duplicate Player Selection", "Each player can only be selected once in the simulation.")
        return

    # Add selected characters to the dictionary with counts, excluding None
    for player in selected_players:
        selected_characters[player] = selected_characters.get(player, 0) + 1

    # Check if any player has been selected more than once, excluding None
    if any(count > 1 for count in selected_characters.values() if count > 0):
        messagebox.showwarning("Duplicate Player Selection", "Each player can only be selected once in the simulation.")
        return

    # Use the global seed variable
    global seed

    # Define the folder name
    folder_name = "Matches"

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Define the file name based on the specified format
    team_name_left = team_name_left_entry.get()
    team_name_right = team_name_right_entry.get()

    # Retrieve the round number from the entry
    round_number = int(round_number_entry.get())
    randomKey = random.randint(1, 1000000)
    file_name = f"{folder_name}/{team_name_left} vs {team_name_right} - {round_number} Round - Key {randomKey}.txt"

    try:
        # Open the file in write mode with UTF-8 encoding using a context manager
        with open(file_name, 'w', encoding='utf-8') as file:
            # Redirect stdout to the file
            sys.stdout = file

            # Call the phase1 function with the collected information
            phase1(team_name_left, team_a_players, team_name_right, team_b_players, round_number)
    finally:
        # Reset stdout to its original value
        reset_stdout()

        # Show a message indicating that the simulation has finished
        messagebox.showinfo("Simulation Finished", "Simulation completed successfully!")

    # Force an update of the Tkinter event loop
    root.update_idletasks()

# Function to open patchnotes.txt
def open_patch_notes():
    github_url = "https://raw.githubusercontent.com/TheFilip/ElementBendingBattleEngine/main/patchnotes.txt"

    try:
        # Make an HTTP request to fetch the content of the patchnotes.txt file
        response = requests.get(github_url)
        response.raise_for_status()  # Raise an exception for bad responses (e.g., 404 Not Found)

        patch_notes_content = response.text

        patch_notes_window = tk.Toplevel(root)
        patch_notes_window.title("Patch Notes")

        # Create a scrollable text widget
        patch_notes_text = ScrolledText(patch_notes_window, wrap=tk.WORD, width=80, height=20)
        patch_notes_text.insert(tk.END, patch_notes_content)
        patch_notes_text.pack(expand=True, fill='both')
        patch_notes_text.config(state=tk.DISABLED)  # Make the text widget read-only

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch patchnotes: {e}")


# Create the main window
root = tk.Tk()
root.title(f"EBBE - v{APP_VERSION}")

# Create and place the "..." button in the top left
patch_notes_button = tk.Button(root, text="...", command=open_patch_notes)
patch_notes_button.grid(row=0, column=0, sticky="nw")

# Create and place the team name input above both drop-down areas
team_name_left_label = tk.Label(root, text="Team Name (Left):")
team_name_left_label.grid(row=0, column=1, padx=10, pady=5)

team_name_left_entry = tk.Entry(root, width=15)
team_name_left_entry.insert(0, "TeamA")  # Initial value
team_name_left_entry.grid(row=0, column=2, padx=10, pady=5)

team_name_right_label = tk.Label(root, text="Team Name (Right):")
team_name_right_label.grid(row=0, column=3, padx=10, pady=5)

team_name_right_entry = tk.Entry(root, width=15)
team_name_right_entry.insert(0, "TeamB")  # Initial value
team_name_right_entry.grid(row=0, column=4, padx=10, pady=5)

# Create and place drop-downs on the left
left_comboboxes = []
for i in range(5):
    label = tk.Label(root, text=f"Player {i+1}:")
    label.grid(row=i+1, column=1, padx=10, pady=5)
    
    left_combobox = ttk.Combobox(root, values=[character.name if character else 'None' for character in characterList])
    left_combobox.grid(row=i+1, column=2, padx=10, pady=5)
    left_combobox.set(characterList[0].name if characterList[0] else 'None')
    left_comboboxes.append(left_combobox)

# Create and place drop-downs on the right
right_comboboxes = []
for i in range(5):
    label = tk.Label(root, text=f"Player {i+1}:")
    label.grid(row=i+1, column=3, padx=10, pady=5)
    
    right_combobox = ttk.Combobox(root, values=[character.name if character else 'None' for character in characterList])
    right_combobox.grid(row=i+1, column=4, padx=10, pady=5)
    right_combobox.set(characterList[0].name if characterList[0] else 'None')
    right_comboboxes.append(right_combobox)

# Create and place the round number input
round_number_label = tk.Label(root, text="Round Number:")
round_number_label.grid(row=7, column=1, padx=10, pady=5)

round_number_entry = tk.Entry(root, width=5)
round_number_entry.insert(0, ROUNDNUMBER)  # Initial value
round_number_entry.grid(row=7, column=2, padx=10, pady=5)

# Create and place the "Generate/Simulate" button in the middle at the bottom
generate_button = tk.Button(root, text="Simulate Match", command=generate_simulation)
generate_button.grid(row=7, column=3, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
