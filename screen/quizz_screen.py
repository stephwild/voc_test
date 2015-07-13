from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from . import sc_globals

from parser.voc_fill import init_array
from rdm.random_draw import random_draw

Builder.load_file('kv/quizz.kv')

class QuizzScreen(Screen):
    nbr_succeed = 0
    nbr_test = 4

    max_retries = NumericProperty(3)
    keyword = StringProperty('Hello World')
    rsp_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(QuizzScreen, self).__init__(**kwargs)

        # Fill the VocItem array with the specified file
        tab = init_array(False)
        self.random_tab = random_draw(tab, self.nbr_test)
        self.i = 0

        self.init_quizz_entry()

    def init_quizz_entry(self):
        self.retry = 0
        self.current_vocitem = self.random_tab[self.i]
        self.keyword = self.current_vocitem.keyword.to_String()

    def on_submit(self, instance):
        next_test = False

        if self.current_vocitem.is_good_translation(self.rsp_input.text):
            # Say that you win
            next_test = True
            self.nbr_succeed = self.nbr_succeed + 1
        else:
            if self.retry < self.max_retries:
                self.retry = self.retry + 1
            else:
                # Say that you fail
                # Here you have to lauch a new screen with the solution
                next_test = True

        if next_test:
            self.i = self.i + 1
            self.rsp_input.text = ""

            if self.i < len(self.random_tab):
                self.init_quizz_entry()
            else:
                sc_globals.sm.current = 'menu'
