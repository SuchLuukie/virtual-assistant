# Import libraries
import tkinter as tk

# Import files
from gui import LoginGUI


def main():
	root = tk.Tk()
	app = LoginGUI(root)

	root.mainloop()


if __name__ == '__main__':
	main()
