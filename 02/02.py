
class Keypad:
    def __init__(self):
        self.x = 1
        self.y = 1
        
    def get_digit(self):
        return self.y * 3 + self.x + 1
        
    def move(self, input):
        if input == "D":
            self.y = min(2, self.y + 1)
        if input == "U":
            self.y = max(0, self.y - 1)
        if input == "R":
            self.x = min(2, self.x + 1)
        if input == "L":
            self.x = max(0, self.x - 1)

output = []
pad = Keypad()

with open("input.txt") as input_file:
    for line in input_file:
        for char in line.strip():
            pad.move(char)
        
        output.append(pad.get_digit())
    
print("Part one:", "".join(str(x) for x in output))

class Keypad2:
    digit_lookup = {
        (0, 2) : "1",
        (-1, 1) : "2",
        (0, 1) : "3",
        (1, 1) : "4",
        (-2, 0) : "5",
        (-1, 0) : "6",
        (0, 0) : "7",
        (1, 0) : "8",
        (2, 0) : "9",
        (-1, -1) : "A",
        (0, -1) : "B",
        (1, -1) : "C",
        (0, -2) : "D",
        }
                   
    def __init__(self):
        self.x = -2
        self.y = 0
        
    def get_digit(self):
        return Keypad2.digit_lookup[(self.x, self.y)]
        
    def move(self, input):
        if input == "D":
            self.y = self.y if abs(self.x) + abs(self.y - 1) > 2 else self.y - 1
        if input == "U":
            self.y = self.y if abs(self.x) + abs(self.y + 1) > 2 else self.y + 1
        if input == "R":
            self.x = self.x if abs(self.x + 1) + abs(self.y) > 2 else self.x + 1
        if input == "L":
            self.x = self.x if abs(self.x - 1) + abs(self.y) > 2 else self.x - 1
            
            
output = []
pad = Keypad2()

with open("input.txt") as input_file:
    for line in input_file:
        for char in line.strip():
            pad.move(char)
        
        output.append(pad.get_digit())
    
print("Part two:", "".join(str(x) for x in output))
    