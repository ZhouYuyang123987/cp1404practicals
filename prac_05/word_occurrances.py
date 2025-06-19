dict_words = {}
sentence = input("Text:")
words = sentence.split(' ')
words.sort()
for word in words:
    try:
        dict_words[word] += 1
    except KeyError:
        dict_words[word] = 1
word_length = max(len(word) for word in dict_words)
for i in dict_words:
    print(f"{i:{word_length}}:{dict_words[i]}")
