from collections import Counter
from operator import itemgetter

def get_5_most_abundant(counter):
    counter = sorted(counter.items(), key=itemgetter(0))
    counter = sorted(counter, key=itemgetter(1), reverse=True)
    return "".join(x[0] for x in counter[:5])
    
def rotate_chars(input_str, n):
    output = [ord(x) - 97 for x in input_str]
    output = [chr(((x + n) % 26) + 97) for x in output]
    return "".join(output)


with open("input.txt") as input_file:
    total = 0
    for line in input_file:
        code, metadata = line.strip().rsplit("-", 1)
        code = code.replace("-", "")
        code_counts = Counter(code)
        
        sector_id, checksum = metadata.split("[")
        checksum = checksum[:-1]
        
        if checksum == get_5_most_abundant(code_counts):
            total += int(sector_id)
        
    print("Part one:", total)
        
        
with open("input.txt") as input_file:
   for line in input_file:
        code, metadata = line.strip().rsplit("-", 1)
        code = code.replace("-", "")
        code_counts = Counter(code)
        
        sector_id, checksum = metadata.split("[")
        checksum = checksum[:-1]
        
        if checksum == get_5_most_abundant(code_counts):
            sector_name = rotate_chars(code, int(sector_id))
            if "north" in sector_name:
                print("Part two:", sector_name, sector_id)
      
