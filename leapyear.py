testcases = input()
while testcases:

    year = input()
    if year % 4 == 0:
        print "leap"
    elif year % 400 == 0 and year % 100 == 0:
        print "leap"
    else:
        print "not leap"
        
    testcases = testcases -1
