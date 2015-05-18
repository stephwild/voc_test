from vocitem import VocItem, pretty_print_vocitem

l = []
delim = ' - '

def fill_voc_dic(str):
    f = open(str, 'r')

    for line in f:
        item = line_handler(line)

        if item is not None:
            l.append(item)

def line_handler(line):
    l = line.split(delim)
    item = None

    if len(l) != 1:
        item = VocItem(l[0], l[1], None, None)

    return item

def init_array(need_log):
    fill_voc_dic("vocabulary")

    if need_log:
        pretty_print_vocitem(l)

    return l
