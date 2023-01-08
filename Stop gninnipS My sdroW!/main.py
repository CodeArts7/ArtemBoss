def spin_words(sentence):
    sen = sentence.split()
    new_sen = ''

    for i in sen:
        if len(i) >= 5:
            i = i[::-1]
            new_sen += i + ' '
        else:
            new_sen += i + ' '

    print(new_sen.rstrip())




spin_words("CodeWars")