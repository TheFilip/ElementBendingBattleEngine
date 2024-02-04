from main import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkinter.scrolledtext import ScrolledText
import sys, os, webbrowser, random, requests

# Define the version of your application
APP_VERSION = "0.25a"  # Change this to your actual version

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

    team_a_players = [next((char for char in available_characters if char and char.name in left_comboboxes[i].get()), None) if left_comboboxes[i].get() != 'None' else None for i in range(5)]
    team_b_players = [next((char for char in available_characters if char and char.name in right_comboboxes[i].get()), None) if right_comboboxes[i].get() != 'None' else None for i in range(5)]


    # Check if each team has at least one player
    if not any(team_a_players) or not any(team_b_players) or len(set(player for player in team_a_players if player is not None)) != 1 or len(set(player for player in team_b_players if player is not None)) != 1:
        messagebox.showwarning("Team Incomplete", "Each team must have at least one player.")
        return


    # Check if characters are not already selected, excluding None
    selected_players = [player for player in team_a_players + team_b_players if player is not None]

    # Check for duplicate selection, excluding None
    if len(set(selected_players)) != len(selected_players):
        messagebox.showwarning("Duplicate Selection", "Each character can only be selected once.")
        return


    # Add selected characters to the dictionary with counts, excluding None
    selected_characters.clear()
    for player in selected_players:
        if player is not None:
            selected_characters[player] = selected_players.count(player)

    # Check if any player has been selected more than once, excluding None
    if any(count > 1 for count in selected_characters.values()):
        messagebox.showwarning("Duplicate Player Selection", "Each player can only be selected once in the simulation.")
        return

    # Ensure that there is at least one character selected for each team
    if not any(team_a_players) or not any(team_b_players):
        messagebox.showwarning("Team Incomplete", "Each team must have at least one player.2")
        return

    # Define the folder name within the user's documents
    documents_folder = os.path.expanduser("~\\Documents")
    folder_name = os.path.join(documents_folder, "Matches")

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

    # Retrieve the state of the "Allow Emote Conversations" checkbox
    emoticon_conversations_enabled = allow_emote_conversations_var.get()

    try:
        # Open the file in write mode with UTF-8 encoding using a context manager
        with open(file_name, 'w', encoding='utf-8') as file:
            # Redirect stdout to the file
            sys.stdout = file

            # Call the phase1 function with the collected information and emoticonConversations state
            phase1(team_name_left, team_a_players, team_name_right, team_b_players, round_number, emoticon_conversations_enabled)
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

# Function to open the "Matches" folder
def open_matches_folder():
    # Get the path to the user's documents folder
    documents_folder = os.path.expanduser("~\\Documents")

    # Create the "Matches" folder within the documents folder
    folder_path = os.path.join(documents_folder, "Matches")
    os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

    # Open the file explorer in the "Matches" folder
    webbrowser.open(folder_path)

# Create the main window
root = tk.Tk()
root.title(f"EBBE - v{APP_VERSION}")

# Create and place the folder button under the "..." button
folder_button = tk.Button(root, text="📁", command=open_matches_folder)
folder_button.grid(row=1, column=0, sticky="nw", pady=5)

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
    label = tk.Label(root, text=f"Player {i+1} (Left):")
    label.grid(row=i+1, column=1, padx=10, pady=5)

    left_combobox_values = [f"{character.element} - {character.name}" if character else 'None' for character in characterList]
    left_combobox = ttk.Combobox(root, values=left_combobox_values)
    left_combobox.grid(row=i+1, column=2, padx=10, pady=5)
    left_combobox.set(left_combobox_values[0])
    left_comboboxes.append(left_combobox)

# Create and place drop-downs on the right
right_comboboxes = []
for i in range(5):
    label = tk.Label(root, text=f"Player {i+1} (Right):")
    label.grid(row=i+1, column=3, padx=10, pady=5)

    right_combobox_values = [f"{character.element} - {character.name}" if character else 'None' for character in characterList]
    right_combobox = ttk.Combobox(root, values=right_combobox_values)
    right_combobox.grid(row=i+1, column=4, padx=10, pady=5)
    right_combobox.set(right_combobox_values[0])
    right_comboboxes.append(right_combobox)

# Create and place the round number input
round_number_label = tk.Label(root, text="Round Number:")
round_number_label.grid(row=7, column=1, padx=10, pady=5)

round_number_entry = tk.Entry(root, width=5)
round_number_entry.insert(0, ROUNDNUMBER)  # Initial value
round_number_entry.grid(row=7, column=2, padx=10, pady=5)

# Create and place the "Allow Emote Conversations" checkbox
allow_emote_conversations_var = tk.BooleanVar()
allow_emote_conversations_checkbox = tk.Checkbutton(root, text="Allow Emote Conversations", variable=allow_emote_conversations_var)
allow_emote_conversations_checkbox.grid(row=7, column=3, padx=10, pady=5)

# Create and place the "Generate/Simulate" button in the middle at the bottom
generate_button = tk.Button(root, text="Simulate Match", command=generate_simulation)
generate_button.grid(row=7, column=4, pady=20)

# Start the Tkinter event loop
root.mainloop()
