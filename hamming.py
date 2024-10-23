def hamming(n):
    hammings = []
    
    i = 0
    j = 0
    k = 0
    print (len(hammings))
    while len(hammings) < n:
        print ("In the while")
        
        hammer = (2**i)*(3**j)*(5**k)
        print (f'Hammer: {hammer} - i: {i} - j: {j} - k: {k}')
        hammings.append(hammer)
        
        if i == j == k:
            i += 1
        elif j < i:
            j += 1
        elif k < j:
            k += 1
            
    hammings.sort()
    print(hammings)
        



#hamming(1)  #, 1, "hamming(1) should be 1")
#hamming(2)  #, 2, "hamming(2) should be 2")
#hamming(3)  #, 3, "hamming(3) should be 3")
#hamming(4)  #, 4, "hamming(4) should be 4")
#hamming(5)  #, 5, "hamming(5) should be 5")
#hamming(6)  #, 6, "hamming(6) should be 6")
#hamming(7)  #, 8, "hamming(7) should be 8")
#hamming(8)  #, 9, "hamming(8) should be 9")
hamming(9)  #, 10, "hamming(9) should be 10")
#hamming(10) #, 12, "hamming(10) should be 12")
#hamming(11) #, 15, "hamming(11) should be 15")
#hamming(12) #, 16, "hamming(12) should be 16")
#hamming(13) #, 18, "hamming(13) should be 18")
#hamming(14) #, 20, "hamming(14) should be 20")
#hamming(15) #, 24, "hamming(15) should be 24")
#hamming(16) #, 25, "hamming(16) should be 25")
#hamming(17) #, 27, "hamming(17) should be 27")
#hamming(18) #, 30, "hamming(18) should be 30")
#hamming(19) #, 32, "hamming(19) should be 32")