def likes(names):
    if len(names) == 1:
        return f'{names[0]} likes this'

    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'

    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'

    elif len(names) > 3:
        amount = len(names) - 2
        return f'{names[0]}, {names[1]} and {amount} others like this'


likes(['Alex', 'Jacob', 'Mark', 'Max'])