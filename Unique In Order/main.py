import itertools


def unique_in_order(iterable):
    return [i for i, _ in itertools.groupby(iterable)]


unique_in_order(('AAAABBBCCDAABBB'))