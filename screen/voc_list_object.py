from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.listview import SelectableView

class VocListObj(BoxLayout, SelectableView):
    simple_drawn = 0
    detailed_drawn = 1
    _debug = True

    def __init__(self, **kwargs):
        self.voc_item = kwargs.pop('voc_item', None) # default value: None
        is_selected = False

        if self._debug:
            if self.voc_item is None:
                print('None')
            else:
                print(self.voc_item.get_keyword())

        kwargs['orientation'] = 'vertical'
        super(VocListObj, self).__init__(**kwargs)

        self.draw(self.simple_drawn)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.adapter.handle_selection(self)
            return True

        return super(VocListObj, self).on_touch_up(touch)

    def select(self, *args):
        self.draw(VocListObj.detailed_drawn)
        super(VocListObj, self).select(*args)

        if self._debug:
            print(repr(self))

    def deselect(self, *args):
        self.draw(VocListObj.simple_drawn)
        super(VocListObj, self).deselect(*args)

        if self._debug:
            print(repr(self))

    def draw(self, detail):
        self.clear_widgets()
        self.add_widget(MainVocInfo(self.voc_item))

        if detail == self.detailed_drawn:
            if self.voc_item.description is not None:
                self.add_widget(Label(text='Description: '
                    + self.voc_item.description, halign='left',
                    text_size=(3 * self.width / 4, None)))

            if self.voc_item.example is not None:
                self.add_widget(Label(text='Example: '
                    + self.voc_item.example, halign='left',
                    text_size=(3 * self.width / 4, None)))

    # To debug select behavior
    def __repr__(self):
        if self.is_selected:
            str_select = 'selected'
        else:
            str_select = 'deselected'

        return 'Object: ' + str(VocListObj) + ', keyword: ' \
            + self.voc_item.get_keyword() + ', State: ' + str_select

class MainVocInfo(BoxLayout):

    def __init__(self, voc_item, **kwargs):
        self.voc_item = voc_item

        kwargs['orientation'] = 'horizontal'
        super(MainVocInfo, self).__init__(**kwargs)

        self.draw()

    def draw(self):
        self.clear_widgets()

        label = Label(text=self.voc_item.get_keyword(),
            halign='left')

        self.add_widget(label)
        label.text_size = (2 * label.width, None)

        def_str = ''

        for i_def in self.voc_item.def_list:
            if def_str == '':
                def_str += i_def.to_String()
            else:
                def_str += ', ' + i_def.to_String()

        label = Label(text=def_str, halign='left')

        self.add_widget(label)
        label.text_size = (2 * label.width, None)
