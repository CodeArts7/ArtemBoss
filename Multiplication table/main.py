def multiplication_table(size):
    res = []
    p_res = []
    for i in range(1, size + 1):
        for j in range(i, i * size + 1, i):
            res.append(j)
        p_res.append(res)
    f_res = p_res[0]
    print([f_res[i:i + size] for i in range(0, len(f_res), size)])


multiplication_table(3)
