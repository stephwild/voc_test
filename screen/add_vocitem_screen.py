from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown

class CustomDropDown(DropDown):
    pass

Builder.load_file('kv/add_vocitem.kv')
Builder.load_file('kv/drop_down_genre.kv')

class Add_VocItemScreen(Screen):
    def on_add_definition(self, instance):
        print('Add def')

    def on_submit(self, instance):
        print('Submitting')
