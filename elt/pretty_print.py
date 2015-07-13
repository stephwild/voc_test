# Pretty print function for voc_test base object
# ##############################################

def pretty_print_entity(entity, heading='Entity'):
    print(heading, " -> n:", entity.name, ", g:",
            entity.genre, ", c:", entity.comment, sep='')


def pretty_print_vocitem(item):

    if item is None:
        print("VocItem is NULL")
        return

    # There must have at least a keyword and a def_list (with a least one elt)
    pretty_print_entity(item.keyword, "Keyword")

    # def_list must contain at least one elt
    print("Definition List:")

    count = 0

    for entity in item.def_list:
        pretty_print_entity(entity, "\t- Def Entity " + str(count))
        count = count + 1

    if item.description is None:
        print("Description: No description is set")
    else:
        print("Description:", item.description)

    if item.example is None:
        print("Example: No examples are set")
    else:
        print("Example:", item.example)

def pretty_print_list_vocitem(l):
    if l is None:
        print("List is NULL")
        return

    for i in l:
        pretty_print_vocitem(i)
        print("") # linebreak
