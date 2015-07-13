class VocEntity:
    def __init__(self, name, genre, comment):
        self.name = name
        self.genre = genre
        self.comment = comment

    def to_String(self):
        if self.genre is None and self.comment is None:
            return self.name
        elif self.genre is None:
            return self.name + " (" + self.comment + ")"
        elif self.comment is None:
            return self.name + " [" + self.genre + "]"

        return self.name + " [" + self.genre + "] " + "(" + self.comment + ")"


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

    def get_keyword(self):
        return self.keyword.to_String()

    def get_description(self):
        return self.description

    def get_example(self):
        return self.example

    def nbr_traduction(self):
        return len(self.def_list)

    def is_good_translation(self, response):
        for definion_entity in self.def_list:
            if definion_entity.name == response:
                return True

        return False
