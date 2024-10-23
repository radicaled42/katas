import math
from collections import Counter

def factorial(n):
    return math.factorial(n)

def list_position(word):
    # Convert the word into a list of characters
    length = len(word)
    word_count = Counter(word)  # Create a frequency count of each character
    position = 1  # Start counting from 1 for 1-based index
    
    print(word_count)
    
    for i in range(length):
        for char in sorted(word_count):
            if char < word[i]:
                # Temporarily decrease the count of `char` and calculate permutations
                if word_count[char] > 0:  # Ensure no negative values
                    word_count[char] -= 1
                    permutations = factorial(length - i - 1) // \
                                   math.prod(factorial(v) for v in word_count.values() if v > 0)
                    position += permutations
                    word_count[char] += 1  # Restore the count
            else:
                break
        
        word_count[word[i]] -= 1  # Decrease the count of the current character
        if word_count[word[i]] < 0:
            raise ValueError("Count of characters cannot be negative.")
    
    print(position)
    return position


#list_position('A') # : 1
#list_position('ABAB') # : 2
#list_position('AAAB') # : 1
#list_position('BAAA') # : 4
#list_position('QUESTION') # : 24572
list_position('BOOKKEEPER') # : 10743}
