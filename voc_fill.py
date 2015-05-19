from vocitem import VocEntity, VocItem, pretty_print_vocitem, pretty_print_entity


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
    l = line.split(delim, 1)  # split main word from the traduc_list
    item = None

    item = VocItem(entity_parser(l[0])) # init VocItem with main word

    # for each traduction in traduc_list
    # split function do not remove excess spaces
    for str_entity in l[1].split(','):

        str_entity.strip(' \n\t')  # Remove excess space in traduc entity

        lol = entity_parser(str_entity)
        item.add_translation_entity(lol) # add traduc

    return item


def desc_parser(item, desc):
    item.set_description(desc.split(desc_token, 1)[1])
    return item


def ex_parser(item, examples):
    item.set_example(examples.split(ex_token, 1)[1])
    return item


# In this function, you have always a main name
def entity_parser(str_entity):
    l = str_entity.split(' ', 2)

    entity = VocEntity(l[0], None, None)

    # In this if statement, you can have optionally a genre and description
    # attribute
    if len(l) > 1:
        if l[1] == '[': # this block contain a genre attribute

            if len(l) > 2:
                entity = VocEntity(l[0], l[1], l[2].strip('()'))
            else:
                entity = VocEntity(l[0], l[1], None) # Only genre (with braces)

        else:
            # Only desc attribute (surround by parenthesis)
            entity = VocEntity(l[0], None, l[1].strip('()'))

    pretty_print_entity(entity)

    return entity


def init_array(need_log):
    l = fill_voc_dic("vocabulary")

    if need_log:
        pretty_print_vocitem(l)

    return l
