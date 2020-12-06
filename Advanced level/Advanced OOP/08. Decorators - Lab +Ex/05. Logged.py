def logged(fn):

    def wrapper(*args):
        new_line = '\n'
        return f"you called {fn.__name__}{args}{new_line}it returned {fn(*args)}"
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

