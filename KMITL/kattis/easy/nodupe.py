def check_repeated_words(phrase):
    words = phrase.split()
    word_set = set()

    for word in words:
        if word in word_set:
            return "no"
        else:
            word_set.add(word)

    return "yes"

x = input()

result = check_repeated_words(x)
print(result)