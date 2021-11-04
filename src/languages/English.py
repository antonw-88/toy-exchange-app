from languages.LanguageInterface import LanguageInterface


class English(LanguageInterface):

    def welcome_message(self):
        print("Welcome to login screen, please log in to your account.")

    def exit_button(self):
        print("Exit")

    def login_button(self):
        print("Login")
