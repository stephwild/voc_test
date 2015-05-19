class VocEntity:
    def __init__(self, name, genre, comment):
        self.name = name
        self.genre = genre
        self.comment = comment


class VocItem:
    def_list = []
    description = None
    example = None

    def __init__(self, entity):
        self.keyword = entity

    def add_translation(self, name, genre, comment):
        voc_entity = VocEntity(name, genre, comment)
        self.def_list.append(voc_entity)

    def add_translation_entity(self, entity):
        self.def_list.append(entity)

    def set_description(self, description):
        self.description = description

    def set_example(self, example):
        self.example = example

def pretty_print_entity(entity):
    print("Entity -> n: ", entity.name, ",g: ", entity.genre, ", c: ", entity.comment)

def pretty_print_vocitem(item):

    if item is None:
        print("VocItem is equal to None")
        return

    print("En: " + item.keyword.name)
    print("list: ")

    for i in item.def_list:
        print(i.name + ' --- ')

    if item.description is None:
        desc = "None"
    else:
        desc = item.description

    print("\nDesc: " + desc)

    if item.example is None:
        example = None
    else:
        example = item.example

    print("\nEx: " + example)
