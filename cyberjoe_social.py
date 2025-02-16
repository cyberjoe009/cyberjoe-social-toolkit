import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import os

class AdvancedSetoolkitGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cyberjoe Social Engineering")

        # --- Tool Selection ---
        self.tool_label = ttk.Label(master, text="Select Tool:")
        self.tool_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.tool_var = tk.StringVar(value="payload_generator")  # Default tool
        self.tool_dropdown = ttk.Combobox(master, textvariable=self.tool_var, 
                                          values=["payload_generator", "social_engineering", "wireless_attack", "updater"]) # Add more tools
        self.tool_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.tool_dropdown.current(0)  # Set default selection

        # --- Tool Options Frame ---
        self.options_frame = ttk.LabelFrame(master, text="Tool Options")
        self.options_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.create_tool_options()  # Initialize options based on default tool

        # --- Run Button ---
        self.run_button = ttk.Button(master, text="Run Tool", command=self.run_selected_tool)
        self.run_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        # --- Output Area ---
        self.output_label = ttk.Label(master, text="Output:")
        self.output_label.grid(row=3, column=0, sticky="w")

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10)  # Use scrolledtext
        self.output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        self.output_text.config(state=tk.DISABLED)  # Initially disabled


    def create_tool_options(self):
        # Clear existing options
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        selected_tool = self.tool_var.get()

        if selected_tool == "payload_generator":
            # Example payload generator options
            self.payload_type_label = ttk.Label(self.options_frame, text="Payload Type:")
            self.payload_type_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            self.payload_type_entry = ttk.Entry(self.options_frame)
            self.payload_type_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

            # ... more options ...

        elif selected_tool == "social_engineering":
            # ... social engineering options ...
            self.social_text_label = ttk.Label(self.options_frame, text="Social Text:")
            self.social_text_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            self.social_text_entry = ttk.Entry(self.options_frame)
            self.social_text_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        elif selected_tool == "wireless_attack":
            # ... wireless attack options ...
            self.interface_label = ttk.Label(self.options_frame, text="Interface:")
            self.interface_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
            self.interface_entry = ttk.Entry(self.options_frame)
            self.interface_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        elif selected_tool == "updater":
            pass # No options for updater


        # Add similar "elif" blocks for other tools

    def run_selected_tool(self):
        selected_tool = self.tool_var.get()
        command = []

        if selected_tool == "payload_generator":
            payload_type = self.payload_type_entry.get()
            command = ["msfvenom", "-p", payload_type, "-f", "raw"]  # Example command

        elif selected_tool == "social_engineering":
            social_text = self.social_text_entry.get()
            command = ["python", "social_engineering_script.py", social_text]  # Example

        elif selected_tool == "wireless_attack":
            interface = self.interface_entry.get()
            command = ["airodump-ng", interface] # Example

        elif selected_tool == "updater":
            command = ["apt-get", "update"] # Example

        # ... handle other tools ...

        if command:
            try:
                self.output_text.config(state=tk.NORMAL) # Enable editing
                self.output_text.delete("1.0", tk.END) # Clear previous output

                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                output = stdout.decode()
                error = stderr.decode()

                self.output_text.insert(tk.END, output)
                if error:
                    self.output_text.insert(tk.END, "\nErrors:\n" + error)

                self.output_text.config(state=tk.DISABLED) # Disable editing again

            except FileNotFoundError:
                messagebox.showerror("Error", "Command not found. Make sure the tool is installed.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

    def on_tool_select(self, event):
        self.create_tool_options()


root = tk.Tk()
gui = AdvancedSetoolkitGUI(root)
gui.tool_dropdown.bind("<<ComboboxSelected>>", gui.on_tool_select) # Update options on selection
root.mainloop()
