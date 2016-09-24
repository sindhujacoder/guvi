import collections
word_one = raw_input()
word_two = raw_input()
word_one = list(word_one)
word_two = list(word_two)
if len(word_one) == len(word_two):
    word_one = collections.Counter(word_one)
    word_two = collections.Counter(word_two)

    if word_one.values() == word_two.values():
        print "isomorphic!"
    else:
        print "nope!"
        




