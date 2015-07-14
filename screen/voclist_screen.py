from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import SelectableView, ListItemButton

import gui_view as GLOBAL_

Builder.load_file('kv/voclist.kv')

class SelectableLabel(SelectableView, Label):
    def __init__(self, **kwargs):
        super(Label, self).__init__(**kwargs)
        super(SelectableView, self).__init__(**kwargs)

class VocListScreen(Screen):

    def make_layout(self):
        args_converter = lambda row_index, voc_item: {'text': voc_item.get_keyword()
                + " " + voc_item.def_list[0].to_String()}

        list_adapter = ListAdapter(data=GLOBAL_.voc_array,
                                    args_converter=args_converter,
                                    cls=SelectableLabel,
                                    selection_mode='single',
                                    allow_empty_selection=True)

        self.ids.label_list.adapter = list_adapter
