import pyshorteners
from PIL import Image,ImageTk
import customtkinter
import tkinter
import webbrowser
from tkinter import messagebox
import validators
root = customtkinter.CTk()
root.title("Url Shortner")
root.resizable(0,0)
root.geometry("500x400+500+150")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
#url shortener
def shorten():
    url = url_entry.get()
    if url == "":
        messagebox.showerror("Error", "Please enter the URL.")
        return
    if not validators.url(url):
        messagebox.showerror("Error", "The URL entered is not valid. Please enter a valid URL.")
        return
    try:
        url_shortener = pyshorteners.Shortener()
        short_url = url_shortener.tinyurl.short(url)
        result.configure(text="Shorten URL: \n" + short_url, cursor="hand2")
        indicator_lbl.configure(text="Click the link above to get redirected")
        result.bind("<Button-1>", lambda e: open_url(short_url))
    except pyshorteners.exceptions.ShorteningErrorException:
        messagebox.showerror("Error", "The URL cannot be shortened. Please try again later.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")  
#opens the short url
def open_url(url):
    webbrowser.open(url)
back_img = ImageTk.PhotoImage(Image.open("assets/back.png"))
back_lbl = customtkinter.CTkLabel(root,text="",image=back_img)
back_lbl.pack()
main_frame= customtkinter.CTkFrame(back_lbl,width=400,height=300,corner_radius=40,bg_color="transparent")
heading = customtkinter.CTkLabel(main_frame,text="Best URL Shortner",font=("Century Gothic",40,"bold"),text_color="yellow")
heading.place(relx = 0.5,y=35,anchor=tkinter.CENTER)
url_entry = customtkinter.CTkEntry(main_frame,placeholder_text="Enter a valid URL and see The Magic..",width=350)
url_entry.place(relx=0.5,y=90,anchor = tkinter.CENTER)
Url_shor_btn =customtkinter.CTkButton(main_frame,text="Shorten",font=("Century Gothic",20,"bold"),cursor="hand2",command=shorten)
Url_shor_btn.place(relx=0.5,y=140,anchor=tkinter.CENTER)
result = customtkinter.CTkLabel(main_frame,text="",font=("Century Gothic",20,"bold"),state="disable")
result.place(relx=0.5,y=200,anchor=tkinter.CENTER)
indicator_lbl = customtkinter.CTkLabel(main_frame,text="",state="disable")
indicator_lbl.place(anchor=tkinter.CENTER,relx=0.5,y=250)
main_frame.place(x = 50,y=50)
root.mainloop()
