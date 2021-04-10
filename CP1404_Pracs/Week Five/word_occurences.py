"""
Patrick Robinson
12251568
Word Occurrences
Counting the amount of times a word appears in the user entry and then outputting the results

"""

WORD_STORAGE = {}

string_input = input("Enter a string")  # Getting the input
words = string_input.split()

for word in words:
    word_amount = WORD_STORAGE.get(word, 0)  # Adding the words to the dictionary and counting them
    WORD_STORAGE[word] = word_amount + 1

print(WORD_STORAGE)

WORD_LIST = list(WORD_STORAGE.keys())  # Converting the dictionary to a list to be sorted
WORD_LIST.sort()
print(WORD_LIST)
longest_word = len(max(WORD_LIST))  # Getting the length of the longest word
longest_word_int = int(longest_word)
list_length = len(WORD_LIST)
for word in WORD_LIST:
    print(
        "{:{}} = {}".format(word, longest_word_int, WORD_LIST.count(word)))  # Printing the results in a formatted form
