n_length, m_length = [int(x) for x in input().split()]

n = set()
m = set()

[n.add(int(input())) for _ in range(n_length)]
[m.add(int(input())) for _ in range(m_length)]

intersection = n.intersection(m)

[print(number) for number in intersection]
