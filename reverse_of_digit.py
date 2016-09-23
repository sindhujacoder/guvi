import math
testcases = input()
while testcases:
    number = input()
    length = len(str(number))
    
    rev = 0
    while number:
       
       place = 10 ** (length-1)
       
       rem = number % 10
     
       rev += (rem * place)
      
       number /= 10
       length = length - 1
    print rev
    testcases = testcases - 1
       
        
