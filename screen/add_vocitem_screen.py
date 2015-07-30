from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.uix.button import Button

import elt.vocitem as Item
import gui_view as GLOBAL_
import screen.sc_globals as SC_globals
import update.voc_update as Update

class CustomDropDown(DropDown):
    pass

Builder.load_file('kv/add_vocitem.kv')
Builder.load_file('kv/drop_down_genre.kv')

class Add_VocItemScreen(Screen):
    key_main = ObjectProperty(None)
    key_genre = ObjectProperty(None)
    key_comment = ObjectProperty(None)

    def_main = ObjectProperty(None)
    def_genre = ObjectProperty(None)
    def_comment = ObjectProperty(None)

    desc_input = ObjectProperty(None)
    ex_input = ObjectProperty(None)

    stack_layout = ObjectProperty(None)

    _debug = False

    def __init__(self, **kwargs):
        self.definition_added = []
        super().__init__(**kwargs)

    def _strip_str(self, s):
        return s.strip(' \n\t')

    def _get_entity(self, main_text, genre_text, comment_text):
        main = self._strip_str(main_text)
        genre = self._strip_str(genre_text)
        comment = self._strip_str(comment_text)

        if main == '':
            print('[DEBUG] Error main entity part not added')
            return None

        if genre == '-':
            genre = None

        if comment == '':
            comment = None

        return (main, genre, comment)

    def btn_release(self, btn, entity):
        self.stack_layout.remove_widget(btn)
        self.definition_added.remove(entity)

    def on_add_definition(self, instance):
        print('Add def')

        def_tuple = self._get_entity(self.def_main.text, self.def_genre.text,
            self.def_comment.text)

        if def_tuple is None:
            return

        entity = Item.VocEntity(def_tuple[0], def_tuple[1],
            def_tuple[2])

        self.definition_added.append(entity)

        button = Button(text=entity.name, size_hint=(None, 1.))

        button.text_size[0] = len(entity.name) * 8
        button.texture_size[0] = button.text_size[0]
        button.width = button.texture_size[0]
        button.halign = 'center'

        button.on_release = lambda: self.btn_release(button, entity)

        if self._debug:
            print('button texture_size:', button.texture_size)
            print('button text_size:', button.text_size)

        self.stack_layout.add_widget(button)

    def on_submit(self, instance):
        key_tuple = self._get_entity(self.key_main.text, self.key_genre.text,
            self.key_comment.text)

        if key_tuple is None:
            return

        entity = Item.VocEntity(key_tuple[0], key_tuple[1], key_tuple[2])
        vocitem = Item.VocItem(entity)

        for def_entity in self.definition_added:
            vocitem.add_translation_entity(def_entity)

        if self._strip_str(self.desc_input.text) != '':
            vocitem.description = self.desc_input.text

        if self._strip_str(self.ex_input.text) != '':
            vocitem.example = self.ex_input.text

        GLOBAL_.voc_array.append(vocitem)
        SC_globals.sm.get_screen('voclist').add_item(vocitem)
        Update.update_voc_file('vocabulary', vocitem)
