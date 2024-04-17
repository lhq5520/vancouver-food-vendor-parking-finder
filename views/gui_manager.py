'''
CS5001 Spring 2024 Final Project
@WeifanLi

function that used to create gui widget and area
'''
import tkinter as tk
from tkinter import scrolledtext, ttk, simpledialog, messagebox

# Initialize the display_area as None; it will be set when the GUI starts.
display_area = None


def setup_root(root, title="Vancouver Street Parking Info System"):
    """
    Purpose: Configure the root window of the tkinter application
    with a title and necessary settings.

    Parameters:
        root (tk.Tk): The root window of the application.
        title (str): The title to set for the window.

    Returns: None
    """
    root.title(title)


def setup_frame(root):
    """
    Purpose: Create and configure the main frame in the tkinter application.

    Parameters:
        root (tk.Tk): The root window of the application.

    Returns:
        tk.Frame: The configured frame that will be used to hold other widgets.
    """
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    return frame


def setup_display_area(frame):
    """
    Purpose: Set up a scrolled text area within a given frame for
    displaying output to the user.

    Parameters:
        frame (tk.Frame): The frame in which the
        scrolled text area will be placed.

    Returns: None
    """
    global display_area
    display_area = scrolledtext.ScrolledText(frame, height=15, width=70)
    display_area.pack(padx=5, pady=5)
    display_area.configure(state='disabled')


def append_to_display_area(text):
    """
    Purpose: Append text to the scrollable display area,
    ensuring it remains disabled for editing.

    Parameters:
        text (str): The text to append to the display area.

    Returns: None
    """
    global display_area
    if display_area:
        display_area.configure(state='normal')
        display_area.insert(tk.END, text + "\n")
        display_area.configure(state='disabled')
        display_area.see(tk.END)


def clear_display_area():
    """
    Purpose: Clear all text from the display area.

    Parameters: None

    Returns: None
    """
    global display_area
    if display_area:
        display_area.configure(state='normal')
        display_area.delete('1.0', tk.END)  # Clear all text from the widget
        display_area.configure(state='disabled')


def setup_buttons(frame, run_view_all_parking_info, run_view_all_food_vendor,
                  run_look_up_parking_by_geo, run_find_nearest_parking_spot, run_clear_display, exit_app):
    """
    Purpose: Set up buttons in the specified frame for various application functionalities.

    Parameters:
        frame (tk.Frame): The frame in which to place the buttons.
        run_view_all_parking_info (function): Callback function to view all parking information.
        run_view_all_food_vendor (function): Callback function to view all food vendor information.
        run_look_up_parking_by_geo (function): Callback function to look up parking information by geographic area.
        run_find_nearest_parking_spot (function): Callback function to find the nearest parking spot to a preferred food vendor.
        run_clear_display (function): Callback function to clear the display area.
        exit_app (function): Callback function to exit the application.

    Returns: None
    """
    tk.Button(frame, text="View All Parking Info", command=run_view_all_parking_info).pack(fill=tk.X)
    tk.Button(frame, text="View All Food Vendors", command=run_view_all_food_vendor).pack(fill=tk.X)
    tk.Button(frame, text="Look Up Parking Info by Geo Area", command=run_look_up_parking_by_geo).pack(fill=tk.X)
    tk.Button(frame, text="Search Nearest Parking Spot By Preferred Food Vendor", command=run_find_nearest_parking_spot).pack(fill=tk.X)
    tk.Button(frame, text="Clear Display", command=run_clear_display).pack(fill=tk.X)
    tk.Button(frame, text="Exit", command=exit_app).pack(fill=tk.X)


def gui_input_from_drop_down_select(popup_title, options, prompt):
    """
    Purpose: Create a GUI dialog with a Combobox for user input, allowing selection from predefined options.

    Parameters:
        popup_title (str): The title for the popup window.
        options (list): A list of strings that the user can select from.
        prompt (str): The prompt to display to the user in the popup.

    Returns:
        str: The selected option, or None if no selection is made.

    Raises:
        None
    """
    def on_select():
        user_input.set(combo.get())  # Update the user_input with the selected option
        popup.destroy()  # Close the popup once selection is made

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    popup = tk.Toplevel()
    popup.title(popup_title)
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


def setup_messagebox(message_type, title, message):
    """
    Purpose: Display a messagebox with a given message type, title, and message.

    Parameters:
        message_type (str): The type of messagebox to display ('info', 'warning', 'error').
        title (str): The title for the messagebox window.
        message (str): The message content for the messagebox.

    Returns: None
    """
    if message_type == 'Info':
        messagebox.showinfo(title, message)
    elif message_type == 'Warning':
        messagebox.showwarning(title, message)
    elif message_type == 'Error':
        messagebox.showerror(title, message)
    else:
        raise ValueError("Invalid message type specified.")
