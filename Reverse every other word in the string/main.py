def reverse_alternate(string):
    # if len(string) >= 1 and string != '':
    #     string = string.split(' ')
    #     for i in range(1, len(string), 2):
    #         string[i] = string[i][::-1]
    # else:
    #     print('')
    #
    # string = ' '.join(map(str, string)).rstrip().replace('   ', '')
    # print(string)

    words = string.split()
    words[1::2] = [word[::-1] for word in words[1::2]]
    print(' '.join(words))


reverse_alternate("This is a test")
