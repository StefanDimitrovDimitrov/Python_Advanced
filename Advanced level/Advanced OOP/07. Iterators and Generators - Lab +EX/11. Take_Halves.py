def solution():

    def intergers():
        current_int = 0
        while True:
            current_int += 1
            yield current_int


    def halves():
        for i in intergers():
            yield i / 2

    def take(n , halves):
        result = []
        for i, num in enumerate(halves):
            if i == n:
                return result
            result.append(num)


        # result = [next(halves)for _ in range(n)]
        return result


    return (take, halves, intergers)

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
