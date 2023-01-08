def pyramid(num):
    lst = []
    x = [1]
    counter = 0

    for i in range(num + 1):
        lst.append(x * counter)

        counter += 1
    lst.pop(0)
    print(lst)


pyramid(2)
