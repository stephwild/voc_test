from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.adapters.listadapter import ListAdapter
from screen.voc_list_object import VocListObj

import gui_view as GLOBAL_

Builder.load_file('kv/voclist.kv')

class VocListScreen(Screen):

    def make_layout(self):
        args_voc_convert = lambda row_index, voc_item: \
            {'voc_item': voc_item,
            'size_hint_y': None}

        list_adapter = ListAdapter(data=GLOBAL_.voc_array,
                                    args_converter=args_voc_convert,
                                    cls=VocListObj,
                                    selection_mode='multiple',
                                    allow_empty_selection=True)

        # self.ids permits to get id from kv files
        self.ids.label_list.adapter = list_adapter
