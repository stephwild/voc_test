from vocitem import VocEntity, VocItem
from pretty_print import pretty_print_entity, pretty_print_list_vocitem


# Define value
delim = ' - '
desc_token = '\tDesc: '
ex_token = '\tEx: '

def fill_voc_dic(path):
    f = open(path, 'r')

    str_item = ""
    item = None
    l = []

    # Divide the f file content into block with each
    # correspond to only one VocItem
    for line in f:

        if line[0] == ' ' or line[0] == '\t':
            str_item += line
        else:
            if str_item != "":
                item = block_parser(str_item)

            if item is not None:
                l.append(item)

            str_item = line

    return l


# This function convert the block to a VocItem.
# But, there must only have one block.
# No error checking for that type of error will be found here
# Check, fill_voc_dic for these errors checking
def block_parser(str_item):

    tab_item = str_item.split(desc_token, 1)
    desc_attr = False

    if len(tab_item) > 1:
        tmp = tab_item.pop()  # Contain at least 'Desc' (and maybe 'Ex' part)
        desc_attr = True # There is a description part in this block

        for i in tmp.split(ex_token, 1):  # tmp[0]: Desc, (tmp[1]: Ex)
            tab_item.append(i)
    else:
        tab_item = str_item.split(ex_token, 1)

    # main part must be present in a block !
    item = main_parser(tab_item[0])

    if len(tab_item) > 1:
        if desc_attr:
            item = desc_parser(item, tab_item[1])
        else:
            # As main part must be present and description part is not
            # the remaining is example part
            item = ex_parser(item, tab_item[1])

    # Desc part is only before ex part so the only configuration possible is
    # 0: main_part, 1: desc_part, 2: ex_part
    if len(tab_item) > 2:
        item = ex_parser(item, tab_item[2])

    return item


# This parser parse only main part
# desc and ex part have already been parse before
# No error checking for these parts
def main_parser(line):
    # Delimitor must be present !
    # Action: Split up 'keyword' and 'traduc_list' from main_line
    l = line.split(delim, 1)

    # len(l) = 2 because because previous split must succeed !
    # Action: Init VocItem with keyword
    item = VocItem(entity_parser(l[0], False))

    # for each traduction in traduc_list
    # split function do not remove excess spaces
    for str_entity in l[1].split(','):

        str_entity = str_entity.strip(' \n\t')

        # Add definition to item definition list
        item.add_translation_entity(entity_parser(str_entity, False))

    return item


# Token already parse
def desc_parser(item, desc):
    item.set_description(desc)
    return item


# Token already parse
def ex_parser(item, examples):
    item.set_example(examples)
    return item


# In this function, you have always a keyword
# This function parse only the entity:
#   -> the entity must be passed to the function correctly
#   -> No error handling !
#
# Form: keyword (\[genre\] [\(comment\)])
def entity_parser(str_entity, debug):

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

    if debug:
        pretty_print_entity("Entity", entity)

    return entity


def init_array(need_log):
    l = fill_voc_dic("vocabulary")

    if need_log:
        pretty_print_list_vocitem(l)

    return l
