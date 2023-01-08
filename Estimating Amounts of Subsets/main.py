import itertools
import math


def est_subsets(a):
    print(2**len(set(a)) - 1)
    # counter = 0
    #
    # a = list(set(a))
    #
    # for i in range(1, len(a) + 1):
    #     for combo in itertools.combinations(a, i):
    #         counter += 1
    # p = itertools.chain.from_iterable(itertools.combinations(a, r)for r in range(1, len(a) + 1))

    # for b in p:
    #     counter += 1

    # print(counter)


est_subsets(['a', 'z', 'z', 'z', 'b', 'j', 'f', 'k', 'b',
        'd', 'j', 'j', 'n', 'm', 'm'])
