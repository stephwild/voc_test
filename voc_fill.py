from vocitem import VocEntity, VocItem
from vocitem import pretty_print_vocitem, pretty_print_entity


# Define value
delim = ' - '
desc_token = '\tDesc: '
ex_token = '\tEx: '

def fill_voc_dic(path):
    f = open(path, 'r')

    str_item = ""
    item = None
    l = []

    for line in f:

        if line[0] == ' ' or line[0] == '\t':
            str_item += line
        else:
            item = block_parser(str_item)

            if item is not None:
                l.append(item)

            str_item = line

    return l


def block_parser(str_item):
    if str_item == "":
        return

    tab_item = str_item.split(desc_token, 1)

    if len(tab_item) > 1:
        tmp = tab_item.pop()  # Contain 'Desc' and 'Ex' part

        for i in tmp.split(ex_token, 1):  # list[0]: Desc, list[1]: Ex
            tab_item.append(i)

    # Now tab_item[0] = main_words, tab_item[1]: Desc, tab_item[2]: Ex
    item = main_parser(tab_item[0])

    if len(tab_item) > 1:
        item = desc_parser(tab_item[1]) # Todo: Not necesserely description

    if len(tab_item) > 2:
        item = ex_parser(tab_item[2])

    return item


def main_parser(line):
    # Delimitor must be present !
    # Action: Split up keyword and traduc_list from main_line
    l = line.split(delim, 1)

    # len(l) = 2 because because previous split must succeed !
    # Action: Init VocItem with keyword
    item = VocItem(entity_parser(l[0]))

    # for each traduction in traduc_list
    # split function do not remove excess spaces
    for str_entity in l[1].split(','):

        # Remove excess space in traduc entity
        str_entity = str_entity.strip(' \n\t')

        lol = entity_parser(str_entity)
        item.add_translation_entity(lol) # add traduc

    return item


def desc_parser(item, desc):
    item.set_description(desc.split(desc_token, 1)[1])
    return item


def ex_parser(item, examples):
    item.set_example(examples.split(ex_token, 1)[1])
    return item


# In this function, you have always a keyword
# This function parse only the entity:
#   -> the entity must be passed to the function correctly
#   -> No error handling !
def entity_parser(str_entity):

    genre_attr = False
    desc_attr = False

    l = str_entity.split(' [', 1) # Try to parse genre attribute

    if len(l) > 1:
        genre_attr = True # Genre attribute present

    base = l[len(l) - 1] # last elt of l

    l2 = base.split(' (', 1) # Try to parse desc attribute

    if len(l2) > 1:
        desc_attr = True # Desc attribute present

    # genre success:
    #   -> l have 'name' and 'genre&!desc' -- l2 have 'genre' (and 'desc')
    #
    # genre fail: l have 'name&!desc' -- l2 have 'name' (and 'desc')
    if (genre_attr):
        if (desc_attr):
            entity = VocEntity(l[0], '[' + l2[0], l2[1].rstrip(')'))
        else:
            entity = VocEntity(l[0], '[' + l2[0], None)
    else:
        if (desc_attr):
            entity = VocEntity(l2[0], None, l2[1].rstrip(')'))
        else:
            entity = VocEntity(l[0], None, None)

    pretty_print_entity(entity)

    return entity


def init_array(need_log):
    l = fill_voc_dic("vocabulary")

    if need_log:
        pretty_print_vocitem(l)

    return l
