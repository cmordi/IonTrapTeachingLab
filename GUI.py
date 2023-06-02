import tkinter as tk


# Allows mutual exclusivity of specified checkboxes
def toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes, current_checkbox):
    if current_checkbox.get():
        for checkbox in mutually_exclusive_checkboxes:
            if checkbox != current_checkbox:
                checkbox.set(False)

# Creates checkboxes in grid and fills a list of all checkboxes
def create_checkbox(window, text, mutually_exclusive_checkboxes, row):
    checkbox_var = tk.BooleanVar()
    checkbox = tk.Checkbutton(window, text=text, variable=checkbox_var,
                              command=lambda: toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes, checkbox_var))
    checkbox.grid(row=row, column=1, sticky='w')
    checkboxes.append(checkbox_var)
    return checkbox_var

checkboxes = []


# Create a new tkinter window
window = tk.Tk()
frame = tk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)


# All Electrodes
row = 0
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="All Electrodes:", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
all_high_var = create_checkbox(frame, "All High", checkboxes, row)

row += 1
label_font = ('Helvetica', 12)
all_low_var = create_checkbox(frame, "All Low", checkboxes, row)

row += 1
label_font = ('Helvetica', 12)
all_off_var = create_checkbox(frame, "All Off", checkboxes, row)


# Electrode Set 'a'
a_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'a':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
a_high_var = create_checkbox(frame, "High", a_mutex, row)
a_mutex.append(a_high_var)

row += 1
label_font = ('Helvetica', 12)
a_low_var = create_checkbox(frame, "Low", a_mutex, row)
a_mutex.append(a_low_var)

row += 1
label_font = ('Helvetica', 12)
a_off_var = create_checkbox(frame, "Off", a_mutex, row)
a_mutex.append(a_off_var)


# Electrode Set 'b'
b_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'b':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
b_high_var = create_checkbox(frame, "High", b_mutex, row)
b_mutex.append(b_high_var)

row += 1
label_font = ('Helvetica', 12)
b_low_var = create_checkbox(frame, "Low", b_mutex, row)
b_mutex.append(b_low_var)

row += 1
label_font = ('Helvetica', 12)
b_off_var = create_checkbox(frame, "Off", b_mutex, row)
b_mutex.append(b_off_var)


# Electrode Set 'c'
c_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'c':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
c_high_var = create_checkbox(frame, "High", c_mutex, row)
c_mutex.append(c_high_var)

row += 1
label_font = ('Helvetica', 12)
c_low_var = create_checkbox(frame, "Low", c_mutex, row)
c_mutex.append(c_low_var)

row += 1
label_font = ('Helvetica', 12)
c_off_var = create_checkbox(frame, "Off", c_mutex, row)
c_mutex.append(c_off_var)


# Electrode Set 'd'
d_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'd':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
d_high_var = create_checkbox(frame, "High", d_mutex, row)
d_mutex.append(d_high_var)

row += 1
label_font = ('Helvetica', 12)
d_low_var = create_checkbox(frame, "Low", d_mutex, row)
d_mutex.append(d_low_var)

row += 1
label_font = ('Helvetica', 12)
d_off_var = create_checkbox(frame, "Off", d_mutex, row)
d_mutex.append(d_off_var)


# Electrode Set 'e'
e_mutex = [all_high_var, all_low_var, all_off_var]

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'e':", font=bold_font).grid(row=row, column=0, pady=10)

row += 1
label_font = ('Helvetica', 12)
e_high_var = create_checkbox(frame, "High", e_mutex, row)
e_mutex.append(e_high_var)

row += 1
label_font = ('Helvetica', 12)
e_low_var = create_checkbox(frame, "Low", e_mutex, row)
e_mutex.append(e_low_var)

row += 1
label_font = ('Helvetica', 12)
e_off_var = create_checkbox(frame, "Off", e_mutex, row)
e_mutex.append(e_off_var)


# Start tkinter main loop
window.mainloop()
