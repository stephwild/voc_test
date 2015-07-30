def update_voc_file(voc_file, item):

    # Permit auto closing in exception
    with open(voc_file, 'a') as f:
        key_entity = item.keyword
        f.write(item.keyword.to_String() + ' - ')

        f.write(item.def_list[0].to_String())

        for i in range(1, len(item.def_list)):
            if i == 6:
                sep = ',\n '
            else:
                sep = ', '

            f.write(sep + item.def_list[i].to_String())

        if item.description is not None:
            f.write('\n\tDesc: ' + item.description)

        if item.description is not None:
            f.write('\n\tEx: ' + item.example)

        f.write('\n')
