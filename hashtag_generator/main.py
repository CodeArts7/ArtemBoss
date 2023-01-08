def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    result = s.title().replace(' ', '')
    res = result.strip()
    return f'{"#"}{res}'


generate_hashtag('     Codewars is nice     ')


