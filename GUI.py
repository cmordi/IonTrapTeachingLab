import tkinter as tk


def toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes, current_checkbox):
    if current_checkbox in mutually_exclusive_checkboxes:
        for checkbox in mutually_exclusive_checkboxes:
            if checkbox != current_checkbox:
                checkbox.deselect()


def create_checkbox(window, text, checkboxes, mutually_exclusive_checkboxes):
    checkbox = tk.Checkbutton(window, text=text)
    checkbox.configure(command=lambda: toggle_checkboxes(checkboxes, mutually_exclusive_checkboxes, checkbox))
    checkbox.pack()
    checkboxes.append(checkbox)
    return checkbox  # Return the created checkbox


# Create a new tkinter window
window = tk.Tk()

frame = tk.Frame()
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create the checkboxes
checkboxes = []

# Alls
all_h = create_checkbox(window, "All High", checkboxes, checkboxes)
all_l = create_checkbox(window, "All Low", checkboxes, checkboxes)
all_o = create_checkbox(window, "All Off", checkboxes, checkboxes)

# Electrode set a
group_a = [all_h, all_l, all_o]
a_h = create_checkbox(window, "High", checkboxes, group_a)
group_a.append(a_h)  # Add the checkbox to the group
a_l = create_checkbox(window, "Low", checkboxes, group_a)
group_a.append(a_l)  # Add the checkbox to the group
a_o = create_checkbox(window, "Off", checkboxes, group_a)
group_a.append(a_o)  # Add the checkbox to the group

# Electrode set b
group_b = [all_h, all_l, all_o]
b_h = create_checkbox(window, "High", checkboxes, group_b)
group_b.append(b_h)  # Add the checkbox to the group
b_l = create_checkbox(window, "Low", checkboxes, group_b)
group_b.append(b_l)  # Add the checkbox to the group
b_o = create_checkbox(window, "Off", checkboxes, group_b)
group_b.append(b_o)  # Add the checkbox to the group

# Electrode set c
group_c = [all_h, all_l, all_o]
c_h = create_checkbox(window, "High", checkboxes, group_c)
group_c.append(c_h)  # Add the checkbox to the group
c_l = create_checkbox(window, "Low", checkboxes, group_c)
group_c.append(c_l)  # Add the checkbox to the group
c_o = create_checkbox(window, "Off", checkboxes, group_c)
group_c.append(c_o)  # Add the checkbox to the group

# Electrode set d
group_d = [all_h, all_l, all_o]
d_h = create_checkbox(window, "High", checkboxes, group_d)
group_d.append(d_h)  # Add the checkbox to the group
d_l = create_checkbox(window, "Low", checkboxes, group_d)
group_d.append(d_l)  # Add the checkbox to the group
d_o = create_checkbox(window, "Off", checkboxes, group_d)
group_d.append(d_o)  # Add the checkbox to the group

# Electrode set e
group_e = [all_h, all_l, all_o]
e_h = create_checkbox(window, "High", checkboxes, group_e)
group_e.append(e_h)  # Add the checkbox to the group
e_l = create_checkbox(window, "Low", checkboxes, group_e)
group_e.append(e_l)  # Add the checkbox to the group
e_o = create_checkbox(window, "Off", checkboxes, group_e)


# Start tkinter main loop
window.mainloop()