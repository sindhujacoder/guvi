testcases = input()
roman_dict = {'I':1,'V':5,'X':10,'L':50,'D':500,'M':1000}
while testcases:
    roman = raw_input()
    roman = list(roman)
    
    num = roman_dict.get(roman[0])
    if len(roman) == 1:
        
        print num
    else:
        for i in range(1,len(roman)):
            value = roman_dict.get(roman[i])
            pvalue = roman_dict.get(roman[i-1])
            num = num + value
            if pvalue < value :
                num = (num - pvalue) - pvalue
        print num
    testcases = testcases - 1
    
    
