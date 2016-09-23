number = input()
count = 0
while number:
    rem = number % 10
    count = count + 1
    number /= 10
print count
