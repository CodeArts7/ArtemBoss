class make_looper:

    def __init__(self, string):
        self.string = string
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        if self.string == '':
            return ''
        else:
            return self.string[self.calls % len(self.string) - 1]


abc = make_looper('abc')
abc()
abc()
abc()
abc()
abc()
abc()













