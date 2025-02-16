# cyberjoe-tection-toolkit

THIS TOOL WILL BE USED FOR PENETRATION TESTING ONLY. THIS TOOL WILL NOT BE USED FOR ANYTHING BAD. ITS A TOOL FOR PENETRATION TESTING PROFESSIONALS. ITS VERY BASIC. ONLY USE THIS TOOL IF YOU HAVE A CONTRACT FOR A PENTEST.

How to Use and Expand:

Save: Save the code as a .py file (cyberjoe_tection.py).

Install Tkinter: If you don't have it, install it: sudo apt-get install python3-tk (on Debian/Ubuntu) or the equivalent for your system.

Run: Execute the script: python3 cyberjoe_tection.py

______________________________________________________________________________________________________

GUI Framework: Uses tkinter and ttk (themed Tkinter) for a more modern look and feel. ttk widgets are generally preferred over standard tk widgets.
Tool Selection: A ttk.Combobox allows the user to select from a list of tools. You'll need to expand this list.
Dynamic Options: The create_tool_options() function is crucial. It clears the options frame and creates new widgets (entry fields, labels, etc.) based on the currently selected tool. This is how you make the GUI adapt.
Scrolled Output: Uses scrolledtext.ScrolledText so the output area has a scrollbar if the output is too long. The output is initially disabled to prevent direct editing by the user, and re-enabled only when new output is added.
Error Handling: Includes try...except blocks to catch FileNotFoundError (if the tool command isn't found) and other exceptions. Displays error messages in a popup box.
subprocess for Running Tools: Uses subprocess.Popen which is the recommended way to run external commands. It captures both standard output (stdout) and standard error (stderr).
Decoding Output: Decodes the byte output from subprocess using .decode() to display it as text in the GUI.
Clearing Output: The output area is cleared before running a new command.
Disabling Output Editing: The output area is disabled after displaying the output so the user can not edit it directly.
Event Binding: The gui.tool_dropdown.bind("<<ComboboxSelected>>", gui.on_tool_select) line is very important. It connects the combobox's selection event to the on_tool_select function. This makes the GUI update the options whenever the user chooses a different tool.
