sentence = input("Please enter a sentence: ")
words = sentence.split()
acronym = ''.join(word[0].upper() for word in words)
print("Qisqartma:", acronym)