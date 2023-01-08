def tops(msg):
    first_top, first_top_plus_one, result_tops = 1, 5, ''

    while first_top < len(msg):
        result_tops += msg[first_top]
        first_top += first_top_plus_one
        first_top_plus_one += 4
    print(result_tops[::-1])










tops('abcdefghijklmnopqrstuvwxyz12345')
