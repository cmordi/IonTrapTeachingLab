import sys
from cx_Freeze import setup, Executable

target_script = "GUI.py"

# Create an instance of the Executable class
executable = Executable(
    script=target_script,
    base="Win32GUI",  # "Win32GUI" for a GUI application on Windows
    icon=None   # Specify the path to icon file
)

# Define additional options for the setup
options = {
    "build_exe": {
        "includes": ["tkinter", "serial"],
    }
}

# Use the setup() function to create the executable
setup(
    name="Your Application Name",
    version="1.0",
    description="Description of your application",
    executables=[executable],
    options=options
)
