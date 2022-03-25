# Import libraries
import time

# Import files
from api_handler import ApiHandler
from speech import Speech


class Login:
    def __init__(self, gui):
        self.gui = gui
        self.api_handler = ApiHandler(self.gui)

        self.login_inputs = self.gui.login_inputs
        self.username_input = self.login_inputs.username_input
        self.password_input = self.login_inputs.password_input


    def login_command(self, event):
        username = self.username_input.get()
        password = self.password_input.get()

        login = self.api_handler.login_request(username, password)

        if login == False:
            self.login_inputs.username_input.delete(0, "end")
            self.login_inputs.password_input.delete(0, "end")
            self.login_inputs.username_input.focus()
            return

        elif login == True:
            self.login_inputs.username_frame.destroy()
            self.login_inputs.password_frame.destroy()
            Speech(self.api_handler)