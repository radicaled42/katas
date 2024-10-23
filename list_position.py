import math
from collections import Counter

def factorial(n):
    return math.factorial(n)

def list_position(word):
    length = len(word)
    word_count = Counter(word)
    position = 1 
    
    for i in range(length):
        for char in sorted(word_count):
            if char < word[i]:
                if word_count[char] > 0:
                    word_count[char] -= 1
                    permutations = factorial(length - i - 1) // \
                                   math.prod(factorial(v) for v in word_count.values() if v > 0)
                    position += permutations
                    word_count[char] += 1
            else:
                break
        
        word_count[word[i]] -= 1
    
    #print(position)
    return position


#list_position('A') # : 1
#list_position('ABAB') # : 2
#list_position('AAAB') # : 1
#list_position('BAAA') # : 4
#list_position('QUESTION') # : 24572
list_position('BOOKKEEPER') # : 10743}
