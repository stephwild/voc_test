# from vocitem.py import VocItem
import os
import sys
import random

def random_draw(l, func_ptr, treshold):

    if len(l) < treshold:
        os.write(sys.stderr, 'Fatal error in random_draw: threshold too large')

    draw_list = []
    tmp = list(range(len(l)))

    for i in range(treshold):
        drawn = random.choice(tmp)
        tmp.remove(drawn)             # No duplicate item like set
        draw_list.append(drawn)

    for i in range(len(draw_list)):
        func_ptr(draw_list[i], l)
