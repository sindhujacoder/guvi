testcases = input()
number_set = set()
while testcases:
    number = input()
    number_set.add(number)
    testcases = testcases - 1
print max(number_set)
