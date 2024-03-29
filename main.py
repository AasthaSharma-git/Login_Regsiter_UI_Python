

from threading import Thread
import time
import customtkinter as ctk 
from login_register import LoginAndRegister
from home import Home


        
# Selecting GUI theme - dark,  
# light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme-blue, green, dark-blue 
ctk.set_default_color_theme("blue") 


app = ctk.CTk() 
app.geometry("700x600") 
app.resizable(False,False)
app.title("Quotes Generator") 

login_obj=LoginAndRegister(app)



def check_login_status():
    while True:
        status=login_obj.login_success()
        if status==True:
            show_home_page()
            break
            
        time.sleep(1)
        
def show_home_page():
    home_obj=Home(app)
    

check_thread=Thread(target=check_login_status)
check_thread.start()


app.mainloop()

        
