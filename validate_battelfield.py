def validate_battlefield(field):
    boats = {'1': 0, '2': 0, '3': 0, '4': 0}
    correct_boats = {'1': 4, '2': 3, '3': 2, '4': 1}

    def check_neighbors(row, col):
        # Check if any diagonal neighbors are occupied (for invalid configuration)
        diagonals = [
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Diagonal directions
        ]
        for dr, dc in diagonals:
            r, c = row + dr, col + dc
            if 0 <= r < len(field) and 0 <= c < len(field[0]):
                if field[r][c] == 1:
                    return False  # Invalid if there is a neighboring boat part diagonally
        return True

    def mark_boat(row, col):
        length = 1
        field[row][col] = -1  # Mark this cell as visited

        # Check horizontal length
        horizontal_length = 1
        col_ptr = col + 1
        while col_ptr < len(field[0]) and field[row][col_ptr] == 1:
            if not check_neighbors(row, col_ptr):
                return 0  # Invalid configuration if diagonals are touching
            field[row][col_ptr] = -1  # Mark as visited
            horizontal_length += 1
            col_ptr += 1

        # Check vertical length if no horizontal boat found
        if horizontal_length == 1:  # No horizontal boat
            vertical_length = 1
            row_ptr = row + 1
            while row_ptr < len(field) and field[row_ptr][col] == 1:
                if not check_neighbors(row_ptr, col):
                    return 0  # Invalid configuration if diagonals are touching
                field[row_ptr][col] = -1  # Mark as visited
                vertical_length += 1
                row_ptr += 1

            length = vertical_length
        else:
            length = horizontal_length

        return length

    # Iterate over the grid to find boats
    for r in range(len(field)):
        for c in range(len(field[r])):
            if field[r][c] == 1:  # Found a boat part
                if check_neighbors(r, c):  # Check for valid neighbor placement
                    boat_length = mark_boat(r, c)
                    if boat_length == 0:
                        print(f"Invalid placement at row {r}, column {c}")
                        return False
                    elif str(boat_length) in boats:
                        boats[str(boat_length)] += 1
                    else:
                        print(f"Invalid boat length found: {boat_length}")
                        return False
                else:
                    print(f"Invalid placement at row {r}, column {c}")
                    return False

    print(boats)
    return boats == correct_boats

# Example of a correct board:
board = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("Valid battlefield:", validate_battlefield(board))
