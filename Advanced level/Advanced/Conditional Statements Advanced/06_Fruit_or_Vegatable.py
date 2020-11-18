item = input()

is_item = item == 'banana' or item == 'apple' or item == 'kiwi' or item == 'cherry'or item == 'lemon' or item == 'grapes'
is_item2 = item == 'tomato' or item == 'cucumber' or item =='pepper' or item == 'carrot'

if is_item:
    print('fruit')
elif is_item2:
    print('vegetable')
else:
    print('unknown')