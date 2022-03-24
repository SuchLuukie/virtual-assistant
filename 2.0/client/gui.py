# Import libraries
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

class GUI:
	def __init__(self, root):
		self.root = root

		# Basic settings for the window
		self.root.title("The Program")
		self.root.geometry("400x500")
		self.root.configure(bg="#23272A")

		# Define all the frames inside the window
		self.background = background(self.root)


# Tk Frame that will hold login information
class background(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill="both", expand=True)
        
        self.gif_label = ImageLabel(self.frame)
        self.gif_label.pack()
        self.gif_label.load("background.gif")


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
