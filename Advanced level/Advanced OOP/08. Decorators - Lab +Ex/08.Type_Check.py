def type_check(type_name):
    def decorator(fn):
        def wrapper(*args):

            if type_name == type(args[0]):
                return fn(*args)
            return "Bad Type"

        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))












