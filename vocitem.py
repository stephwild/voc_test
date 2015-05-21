class VocEntity:
    def __init__(self, name, genre, comment):
        self.name = name
        self.genre = genre
        self.comment = comment


class VocItem:
    def __init__(self, entity):
        self.keyword = entity
        self.def_list = []
        self.description = None
        self.example = None

    def add_translation(self, name, genre, comment):
        voc_entity = VocEntity(name, genre, comment)
        self.def_list.append(voc_entity)

    def add_translation_entity(self, entity):
        self.def_list.append(entity)

    def set_description(self, description):
        self.description = description

    def set_example(self, example):
        self.example = example
