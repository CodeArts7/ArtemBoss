def solution(n):
    result = ''

    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]

    if n >= 1000:
        thousand = m[n // 1000]
        hundred = c[(n % 1000) // 100]
        ten = x[(n % 100) // 10]
        one = i[n % 10]
        result = (thousand + hundred + ten + one)
    elif 100 < n < 1000:
        hundred = c[(n % 1000) // 100]
        ten = x[(n % 100) // 10]
        one = i[n % 10]
        result = (hundred + ten + one)
    elif 10 < n < 100:
        ten = x[(n % 100) // 10]
        one = i[n % 10]
        result = (ten + one)
    elif n < 10:
        one = i[n % 10]
        result = one

    res = result.replace(' ', '')
    print(res)


solution(1000)
