from kivy.app import App

import screen.sc_globals as SC_globals

class VocApp(App):
    def build(self):
        # Jump to MenuScreen (first screen of sm [Screen Manager])
        return SC_globals.sm

if __name__ == '__main__':
    # Init Screen Manager
    SC_globals.init_sm()

    VocApp().run()
