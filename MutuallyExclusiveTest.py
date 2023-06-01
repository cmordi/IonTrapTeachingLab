import tkinter as tk

def toggle_checkboxes(checkboxes, current_checkbox):
    if current_checkbox in mutually_exclusive_checkboxes:
        for checkbox in mutually_exclusive_checkboxes:
            if checkbox != current_checkbox:
                checkbox.deselect()

def create_checkbox(window, text, checkboxes):
    checkbox = tk.Checkbutton(window, text=text)
    checkbox.configure(command=lambda: toggle_checkboxes(checkboxes, checkbox))
    checkbox.pack()
    checkboxes.append(checkbox)

# Create the main window
window = tk.Tk()

# Create a list to store the checkboxes
checkboxes = []
mutually_exclusive_checkboxes = []

# Create the checkboxes
create_checkbox(window, "Checkbox 1", checkboxes)
create_checkbox(window, "Checkbox 2", checkboxes)
create_checkbox(window, "Checkbox 3", checkboxes)
mutually_exclusive_checkboxes.extend(checkboxes[:2])  # Checkbox 1 and Checkbox 2 are mutually exclusive

# Start the main Tkinter main loop
window.mainloop()
