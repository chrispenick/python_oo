def find_longest_word(word_list):
    return max(word_list, key = len)
            
words = ['monkey','bear','elephant','dog','cat']
print(find_longest_word(words))

