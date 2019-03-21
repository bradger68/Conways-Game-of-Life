array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

array2 = [[1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]]


def grid_to_string(input):
    result = []
    for element in input:
        seperator = ' '
        foo = map(str, element)
        result.append(seperator.join(foo))

    return '\n'.join(result)

def step(state):
    next_state = [[0 for i in state[0]] for i in state]
    for i in range(len(state)):
        for j in range(len(state[0])):
            neighbors = check_neighbors(state, i, j)
            if state[i][j] == 1:
                if neighbors < 2:
                    next_state[i][j] = 0
                elif neighbors == 2 or neighbors == 3:
                    next_state[i][j] = 1
                elif neighbors > 3:
                    next_state[i][j] = 0
            else:
                if neighbors == 3:
                    next_state[i][j] = 1

    return next_state


def check_neighbors(current_state, row, col):
    total = 0
    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (r == row and c == col) or r < 0 or r >= len(current_state) or c < 0 or c >= len(current_state[0]):
                continue
            total += current_state[r][c]
    return total

#print(check_neighbors(array2, 1, 0))

print(grid_to_string(array2))
print("\n")
print(grid_to_string(step(array2)))


# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.