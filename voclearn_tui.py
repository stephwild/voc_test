from random_draw import random_draw
from voc_fill import init_array


def simple_handler(i, l):
    print(l[i].keyword.name)

l = init_array(False)
random_draw(l, simple_handler, 4)
