import itertools

#def get_permutations(word_list):
#    if len(word_list) == 0:
#        return []
# 
#    if len(word_list) == 1:
#        return [word_list]
#
#    perm_list = []
# 
#    for index in range(len(word_list)):
#       main_letter = word_list[index]
#       remain_list = word_list[:index] + word_list[index+1:]
#
#       for post_word in get_permutations(remain_list):
#           #print (post_word)
#           perm_list.append([main_letter] + list(post_word))
#        
#    return perm_list

def list_position(word):
    #word_list = list(set([''.join(word) for word in get_permutations(word)]))
    word_list = sorted(set([''.join(word) for word in itertools.permutations(word)]))
    #word_list.sort()
    #print(word_list)
    word_index = word_list.index(word)
    print(word_index+1)
    return word_index+1

    

#list_position('A') # : 1
#list_position('ABAB') # : 2
#list_position('AAAB') # : 1
#list_position('BAAA') # : 4
#list_position('QUESTION') # : 24572
list_position('BOOKKEEPER') # : 10743}
