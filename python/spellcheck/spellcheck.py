def spellcheck(word):
    if word in words:
        return
    suggestions = []
    for a in range(len(word) - 1):
        for b in range(a + 1, len(word)):
            if word[a:b] in words:
                suggestions.append(word[a:b])
    return suggestions

wordfile = "wordsEn.txt"
f = open(wordfile, 'r')
words = []
for line in f:
    words.append(line.strip())

word = "init"
while word != "":
    word = input("Word to check (leave blank to quit): ")

    suggestions = spellcheck(word)
    if suggestions:
        print(suggestions)

