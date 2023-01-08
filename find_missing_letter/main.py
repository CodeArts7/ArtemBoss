from urllib3.connectionpool import xrange


def find_missing_letter(chars):
    arr = []
    for j in chars:
        asci_num = ord(j)
        arr.append(asci_num)
    losted_number = sum(xrange(arr[0], arr[-1] + 1)) - sum(arr)
    result = chr(losted_number)
    print(result)


find_missing_letter(['O','Q','R','S'])


