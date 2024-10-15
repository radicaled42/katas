def almost_awesome(number, action):
    for element in range(number - 2, number + 3):
        str_number = str(element)

        rotated_str_element = str_number[::-1]
        if str_number == rotated_str_element and element > 99:
            return 1

        zeros = 1
        for index in range(1, len(str_number)):
            if str_number[index] != '0':
                zeros = 0
        
        if zeros == 1:
            return 1
    
        ascending = 1
        descending = 1
        str_number = str(element)
        for index in range(1, len(str_number)):
            prev_digit = int(str_number[index - 1])
            current_digit = int(str_number[index])
            if prev_digit == 9 and current_digit != 0 and current_digit != 8:
                ascending = 0
            elif prev_digit != 9 and prev_digit + 1 != current_digit:
                ascending = 0
            else:
                pass
            if prev_digit == 1 and current_digit != 0 and current_digit != 2:
                descending = 0
            elif prev_digit != 9 and prev_digit - 1 != current_digit:
                descending = 0
            else:
                pass
        if ascending == 1 or descending == 1:
            return 1
    # Nothing match
    return 0        

def check_palindrome(pal_num):
    str_number = str(pal_num)
    rotated_str_number = str_number[::-1]

    # Check for palindrome
    if str_number == rotated_str_number and pal_num > 99:
        return 2
    else:   
        return almost_awesome(pal_num, 'palindrome')

def check_zeros(str_number):
    # Check if its follow by 0
    zeros = 1
    if int(str_number) > 98:
        for index in range(1, len(str_number)):
            if str_number[index] != '0':
                zeros = 0
        if zeros == 1:
            return 2
        else:
            return almost_awesome(int(str_number), 'zeros')    
    else:
        return 0
        
def asc_desc(str_number):
    # Check if the number is ascending or descending if ascending 9 --> 0 is descending 1 --> 0
    ascending = 1
    descending = 1
    if len(str_number) > 2:
        for index in range(1, len(str_number)):
            prev_digit = int(str_number[index - 1])
            current_digit = int(str_number[index])
            
            # Check for ascending sequence
            if prev_digit == 9:
                if current_digit != 0:
                    ascending = 0
            elif prev_digit + 1 != current_digit:
                ascending = 0
            
            # Check for descending sequence
            if prev_digit == 1:
                if current_digit != 0:
                    descending = 0
            elif prev_digit - 1 != current_digit:
                descending = 0
            
            # Break early if both checks have failed
            if ascending == 0 and descending == 0:
                break
    else:
        return 0
    
    if ascending == 1 or descending == 1:
        return 2
    else:
        return almost_awesome(int(str_number), 'asc_desc')

def is_interesting(number, awesome_phrases):
    result = 0
    str_number = str(number)
    
    # Check for > 99
    if number < 99:
        result == 0

    # Check for awesome
    awesome_element = 0
    if awesome_phrases:
        if number in awesome_phrases:
            result = 2
        else: 
            # Check if its near some awesome number
            for awsesome_number in awesome_phrases:
                if abs(number - awsesome_number) <= 2:
                    awesome_element = 1
            if awesome_element == 1:
                result = 1
            else:
                result = 0

    if result == 0:
        if number > 97:
            if (check_zeros(str_number) == 2):
                result = 2
            else:
                if (asc_desc(str_number) == 2):
                    result = 2
                else:
                    result = check_palindrome(number)
        
    print (f'The number: {number} - result: {result}')
    return result


# "boring" numbers
#is_interesting(3, [1337, 256])    # 0
#is_interesting(3236, [1337, 256]) # 0
#is_interesting(30, []) # 0
#is_interesting(97, []) # 0
is_interesting(98, []) # 1
#is_interesting(1, []) # 1

## progress as we near an "interesting" number
#is_interesting(11207, []) # 0
#is_interesting(11208, []) # 0
#is_interesting(11209, []) # 1
#is_interesting(11210, []) # 1
#is_interesting(11211, []) # 2
#is_interesting(11211, [1337, 256]) # 2
#is_interesting(10000, []) # 2
#is_interesting(12345, []) # 2
#is_interesting(54321, []) # 2
#is_interesting(43210, []) # 2
#is_interesting(67890, []) # 2
#is_interesting(69078, []) # 0
#
## nearing a provided "awesome phrase"
#is_interesting(1335, [1337, 256]) # 1
#is_interesting(1336, [1337, 256]) # 1
#is_interesting(1337, [1337, 256]) # 2
