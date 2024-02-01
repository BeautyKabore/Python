# UNT Fall 2023 - DTSC 3020 - Introduction to Computation with Python
# This program  will be read text data from a file
# count term frequency per document and document frequency,
# and display the results on the screen.

import re
import nltk
nltk.download()
# Gets the file name
#try:

input_file = input("Please enter the name of the input data file:")
#except FileNotFoundError:
#    print("I couldn't find the file. Try again")
#else:
#    input_file = input("Please enter the name of the input data file:")
# reading each list
word_search_count = 0
word_search = input("Please enter a word for which you look term "
                    "frequency and document frequency or blank space if done: ")
file = open('hobbies.txt', 'r')
readData = file.read()
new_word_count = word_search_count + 1
for word in readData:
    if " " == word_search:
        exit()
    elif word_search not in readData:
            print("The word cannot be found in the collection.")
            word_search = input("Please enter a word for which you look term "
                                "frequency and document frequency "
                                "or blank space if done: ")
    elif  word_search == word:
        token = word_tokenize(readData)
        word_search_count += 1
        term_frequency = {}
print(f"Document Frequency of {word_search.lower()}:{word_search_count}")
for line in range(0, len(readData), 2):
        student_Id = readData[line]
        desc = readData[line + 1].strip()
print("Term Frequency (TF) are as follows: ")
print(f'TF for {word_search} in {student_Id} are : {new_word_count}')
    #print(f'TF for {term_frequency[word_search]}  are : {term_frequency[word_search_count]}')

