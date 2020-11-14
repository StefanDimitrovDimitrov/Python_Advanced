def age_assignment(*args, **kwargs):
    result = {}
    for person in args:
        result[person] = kwargs[person[0]]
    return result

