from vocitem import VocItem, pretty_print_vocitem

l = []
delim = ' - '

def fill_voc_dic(str):
    f = open(str, 'r')

    str_item = ""
    item = None

    for line in f:

        if line[0] == ' ' or line[0] == '\t':
            str_item += line
        else:
            item = block_handler(str_item)

            if item is not None:
                l.append(item)

            str_item = line


def block_handler(str_item):
    if str_item == "":
        return

    tab_item = str_item.split('\tDesc: ', 1)

    if len(tab_item) > 1:
        tmp = tab_item.pop()  # Contain 'Desc' and 'Ex' part

        for i in tmp.split('\tEx: ', 1):  # list[0]: Desc, list[1]: Ex
            tab_item.append(i)

    # Now tab_item[0] = main_words, tab_item[1]: Desc, tab_item[2]: Ex
    item = line_handler(tab_item[0])

    if len(tab_item) > 1:
        item = desc_handler(tab_item[1])

    if len(tab_item) > 2:
        item = ex_handler(tab_item[2])

    return item


def line_handler(line):
    l = line.split(delim)
    item = None

    if len(l) != 1:
        item = VocItem(l[0], l[1])

    return item


def desc_handler(item, desc):
    item.set_description(desc.split('\tDesc: ', 1)[1])
    return item


def ex_handler(item, examples):
    item.set_example(examples.split('\tEx: ', 1)[1])
    return item


def init_array(need_log):
    fill_voc_dic("vocabulary")

    if need_log:
        pretty_print_vocitem(l)

    return l
