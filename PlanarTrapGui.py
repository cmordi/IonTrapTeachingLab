import tkinter as tk


def command1():
    # Send command '1' over the serial port
    pass

def command2():
    # Send command '2' over the serial port
    pass

def command3():
    # Send command '3' over the serial port
    pass

def command4():
    # Send command '4' over the serial port
    pass
# Create a new tkinter window
window = tk.Tk()

# Create four buttons and assign each to a different command
button1 = tk.Button(window, text="Button 1", command=command1)
button2 = tk.Button(window, text="Button 2", command=command2)
button3 = tk.Button(window, text="Button 3", command=command3)
button4 = tk.Button(window, text="Button 4", command=command4)

# Place the buttons in the window with padding
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)

# Start the tkinter main loop
window.mainloop()


