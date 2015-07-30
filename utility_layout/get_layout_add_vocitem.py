# Constant
window_hpad = 2
window_vpad = 5

x_spacing = 2
y_spacing = 2

default_size_y = 5
default_label_size_x = 10
default_comment_size_y = 10
default_desc_ex_size = 10

size_button = (30, default_size_y)

def str_elt(name, x, top, size, x_str='x', y_str='top'):
    return name + ':\n\t{\'' + x_str + '\': ' + str(x / 100) + ', \'' + y_str \
        + '\': ' + str(top / 100) + '}\n\tsize: ' + str(size[0] / 100) \
        + ', ' + str(size[1] / 100)

class Elt:
    def __init__(self, name, pos_x=None, pos_y=None, size_x=None,
            size_y=default_size_y):
        self.name = name
        self.pos = (pos_x, pos_y)
        self.size = (size_x, size_y)

    def after_x(self):
        return self.pos[0] + self.size[0] + x_spacing

    def after_y(self):
        return self.pos[1] - self.size[1] - y_spacing

    def __str__(self):
        return str_elt(self.name, self.pos[0], self.pos[1], self.size)

class Item:
    def __init__(self, name):
        self.name = name

    label = Elt('Label', size_x=default_label_size_x)
    main = Elt('Main')
    genre = Elt('Genre', size_x=default_size_y)
    comment = Elt('Comment', size_y=default_comment_size_y)

    def print(self):
        print('========================')
        print('Item Name: ' + self.name)
        print('========================\n')
        print(str(self.label))
        print(str(self.main))
        print(str(self.genre))
        print(str(self.comment))


keyword = Item('Keyword')
def_list = Item('Def_list')

# Position are relative from top and x
keyword.label.pos = (window_hpad, 100 - window_vpad)

keyword.genre.pos = (keyword.label.after_x(), keyword.label.pos[1])

keyword.main.pos = (keyword.genre.after_x(), keyword.label.pos[1])
keyword.main.size = (100 - keyword.genre.after_x() - window_hpad,
    keyword.main.size[1])

keyword.comment.pos = (keyword.label.after_x(), keyword.label.after_y())
keyword.comment.size = (100 - keyword.label.after_x() - window_hpad,
    keyword.comment.size[1])

keyword.print()
print()

stack_layout_pos = (window_hpad, keyword.comment.after_y())
stack_layout_size = size_button

print(str_elt('Stack Layout', stack_layout_pos[0], stack_layout_pos[1],
    stack_layout_size) + '\n')

def_list.label.pos = (window_hpad, stack_layout_pos[1] - stack_layout_size[1]
        - y_spacing)

def_list.genre.pos = (def_list.label.after_x(), def_list.label.pos[1])

def_list.main.pos = (def_list.genre.after_x(), def_list.label.pos[1])
def_list.main.size = (100 - def_list.genre.after_x() - window_hpad,
    def_list.main.size[1])

def_list.comment.pos = (def_list.label.after_x(), def_list.label.after_y())
def_list.comment.size = (100 - def_list.label.after_x() - window_hpad,
    def_list.comment.size[1])

def_list.print()
print()

add_button_pos = (def_list.comment.pos[0], def_list.comment.after_y())

desc_label_pos = (window_hpad, add_button_pos[1] - size_button[1] - y_spacing -
        5)
desc_label_sz = (default_label_size_x, default_size_y)

desc_txtipt_pos = (desc_label_pos[0] + desc_label_sz[0] + x_spacing,
    desc_label_pos[1])
desc_txtipt_sz = (100 - desc_txtipt_pos[0] - x_spacing, default_desc_ex_size)

ex_label_pos = (window_hpad, desc_txtipt_pos[1] - desc_txtipt_sz[1]
    - y_spacing)
ex_label_sz = (default_label_size_x, default_size_y)

ex_txtipt_pos = (ex_label_pos[0] + ex_label_sz[0] + x_spacing, ex_label_pos[1])
ex_txtipt_sz = (100 - desc_txtipt_pos[0] - x_spacing, default_desc_ex_size)

print(str_elt('Add Button', add_button_pos[0], add_button_pos[1], size_button))
print()

print(str_elt('Desc Label', desc_label_pos[0], desc_label_pos[1],
    desc_label_sz))
print()

print(str_elt('Desc Text Input', desc_txtipt_pos[0], desc_txtipt_pos[1],
    desc_txtipt_sz))
print()

print(str_elt('Ex Label', ex_label_pos[0], ex_label_pos[1], ex_label_sz))
print()

print(str_elt('Ex Text Input', ex_txtipt_pos[0], ex_txtipt_pos[1],
    ex_txtipt_sz))
print()

# Submit in bottom-center of screen
print(str_elt('Submit Button', 50, window_vpad, size_button, x_str='center_x',
    y_str='y'))
