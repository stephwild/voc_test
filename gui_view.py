from kivy.app import App
from kivy.core.window import Window

import screen.sc_globals as SC_globals
from parser.voc_fill import init_array


voc_array = init_array(False)
max_retries = 4
nbr_test = 4


class VocApp(App):
    def build(self):
        # Handle back/Esc Button
        Window.bind(on_keyboard=SC_globals.on_back_btn)

        # Jump to MenuScreen (first screen of sm [Screen Manager])
        return SC_globals.sm


if __name__ == '__main__':
    # Init Screen Manager
    SC_globals.init_sm()

    VocApp().run()
