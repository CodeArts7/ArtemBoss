from collections import Counter


def scramble(s1, s2):
    s1 = Counter(s1)
    s2 = Counter(s2)

    return all(i in s1 and s1[i] >= s2[i] for i in s2)
    # return len(Counter(s2) - Counter(s1)) == 0)


scramble('cedewaraaossoqqyt', 'codewars')
