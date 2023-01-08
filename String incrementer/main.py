import re
from string import ascii_lowercase


def increment_string(strng):
    if strng == '':
        return str(1)
    elif strng[-1] in ascii_lowercase:
        return strng + '1'
    else:
        ends = re.compile(r'[0-9]+$')
        return re.sub(ends, lambda x: f"{str(int(x.group()) + 1).zfill(len(x.group()))}", strng)


print(increment_string('foo'))




