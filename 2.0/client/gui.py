# Import libraries
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

# Import files
from login import Login

class LoginGUI:
    def __init__(self, root):
        self.root = root

        # Basic settings for the window
        self.root.title("Athena Virtual Assistant")
        self.root.resizable(False, False)

        # Define all the frames inside the window
        self.background = Background(self.root)
        self.initiate_logins()


    def initiate_logins(self): 
        self.login_inputs = LoginForms(self.root)
        self.login_handler = Login(self)

        self.login_inputs.password_input.bind("<Return>", self.login_handler.login_command)


# Tk Frame that will hold login information
class LoginForms:
    def __init__(self, root):
        self.root = root
        self.username_frame = tk.Frame(self.root, width=350, height=200)
        self.username_frame.place(anchor="center", x=270, y=150)

        self.password_frame = tk.Frame(self.root, width=350, height=200)
        self.password_frame.place(anchor="center", x=270, y=230)

        self.username_var = tk.StringVar()
        self.username_input = tk.Entry(self.username_frame, textvariable=self.username_var, width=17, font=("Helvetica", 30, "bold"), justify='center')
        self.username_input.pack()
        self.username_input.focus()

        self.password_var = tk.StringVar()
        self.password_input = tk.Entry(self.password_frame, textvariable=self.password_var, show="\u2022", width=17, font=("Helvetica", 30, "bold"), justify='center')
        self.password_input.pack()
        

# Tk Frame that will hold background
class Background:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        
        self.gif_label = ImageLabel(self.frame)
        self.gif_label.configure(borderwidth=0, highlightthickness=0)
        self.gif_label.pack()

        self.gif_label.load("background.gif")


# Tk Label that handles animation of background gif
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
