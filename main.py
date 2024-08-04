"""
The main file to run this application and provide a GUI which uses the prediction model from
"""

import customtkinter as ctk
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()

root.title("Will it sell?")
root.geometry('1000x600')