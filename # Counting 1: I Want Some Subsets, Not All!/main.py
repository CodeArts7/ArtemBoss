import itertools


def f(n):
    arr = []
    [arr.append(i) for i in range(1, n + 1)]
    a = [",".join(map(str, comb)) for i in arr for comb in itertools.combinations(arr, i)]
    print(len(a))
    # a, b = 0, 1
    # for _ in range(n):
    #     a, b = b, a + b + 1
    # print(a)
    # arr = []
    # counter = 0
    #
    # [arr.append(i) for i in range(1, n + 1)]
    #
    # for i in range(1, len(arr) + 1):
    #     for combo in itertools.combinations(arr, i):
    #         combo = list(combo)
    #
    #         if len(combo) < 2:
    #             counter += 1
    #         else:
    #             for x in range(len(combo)):
    #                 if combo[x] - combo[x - 1] == 1:
    #                     break
    #             else:
    #                 counter += 1




f(5)
