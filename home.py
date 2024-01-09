import tkinter as tk
from tkinter import ttk, messagebox
import requests
import customtkinter as ctk
login_status=False

class Home():
    def __init__(self, app):

        self.app = app

      
        self.welcome_frame = ctk.CTkFrame(
            master=app, border_width=2, corner_radius=10, width=650, height=550)
        self.welcome_frame.place(x=30, y=30)

        
        self.label = ctk.CTkLabel(master=self.welcome_frame,
                                  text='MAIN WINDOW')
        self.label.place(x=300, y=50)

        