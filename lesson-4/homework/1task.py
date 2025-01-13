def uncommon_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    uncommon = set1.symmetric_difference(set2)
    return list(uncommon)
list1 = input("Enter first list: ").split(',')
list2 = input("Enter second list: ").split(',')
list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]
result = uncommon_elements(list1, list2)
print("Uncommon elementlar:", result)