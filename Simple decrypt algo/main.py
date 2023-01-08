from collections import Counter
import string


def decrypt(test_key):
    arr = Counter(test_key)
    print(''.join(str(arr[j]) for j in string.ascii_lowercase))
    # arr = []
    # st = string.ascii_lowercase
    #
    # for i in test_key:
    #     if i in string.ascii_lowercase:
    #         arr.append(i)
    #
    # res = Counter(arr)
    #
    # for key, value in res.items():
    #     for el in st:
    #         if el == key:
    #             st = st.replace(el, str(res[key]))
    #
    # for j in st:
    #     if j in 'abcdefghijklmnopqrstuvwxyz':
    #         st = st.replace(j, '0')

    # print(st)


decrypt('$aaaa#bbb*ccfff!z')
