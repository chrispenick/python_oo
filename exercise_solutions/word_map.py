words = ['monkey','bear','elephant','dog','cat']
##for word in words:
##    word_len.append((word, len(word)))
##
##word_lens = list(map(len, words))
##results = list(zip(words,word_lens))
results = [(word, len(word)) for word in words]

print(words)

results.sort(key = lambda t:t[1])
print(results)


