import tkinter as tk

# Create a new tkinter window
window = tk.Tk()

frame = tk.Frame()
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a group of radio buttons for "All Electrodes"
row = 0
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="All Electrodes:", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_all = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All Off", font=label_font).grid(row=row, column=0)
radio_button_all_off = tk.Radiobutton(frame, variable=radio_var_all, value="off")
radio_button_all_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All Low", font=label_font).grid(row=row, column=0)
radio_button_all_low = tk.Radiobutton(frame, variable=radio_var_all, value="low")
radio_button_all_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All High", font=label_font).grid(row=row, column=0)
radio_button_all_high = tk.Radiobutton(frame, variable=radio_var_all, value="high")
radio_button_all_high.grid(row=row, column=1)

# Create a group of radio buttons for "Electrode Set 'a'"
row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'a':", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_set_a = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
radio_button_set_a_off = tk.Radiobutton(frame, variable=radio_var_set_a, value="off")
radio_button_set_a_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
radio_button_set_a_low = tk.Radiobutton(frame, variable=radio_var_set_a, value="low")
radio_button_set_a_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
radio_button_set_a_high = tk.Radiobutton(frame, variable=radio_var_set_a, value="high")
radio_button_set_a_high.grid(row=row, column=1)

# Create a group of radio buttons for "Electrode Set 'b'"
row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'b':", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_set_b = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
radio_button_set_b_off = tk.Radiobutton(frame, variable=radio_var_set_b, value="off")
radio_button_set_b_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
radio_button_set_b_low = tk.Radiobutton(frame, variable=radio_var_set_b, value="low")
radio_button_set_b_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
radio_button_set_b_high = tk.Radiobutton(frame, variable=radio_var_set_b, value="high")
radio_button_set_b_high.grid(row=row, column=1)

# Create a group of radio buttons for "Electrode Set 'c'"
row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'c':", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_set_c = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
radio_button_set_c_off = tk.Radiobutton(frame, variable=radio_var_set_c, value="off")
radio_button_set_c_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
radio_button_set_c_low = tk.Radiobutton(frame, variable=radio_var_set_c, value="low")
radio_button_set_c_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
radio_button_set_c_high = tk.Radiobutton(frame, variable=radio_var_set_c, value="high")
radio_button_set_c_high.grid(row=row, column=1)

# Create a group of radio buttons for "Electrode Set 'd'"
row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'd':", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_set_d = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
radio_button_set_d_off = tk.Radiobutton(frame, variable=radio_var_set_d, value="off")
radio_button_set_d_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
radio_button_set_d_low = tk.Radiobutton(frame, variable=radio_var_set_d, value="low")
radio_button_set_d_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
radio_button_set_d_high = tk.Radiobutton(frame, variable=radio_var_set_d, value="high")
radio_button_set_d_high.grid(row=row, column=1)

# Create a group of radio buttons for "Electrode Set 'e'"
row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set 'e':", font=bold_font).grid(row=row, column=0, pady=10)

radio_var_set_e = tk.StringVar()

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
radio_button_set_e_off = tk.Radiobutton(frame, variable=radio_var_set_e, value="off")
radio_button_set_e_off.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
radio_button_set_e_low = tk.Radiobutton(frame, variable=radio_var_set_e, value="low")
radio_button_set_e_low.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
radio_button_set_e_high = tk.Radiobutton(frame, variable=radio_var_set_e, value="high")
radio_button_set_e_high.grid(row=row, column=1)

# Start the tkinter main loop
window.mainloop()
