class VocEntity:
    def __init__(self, name: str, genre: str, comment: str):
        self.name = name
        self.genre = genre
        self.comment = comment


class VocItem:
    def_list = None
    description = None
    example = None

    def __init__(self, entity: VocEntity):
        self.word = entity

    def add_translation(self, name: str, genre: str, comment: str):
        voc_entity = VocEntity(name, genre, comment)
        self.def_list.append(voc_entity)

    def add_translation_entity(self, entity: VocEntity):
        self.def_list.append(entity)

    def set_description(self, description: str):
        self.description = description

    def set_example(self, example: str):
        self.example = example


def pretty_print_vocitem(l: list):
    for i in range(len(l)):
        print("En: " + l[i].word.name, end=" ---- ")
        print("list: ")

        for i in l[i].def_list:
            print(i.name + ' - ')
