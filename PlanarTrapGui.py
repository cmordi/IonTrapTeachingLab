import tkinter as tk


# Create a new tkinter window
window = tk.Tk()

frame = tk.Frame()
frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

row = 0
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Main Planar Modes", font=bold_font).grid(row=row, column=1, pady=10)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All Off", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All Low", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="All High", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set A", font=bold_font).grid(row=row, column=1, pady=10)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
bold_font = ('Helvetica', 16, 'bold')
tk.Label(frame, text="Electrode Set B", font=bold_font).grid(row=row, column=1, pady=10)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Off", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="Low", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

row += 1
label_font = ('Helvetica', 12)
tk.Label(frame, text="High", font=label_font).grid(row=row, column=0)
checkbutton_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(frame, variable=checkbutton_var)
checkbutton.grid(row=row, column=1)

# Start the tkinter main loop
window.mainloop()


