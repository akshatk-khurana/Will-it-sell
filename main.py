"""
The main file to run this application and provide a GUI which uses the prediction model from
"""

import customtkinter as ctk
from PIL import ImageTk, Image
import os

WIDTH = 800
HEIGHT = 600

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class EtsyApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Etsy Sales Predictor")
        self.geometry(f"{WIDTH}x{HEIGHT}")  

        self.upload_button = ctk.CTkButton(self, 
                                      text="Upload Design",
                                      command=self.on_upload_click,
                                      height=20,
                                      width=100,
                                      corner_radius=5,
                                      font=("Tahoma", 16),
                                      state="normal")
        
        self.upload_button.pack(pady=60, padx=60)  

        self.chosen_image = None

        self.chosen_label = ctk.CTkLabel(self, 
                                              text="")
        self.chosen_label.pack(pady=80)
        
        self.allow_to_go_ahead = False
    
    def on_upload_click(self):
        allowed_file_types = [
            ("Image files", ".png .jpg .jpeg")
        ]

        image_path = ctk.filedialog.askopenfilename(filetypes=
                                                    allowed_file_types)
    
        if len(image_path) > 0:
            img = Image.open(image_path)
            self.chosen_image = ImageTk.PhotoImage(img)

            image_path_to_display = image_path.split("/")[-1]
            self.chosen_label.configure(text=
                                        image_path_to_display)
            
            self.allow_to_go_ahead = True
        else:
            self.allow_to_go_ahead = False
            self.chosen_label.configure(text=
                                        "No file chosen.")

app = EtsyApp()
app.mainloop()