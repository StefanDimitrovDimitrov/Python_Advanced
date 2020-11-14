def func_executor(*args):
    results = []
    for arg in args:
        func = arg[0]
        params = arg[1]
        results.append(func(*params))
    return results