import tkinter as tk
import serial as ser 

# Create a new tkinter window
window = tk.Tk()

frame = tk.Frame()
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

ser = ser.Serial('COM3', 9600)

# "All Electrodes"
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

#"Electrode Set 'a'"
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

#"Electrode Set 'b'"
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

# "Electrode Set 'c'"
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

#"Electrode Set 'd'"
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

# "Electrode Set 'e'"
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

def submit():
    all_choice = radio_var_all.get()
    if all_choice:
        ser.write(("all " + all_choice + "\n").encode())

    a_choice = radio_var_set_a.get()
    if a_choice:
        ser.write(("a " + a_choice + "\n").encode())

    b_choice = radio_var_set_b.get()
    if b_choice:
        ser.write(("b " + b_choice + "\n").encode())

    c_choice = radio_var_set_c.get()
    if c_choice:
        ser.write(("c " + c_choice + "\n").encode())

    d_choice = radio_var_set_d.get()
    if d_choice:
        ser.write(("d " + d_choice + "\n").encode())

    e_choice = radio_var_set_e.get()
    if e_choice:
        ser.write(("e " + e_choice + "\n").encode())


submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.grid(row=row+1, column=0, columnspan=2, pady=10, sticky=tk.W)

def on_close():
    ser.close()  # close the serial connection
    window.destroy()  # destroy the window

window.protocol("WM_DELETE_WINDOW", on_close)

# Start the tkinter main loop
window.mainloop()
