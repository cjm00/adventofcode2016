import itertools as it

counter = 0

with open("input.txt") as input_file:
    for line in input_file:
        a = list(map(int, line.strip().split()))
        a.sort()
        
        if a[0] + a[1] > a[2]:
            counter += 1
            
print("Part one:", counter)


def chunks(size, iterable):
   for item in zip(*[iter(iterable)] * size):
        yield item

        
counter2 = 0
with open("input.txt") as input_file:
    for triple in chunks(3, input_file.readlines()):
        nums = [int(item) for line in triple for item in line.strip().split()]

        a = tuple(sorted([nums[0], nums[3], nums[6]]))
        b = tuple(sorted([nums[1], nums[4], nums[7]]))
        c = tuple(sorted([nums[2], nums[5], nums[8]]))
        
        if a[0] + a[1] > a[2]: counter2 += 1
        if b[0] + b[1] > b[2]: counter2 += 1
        if c[0] + c[1] > c[2]: counter2 += 1

print("Part two:", counter2)
