def validate_battlefield(field):
    boats = {'1': 0, '2': 0, '3': 0, '4': 0}
    correct_boats = {'1': 4, '2': 3, '3': 2, '4': 1}
    count_boat = 0
    
    # Go over the row
    for boat_row in range(0, len(field)):
        #print (field[boat_row])
        # Go through each member of the row
        for boat_column in range(0, len(field[boat_row])):
            #print (f'Element in the row: {field[boat_row][boat_column]} - column: {boat_column} - row: {boat_row}')
            if field[boat_row][boat_column] == 1 and field[boat_row - 1][boat_column] != 1 and field[boat_row + 1][boat_column] != 1 and field[boat_row][boat_column - 1] != 1 and field[boat_row][boat_column + 1] != 1:
                boats['1'] += 1
            elif field[boat_row][boat_column] == 1 and field[boat_row - 1][boat_column] != 1 and field[boat_row][boat_column - 1] != 1 and field[boat_row][boat_column + 1] != 1:
                #print (f'There might be a boat on column: {boat_column} - row: {boat_row}')
                for index_row in range(boat_row, len(field)):
                    if field[index_row][boat_column] == 1:
                        count_boat += 1
                    else:
                        break
                #print (f"The length of the boat is {count_boat}")
                if f'{count_boat}' in boats.keys():
                    boats[f'{count_boat}'] += 1
                count_boat = 0
            elif field[boat_row][boat_column] == 1 and field[boat_row][boat_column - 1] != 1 and field[boat_row + 1][boat_column] != 1 and field[boat_row - 1][boat_column] != 1:
                #print (f'There might be a boat on column: {boat_column} - row: {boat_row}')
                for index_col in range(boat_column, len(field[boat_row])):
                    if field[boat_row][index_col] == 1:
                        count_boat += 1
                    else:
                        break
                #print (f"The length of the boat is {count_boat}")
                if f'{count_boat}' in boats.keys():
                    boats[f'{count_boat}'] += 1
                count_boat = 0
            #elif field[boat_row][boat_column] == 1 and (field[boat_row + 1][boat_column] == 1 or field[boat_row + 1][boat_column - 1] == 1 or field[boat_row + 1][boat_column + 1] == 1 or field[boat_row][boat_column - 1] == 1 or field[boat_row][boat_column + 1] == 1 or field[boat_row - 1][boat_column - 1] == 1 or field[boat_row - 1][boat_column] == 1 or field[boat_row - 1][boat_column + 1] == 1):
            elif field[boat_row][boat_column] == 1 and (field[boat_row + 1][boat_column - 1] == 1 or field[boat_row + 1][boat_column + 1] == 1 or field[boat_row - 1][boat_column - 1] == 1 or field[boat_row - 1][boat_column + 1] == 1):
                print("There is an error with this configuration")
                print (f'There might be a error on column: {boat_column} - row: {boat_row}')

    #print (field)
    print (boats)
    if (boats == correct_boats):
        print("Correct configuration")
    else:
        print("There is something wrong")



battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
validate_battlefield(battleField)