from kivy.uix.screenmanager import ScreenManager


# Init the Screen Manager
def init_sm():
    from .menu_screen import MenuScreen
    from .quizz_screen import QuizzScreen
    from .voclist_screen import VocListScreen
    from .add_vocitem_screen import Add_VocItemScreen
    from .settings_screen import SettingsScreen

    global sm
    sm = ScreenManager()

    sm.add_widget(MenuScreen(name='menu'))
    sm.add_widget(QuizzScreen(name='quizz'))
    sm.add_widget(VocListScreen(name='voclist'))
    sm.add_widget(Add_VocItemScreen(name='add_vocitem'))
    sm.add_widget(SettingsScreen(name='settings'))

def on_back_btn(window, key, *args):
    # if it's Back/Esc key
    if key == 27:
        if sm.current != 'menu':
            sm.current = 'menu'
            return True

    # Let kivy handle this event
    return False
