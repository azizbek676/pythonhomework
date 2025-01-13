import string
from collections import Counter
def word_frequency_counter(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        word_counts = Counter(words)
        print("Word Frequency Count:")
        for word, count in word_counts.most_common():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The file was not found.")
file_name = input("Enter the name of the text file (with extension): ")
word_frequency_counter(file_name)
