def adjust_heading(change, old_heading):
    if change == 'L': change = -1
    elif change == 'R': change = 1
    
    return (old_heading + change) % 4
    
def move(position, heading, magnitude):
    magnitude = int(magnitude)
    if heading == 0:
        return (position[0], position[1] + magnitude)
    elif heading == 1:
        return (position[0] + magnitude, position[1])
    elif heading == 2:
        return (position[0], position[1] - magnitude)
    elif heading == 3:
        return (position[0] - magnitude, position[1])
        
def first_revisited(data):
    heading = 0
    pos = (0,0)
    visited = {(0,0)}
    for movement in data:
        heading = adjust_heading(movement[:1], heading)
        for _ in range(int(movement[1:])):
            pos = move(pos, heading, 1)
            if pos in visited:
                return pos         
            visited.add(pos)
            

with open('input.txt') as input:
    data = list(input.read().strip().split(', '))
    
heading = 0
pos = (0,0)

for movement in data:
    heading = adjust_heading(movement[:1], heading)
    pos = move(pos, heading, movement[1:])
    
print(abs(pos[0]) + abs(pos[1]))

pos = first_revisited(data)
print(abs(pos[0]) + abs(pos[1]))
