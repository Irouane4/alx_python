word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
word_first_3, *middle_word, word_last_2 = word
print("First 3 letters: {}".format("".join(word_first_3)))
print("Last 2 letters: {}".format("".join(word_last_2)))
print("Middle word: {}".format("".join(middle_word)))
