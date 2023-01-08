# import random
# import string
#
#
# class Url_shortener:
#
#     url_array = {}
#     short_url = ''
#     beg = 'short.ly/'
#
#     def shorten(self, long_url):
#
#         letters = string.ascii_lowercase
#         random_string = ''.join(random.choice(letters) for i in range(8))
#         random_string_two = ''.join(random.choice(letters) for i in range(3))
#         random_string_three = ''.join(random.choice(letters) for i in range(3))
#         self.short_url = self.beg + random_string + '/' + random_string_two + '.' + random_string_three
#
#         if self.short_url in self.url_array:
#             self.short_url[10:12] = ''.join(random.choice(letters) for i in range(2))
#
#         self.url_array[long_url] = self.short_url
#         return self.url_array
#
#     def redirect(self):
#
#         for key, value in self.url_array.items():
#             if value == value:
#                 return key
#
#
# Url_shortener().shorten('https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e')
# Url_shortener().redirect()


from itertools import product
from string import ascii_lowercase


def short_url_generator():
    for l in range(1, 5):
        for p in product(ascii_lowercase, repeat=l):
            yield 'short.ly/' + ''.join(p)


class UrlShortener:

    short_urls = short_url_generator()
    long_to_short = {}
    short_to_long = {}

    @classmethod
    # Если исходный url уже есть в БД, то меняем его на новый
    def shorten(cls, long_url):
        if long_url in cls.long_to_short:
            return cls.long_to_short[long_url]
        # Чтобы короткие url не повторялись, мы добавили фуекцию next()
        short_url = next(cls.short_urls)
        # Создаём словарь с ключами и значениями
        cls.long_to_short[long_url] = short_url
        cls.short_to_long[short_url] = long_url
        return short_url

    @classmethod
    def redirect(cls, short_url):
        # Если короткий url уже есть в БД, то меняем его на новый
        if short_url in cls.short_to_long:
            print(cls.short_to_long[short_url])

        # raise Exception('Redirection failed!')








