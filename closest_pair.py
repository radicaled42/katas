from math import sqrt

def closest_pair(points):

    #points_dict = {}
    #print(points)
    #print(type(points))
    shortest_distance = 999
    origin = ()
    destiny = ()
    for point in points:
        distance = 999
        other_point = ''
        for compare_point in points:
            if compare_point != point:
                a1, a2 = point
                b1, b2 = compare_point
                points_distance = sqrt((abs(a1 - b1))**2 + (abs(a2 - b2))**2)
                #print(f'Point: {point} - Compare: {compare_point} - Distance: {points_distance}')
                if points_distance < distance:
                    distance = points_distance
                    other_point = compare_point
        #print(f'Point: {point} - Compare: {other_point} - Distance: {distance}')
        #print(f'D: {distance} - SD: {shortest_distance}')
        if distance < shortest_distance:
            shortest_distance = distance
            origin = point
            destiny = other_point
    
    print(f'FINAL - Point: {origin} - Compare: {destiny} - Distance: {shortest_distance}')
    return (origin, destiny)
    
    
#closest_pair( ((2, 2), (2, 8), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)))
closest_pair(((2, 2), (2, 8), (5, 5), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9)))