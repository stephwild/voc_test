from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from . import sc_globals

from rdm.random_draw import random_draw
import gui_view as GLOBAL_


Builder.load_file('kv/quizz.kv')


class QuizzScreen(Screen):
    keyword = StringProperty()
    nbr_succeed = NumericProperty(0)
    nbr_test = GLOBAL_.nbr_test
    rsp_input = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(QuizzScreen, self).__init__(**kwargs)

    def init_quizz_globaly(self):
        self.i = 0
        self.nbr_succeed = 0
        self.random_tab = random_draw(GLOBAL_.voc_array, GLOBAL_.nbr_test)

    def init_quizz_entry(self):
        self.retry = 0
        self.current_vocitem = self.random_tab[self.i]
        self.keyword = self.current_vocitem.keyword.to_String()

    def on_submit(self, instance):
        next_test = False
        self.retry += 1

        if self.current_vocitem.is_good_translation(self.rsp_input.text):
            # Say that you win
            next_test = True
            self.nbr_succeed += 1

        elif self.retry >= GLOBAL_.max_retries:
            # You Failed...
            # TODO: Here, Lauch a new screen with the solution
            next_test = True

        if next_test:
            self.i += 1
            self.rsp_input.text = ""

            if self.i < len(self.random_tab):
                self.init_quizz_entry()
            else:
                sc_globals.sm.current = 'menu'
