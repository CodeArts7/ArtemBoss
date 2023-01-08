def sort_array(source_array):
    odd = []
    odd_counter = 0

    for i in source_array:
        if i % 2 != 0:
            odd.append(i)
    odd = sorted(odd)

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd[odd_counter]
            odd_counter += 1

    return source_array


sort_array([5, 3, 1, 8, 0])
