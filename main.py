from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window


Window.clearcolor = (1, 0, 0, 1)

class LoginApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', pos_hint={'center_x': 0.5, 'center_y': 0.5}, size_hint=(None, None))

        self.username_input = TextInput(hint_text='Username', multiline=False, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5})
        self.result_label = TextInput(hint_text='', disabled=True, size_hint=(None, None), size=(200, 40), pos_hint={'center_x': 0.5},
                                       foreground_color=(1, 1, 1, 1))

        login_btn = Button(text='Login', size_hint=(None, None), size=(100, 40), pos_hint={'center_x': 0.5}, background_color=(1, 1, 0, 1))
        login_btn.bind(on_press=self.login)

        layout.add_widget(self.result_label)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_btn)

        return layout

    def login(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        if username == 'DL' and password == '123':
            self.result_label.text = 'Success!'
        elif username == '' and password == '':
            self.result_label.text = 'Empty!'
        elif username != 'DL' or password != '123':
            self.result_label.text = 'wrong input!'
        else:
            self.result_label.text = 'Failed.'


if __name__ == '__main__':
    LoginApp().run()
