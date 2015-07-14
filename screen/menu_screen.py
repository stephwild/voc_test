from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from . import sc_globals

Builder.load_file('kv/menu.kv')

class MenuScreen(Screen):

    def run_quizz(self):
        # Init Quizz for the QuizzScreen contain in ScreenManager
        sc_globals.sm.get_screen('quizz').init_quizz_globaly()
        sc_globals.sm.get_screen('quizz').init_quizz_entry()

        sc_globals.sm.current = 'quizz'

    def run_voclist(self):
        sc_globals.sm.get_screen('voclist').make_layout()
        sc_globals.sm.current = 'voclist'

    def run_settings(self):
        sc_globals.sm.current = 'settings'
