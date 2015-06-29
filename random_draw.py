# from vocitem.py import VocItem
import os
import sys
import random

def random_draw(l, treshold):

    if len(l) < treshold:
        os.write(sys.stderr, 'Fatal error in random_draw: threshold too large')

    draw_list = []
    tmp = list(range(len(l)))

    for i in range(treshold):
        drawn = random.choice(tmp)
        tmp.remove(drawn)             # No duplicate item like set
        draw_list.append(l[drawn])

    return draw_list
