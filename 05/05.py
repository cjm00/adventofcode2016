import hashlib

puzzle_input = "cxdnnyjw"
counter = 0
password = ""

while len(password) < 8:
    h = hashlib.md5()
    puzzle = puzzle_input + str(counter)
    h.update(puzzle.encode('utf-8'))
    h = h.hexdigest()
    if h[:5] == "00000": password += h[5]
    counter += 1
    
print("Part one:", password)

password = [False] * 8
counter = -1

while not all(password):
    counter += 1
    h = hashlib.md5()
    puzzle = puzzle_input + str(counter)
    h.update(puzzle.encode('utf-8'))
    h = h.hexdigest()
    if h[:5] == "00000":
        try: 
            index = int(h[5])
        except ValueError:
            continue
            
        if index > 7:
            continue
            
        if password[index] is False:
            password[index] = h[6]
    
    
print("Part two:", "".join(password))
