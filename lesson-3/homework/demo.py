def reverse_tuple(tpl):
    return tpl[::-1]

sample_tuple = tuple(map(int, input("Enter the tuple elements separated by commas: ").split(',')))
print("Reverse Tuple:", reverse_tuple(sample_tuple))