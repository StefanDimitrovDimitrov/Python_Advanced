def generator_string(words):
    for word in words.split():
        yield word


my_sentence = generator_string('This is a test')
for word in my_sentence:
    print(word)
