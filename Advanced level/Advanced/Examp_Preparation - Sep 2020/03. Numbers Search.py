def numbers_searching(*arg):
    list = sorted([*arg])
    missing_number = [x for x in range(list[0], list[-1]+1) if x not in list]

    seen = {}
    dupes = []

    for x in list:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
            seen[x] += 1

    number = "".join(str(x) for x in (missing_number))
    result =[int(number), dupes]

    return result
    # return f"[{number}, {dupes}]"

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))