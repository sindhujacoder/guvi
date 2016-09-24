testcases = input()
while testcases:
    word_one = raw_input()
    word_one = ''.join(word_one[x:x+2][::-1] for x in xrange(0,len(word_one),2))
    print word_one
    
