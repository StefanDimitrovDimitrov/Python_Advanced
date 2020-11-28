VOWELS = {"A", "E", "I", "O", "Y"}

def vowel_filter(fn):

    def wrapper(*args, **kwargs):

        result = fn(*args, *kwargs)
        return [c for c in result if c.upper() in VOWELS]

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
