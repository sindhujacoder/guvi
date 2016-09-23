testcases = input()
while testcases:
    number = input()
    factorial = 1
    for num in range(1,number+1):
        factorial = factorial * num
    testcases = testcases - 1
print factorial
