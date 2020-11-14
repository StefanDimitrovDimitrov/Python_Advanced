n = int(input())
usernames = {input() for _ in range(n)}
[print(name) for name in usernames]