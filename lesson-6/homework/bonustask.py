import string
from collections import Counter
def word_frequency_counter(file_name, top_n=10):
    try:
        word_counts = Counter()
        with open(file_name, 'r') as file:
            for line in file:
                line = line.lower()
                line = line.translate(str.maketrans('', '', string.punctuation))
                words = line.split()
                word_counts.update(words)
        print(f"\nTop {top_n} Most Common Words:")
        for word, count in word_counts.most_common(top_n):
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
file_name = input("Enter the name of the text file (with extension): ")
top_n = int(input("Enter the number of top common words to display: "))
word_frequency_counter(file_name, top_n)
