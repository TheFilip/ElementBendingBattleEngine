from main import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sys, os




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

# Create the main window
root = tk.Tk()
root.title("Team Simulation")

# Create and place the team name input above both drop-down areas
team_name_left_label = tk.Label(root, text="Team Name (Left):")
team_name_left_label.grid(row=0, column=0, padx=10, pady=5)

team_name_left_entry = tk.Entry(root, width=15)
team_name_left_entry.insert(0, "TeamA")  # Initial value
team_name_left_entry.grid(row=0, column=1, padx=10, pady=5)

team_name_right_label = tk.Label(root, text="Team Name (Right):")
team_name_right_label.grid(row=0, column=2, padx=10, pady=5)

team_name_right_entry = tk.Entry(root, width=15)
team_name_right_entry.insert(0, "TeamB")  # Initial value
team_name_right_entry.grid(row=0, column=3, padx=10, pady=5)

# Create and place drop-downs on the left
left_comboboxes = []
for i in range(5):
    label = tk.Label(root, text=f"Player {i+1} (Left):")
    label.grid(row=i+1, column=0, padx=10, pady=5)
    
    left_combobox = ttk.Combobox(root, values=[character.name if character else 'None' for character in characterList])
    left_combobox.grid(row=i+1, column=1, padx=10, pady=5)
    left_combobox.set(characterList[0].name if characterList[0] else 'None')
    left_comboboxes.append(left_combobox)

# Create and place drop-downs on the right
right_comboboxes = []
for i in range(5):
    label = tk.Label(root, text=f"Player {i+1} (Right):")
    label.grid(row=i+1, column=2, padx=10, pady=5)
    
    right_combobox = ttk.Combobox(root, values=[character.name if character else 'None' for character in characterList])
    right_combobox.grid(row=i+1, column=3, padx=10, pady=5)
    right_combobox.set(characterList[0].name if characterList[0] else 'None')
    right_comboboxes.append(right_combobox)

# Create and place the round number input
round_number_label = tk.Label(root, text="Round Number:")
round_number_label.grid(row=7, column=0, padx=10, pady=5)

round_number_entry = tk.Entry(root, width=5)
round_number_entry.insert(0, ROUNDNUMBER)  # Initial value
round_number_entry.grid(row=7, column=1, padx=10, pady=5)

# Create and place the "Generate/Simulate" button in the middle at the bottom
generate_button = tk.Button(root, text="Simulate Match", command=generate_simulation)
generate_button.grid(row=7, column=2, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
