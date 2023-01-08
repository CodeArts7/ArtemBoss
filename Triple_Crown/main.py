def triple_crown(receivers):
    first = []
    second = []
    third = []

    for values in receivers['Cooper Kupp'].values():
        first.append(values)
    for values2 in receivers['Justin Jefferson'].values():
        second.append(values2)
    for values3 in receivers['Davante Adams'].values():
        third.append(values3)

    if first[0] > second[0] and first[0] > third[0] and first[1] > second[1] and first[1] > third[1] and first[2] > second[2] and first[2] > third[2]:
        return 'Cooper Kupp'
    elif second[0] > first[0] and second[0] > third[0] and second[1] > first[1] and second[1] > third[1] and second[2] > first[2] and second[2] > third[2]:
        return 'Justin Jefferson'
    elif third[0] > first[0] and third[0] > second[0] and third[1] > first[1] and third[1] > second[1] and third[2] > first[2] and third[2] > second[2]:
        return 'Davante Adams'
    else:
        return 'None of them'


triple_crown({'Cooper Kupp': {'Receiving yards': 1700, 'Receiving touchdowns': 18, 'Receptions': 117},
                                         'Justin Jefferson': {'Receiving yards':1650, 'Receiving touchdowns': 17, 'Receptions': 115},
                                        'Davante Adams':{'Receiving yards': 1750, 'Receiving touchdowns': 16, 'Receptions': 113}})
