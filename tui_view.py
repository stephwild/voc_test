import sys

from rdm.random_draw import random_draw
from parser.voc_fill import init_array


def list_handler(i, l):
    print(l[i].keyword.name)


def print_Entity(entity):

    if entity.genre is None:

        if entity.comment is None:
            print(entity.name)
        else:
            print(entity.name, '(' + entity.comment + ')')

    else:
        if entity.comment is None:
            print(entity.name, entity.genre)
        else:
            print(entity.name, entity.genre, '(' + entity.comment + ')')


def print_VocItem(item):
    print("------- CORRECTION -------")
    print("\nKeyword: ", end="")
    print_Entity(item.keyword)

    print("def_list:")

    for entity in item.def_list:
        print("\t- ", end="")
        print_Entity(entity)

    if item.description is not None:
        print("Description:", item.description)

    if item.example is not None:
        print("Example:", item.example)
    print("\n----- END CORRECTION -----")


# index of the VocItem, list of VocItem
def traduc_handler(rdm_item):
    retry = 0
    succeed_test = False
    global l

    while (retry < max_retry):
        print("\nKeyword:", rdm_item.keyword.name)
        print("Traduction: ", end="")
        sys.stdout.flush()
        response = sys.stdin.readline().strip(' \t\n')

        for definion_entity in rdm_item.def_list:

            if definion_entity.name == response:
                succeed_test = True
                break

        if succeed_test:
            global nbr_succeed
            nbr_succeed = nbr_succeed + 1
            break

        retry = retry + 1

    if succeed_test:
        print("\nWell Played Dude, you succeed this one")
    else:
        print("\nFailed !")
        print("More luck next time ! Check the response beneath:\n")
        print_VocItem(rdm_item)


nbr_succeed = 0
nbr_test = 4
max_retry = 3

# Fill the VocItem array with the specified file
l = init_array(False)

# Run the tests
print('Vocabulary test will begin !')
print('Today, there will has', str(nbr_test), 'tests')

try:
    random_list = random_draw(l, nbr_test)

    for i in range(len(random_list)):
        traduc_handler(random_list[i])

except KeyboardInterrupt as e:
    print("\n\nExiting: Application interrupted by Keyboard")
    sys.exit(0)

print("\nYour score is", str(nbr_succeed) + "/" + str(nbr_test))
