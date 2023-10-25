def process_string(s):
    x = s.split()
    result = []
    for i, word in enumerate(x):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return result
print(process_string("This is my test String"))
