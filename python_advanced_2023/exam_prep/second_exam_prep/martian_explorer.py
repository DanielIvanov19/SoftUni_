SIZE = 6

deposits = {'W': ['Water', 0], 'M': ['Metal', 0], 'C': ['Concrete', 0]}

mars = []
rover_pos = []

for row in range(SIZE):
    current_row = input().split()

    if 'E' in current_row:
        rover_pos = [row, current_row.index('E')]
    mars.append(current_row)
# print(*mars, sep='\n')
# print(rover_pos)

# command mapping to not use if statements for the edge case when the rover is out of the field
directions = {
    'up': lambda r, c: [(r - 1) % SIZE, c],  # (-1, 0),
    'down': lambda r, c: [(r + 1) % SIZE, c],  # (1, 0),
    'left': lambda r, c: [r, (c - 1) % SIZE],  # (0, -1),
    'right': lambda r, c: [r, (c + 1) % SIZE],  # (0, 1)
}

commands = input().split(', ')

for command in commands:
    rover_pos = directions[command](*rover_pos)  # '*' to unpack the arguments for the directions mapper
    position = mars[rover_pos[0]][rover_pos[1]]

    if position in deposits:
        print(f'{deposits[position][0]} deposit found at ({rover_pos[0]}, {rover_pos[1]})')

        deposits[position][1] += 1

    elif position == 'R':
        print(f'Rover got broken at ({rover_pos[0]}, {rover_pos[1]})')
        break

if all([deposits['W'][1], deposits['M'][1], deposits['C'][1]]):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
