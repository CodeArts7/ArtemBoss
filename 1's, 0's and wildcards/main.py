def possibilities(param):
    # temp = []
    # if '?' in param:
    #     first = param.replace('?', '0', 1)
    #     second = param.replace('?', '1', 1)
    #
    #     if '?' not in first and second:
    #         temp.append(first)
    #         temp.append(second)
    #     else:
    #         possibilities(first)
    #         possibilities(second)

    if '?' not in param:
        print(param)
    else:
        first = param.replace('?', '0', 1)
        second = param.replace('?', '1', 1)

        possibilities(first)
        possibilities(second)








possibilities('10??')
