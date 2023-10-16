# This script is intended to count the amount of words a user enters, 
import re
 
# This function Checks if word exists in word_counts dict. If so, increments the count by 1. Else adds the new word to dict with a count of 1.
def update_words(word, used_words):
    if word in used_words:
        used_words[word] += 1
    else:
        used_words.update({word: 1})
    return used_words

# This function will split a sentence into a list of words, by removing punctuation with regex and split on whitespaces. 
def split_sentence(sentence):
   cleaned = re.sub(r'[,\.]', '', sentence)
   my_words = cleaned.split(" ")
   return my_words

def main ():
    words_count = {}

    my_sentence = input("Please enter a sentence ")

    words = split_sentence(my_sentence)

    for word in words:
        words_count = update_words(word.title(), words_count)

    print(words_count)
main()