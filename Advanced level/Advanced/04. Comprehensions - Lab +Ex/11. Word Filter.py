string = list(map(str,input().split(' ')))

result =[word for word in string if len(word) % 2 == 0]

for word in result:
    print(word)