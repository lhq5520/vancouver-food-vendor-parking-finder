import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog

# Initialize the display_area as None; it will be set when the GUI starts.
display_area = None

def setup_display_area(frame):
    global display_area
    display_area = scrolledtext.ScrolledText(frame, height=15, width=70)
    display_area.pack(padx=5, pady=5)
    display_area.configure(state='disabled')


def append_to_display_area(text):
    global display_area
    if display_area:
        display_area.configure(state='normal')
        display_area.insert(tk.END, text + "\n")
        display_area.configure(state='disabled')
        display_area.see(tk.END)


def clear_display_area():
    global display_area
    if display_area:
        display_area.configure(state='normal')
        display_area.delete('1.0', tk.END)  # Clear all text from the widget
        display_area.configure(state='disabled')


def gui_input_from_list(prompt, options):
    """
    Creates a GUI dialog with a Combobox for input, restricting input to predefined options.

    Args:
    prompt (str): The prompt to display to the user.
    options (list): A list of strings that the user can select from.

    Returns:
    str: The selected option or None if no selection is made.
    """
    def on_select():
        user_input.set(combo.get())  # Update the user_input with the selected option
        popup.destroy()  # Close the popup once selection is made

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    popup = tk.Toplevel()
    popup.title("Selection")
    label = tk.Label(popup, text=prompt)
    label.pack(padx=10, pady=10)

    user_input = tk.StringVar(popup)
    combo = ttk.Combobox(popup, textvariable=user_input, values=options, state="readonly")
    combo.pack(padx=10, pady=5)
    combo.set(options[0])  # Optionally set the default value to the first option

    select_button = tk.Button(popup, text="Select", command=on_select)
    select_button.pack(padx=10, pady=10)

    popup.grab_set()  # Make the popup window modal
    popup.wait_window()  # Wait here until the popup is closed

    return user_input.get()  # Return the selected option or the default first option


def gui_input_from_prompt(prompt):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = simpledialog.askstring("Input", prompt)
    root.destroy()
    return user_input