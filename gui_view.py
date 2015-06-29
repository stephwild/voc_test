from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty

from voc_fill import init_array
#from random_draw import random_draw

nbr_succeed = 0
nbr_test = 4
#max_retries = NumericProperty(3)

Builder.load_file('kv/menu.kv')
Builder.load_file('kv/quizz.kv')
#Builder.load_file('kv/voclist.kv')
#Builder.load_file('kv/settings.kv')

class MenuScreen(Screen):
    def run_quizz():
        pass

    def run_voclist():
        pass

    def run_settings():
        pass

class QuizzScreen(Screen):
    max_retries = NumericProperty(3)
    keyword = StringProperty('Hello World')
    pass

class VocListScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(QuizzScreen(name='quizz'))
sm.add_widget(VocListScreen(name='voclist'))
sm.add_widget(SettingsScreen(name='settings'))

class VocApp(App):
    def build(self):
        # Fill the VocItem array with the specified file
        tab = init_array(False)
        sm.current = 'quizz'

        return sm

if __name__ == '__main__':
    VocApp().run()
