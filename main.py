from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from Screens.db import DB  # <- keep as is

KV = r"""
ScreenManager:
    LoginScreen:
    HomeScreen:

<LoginScreen>:
    name: "login"
    BoxLayout:
        orientation: "vertical"
        padding: 16
        spacing: 10

        Label:
            text: "MyKivyApp"
            font_size: "22sp"
            size_hint_y: None
            height: "40dp"

        TextInput:
            id: user
            hint_text: "Username"
            multiline: False

        TextInput:
            id: pwd
            hint_text: "Password"
            password: True
            multiline: False

        BoxLayout:
            size_hint_y: None
            height: "48dp"
            spacing: 10

            Button:
                text: "Login"
                on_release: root.login(user.text, pwd.text)

            Button:
                text: "Sign up"
                on_release: root.signup(user.text, pwd.text)

        Label:
            id: msg
            text: root.message
            color: (1,0,0,1)

<HomeScreen>:
    name: "home"
    BoxLayout:
        orientation: "vertical"
        padding: 12
        spacing: 8

        Label:
            text: "Welcome, " + root.username
            size_hint_y: None
            height: "32dp"

        TextInput:
            id: note
            hint_text: "Write a note"
            size_hint_y: None
            height: "100dp"

        Button:
            text: "Add Note"
            size_hint_y: None
            height: "44dp"
            on_release: root.add_note(note.text); note.text = ""

        ScrollView:
            GridLayout:
                id: notes_box
                cols: 1
                size_hint_y: None
                height: self.minimum_height
"""

class LoginScreen(Screen):
    message = StringProperty("")

    def on_pre_enter(self):
        DB.init()

    def login(self, u, p):
        if DB.check_login(u, p):
            self.manager.get_screen("home").username = u
            self.manager.current = "home"
            self.message = ""
        else:
            self.message = "Invalid login"

    def signup(self, u, p):
        ok, msg = DB.create_user(u, p)
        self.message = msg

class HomeScreen(Screen):
    username = StringProperty("")

    def on_pre_enter(self):
        self.load_notes()

    def add_note(self, text):
        if text.strip():
            DB.add_note(self.username, text.strip())
            self.load_notes()

    def load_notes(self):
        notes = DB.list_notes(self.username)
        box = self.ids.notes_box
        box.clear_widgets()
        from kivy.uix.label import Label
        for n in notes:
            box.add_widget(Label(text=f"• {n}", size_hint_y=None, height="28dp"))

class MyApp(App):
    def build(self):
        DB.init()
        return Builder.load_string(KV)

if __name__ == "__main__":
    MyApp().run()
