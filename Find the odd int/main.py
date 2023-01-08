from collections import Counter


def find_it(seq):
    s = Counter(seq)
    print(s)

    for x in s.items():
        print(x)
        if x[1] % 2 != 0:
            print(x[0])


find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1])
