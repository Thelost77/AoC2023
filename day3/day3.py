import os

class Gear:
    def __init__(self, line_idx, idx, value = 0):
        self.line_idx = line_idx
        self.idx = idx
        self.value = value

    def __repr__(self):
        return f"Line idx = {self.line_idx} idx = {self.index} value = {self.value}"

def get_chars(first_index, last_index, line, lines, line_i):
    begin = first_index - 1 if first_index > 0 else first_index
    end = last_index + 1 if last_index < len(line) - 1 else last_index
    return lines[line_i][begin:end + 1]

def get_gear(first_index, last_index, line, lines, line_i):
    begin = first_index - 1 if first_index > 0 else first_index
    end = last_index + 1 if last_index < len(line) - 1 else last_index
    for i in range(begin, end + 1):
        if lines[line_i][i] == '*':
            return Gear(line_i, i)

    return None

file = open(os.path.dirname(__file__) + '/input.txt', 'r')

part_numbers = []
gears = []
gears_value = []
lines = file.readlines()
line_i = 0

while line_i < len(lines):
    line = lines[line_i].replace('\n', '')
    i = 0
    first_index = -1
    last_index = -1
    while i < len(line):
        c = line[i]
        if c.isnumeric():
            if first_index == -1:
                first_index = i
            else:
                last_index = i
        if not c.isnumeric() or i == len(line) - 1:
            last_index = last_index if last_index >= 0 else first_index
            chars_to_check = ''
            if first_index > -1 and last_index > -1:
                for j in range(-1, 2):
                    if (line_i == 0 and j == -1) or (line_i == len(lines) - 1 and j == 1):
                        continue
                    chars_to_check += get_chars(first_index, last_index, line, lines, line_i + j)
                if len([x for x in filter(lambda x: not (x.isnumeric() or x == '.'), chars_to_check)]) > 0:
                    part_number = int(line[first_index:last_index + 1])
                    part_numbers.append(part_number)
                    for j in range(-1, 2):
                        if (line_i == 0 and j == -1) or (line_i == len(lines) - 1 and j == 1):
                            continue
                        gear = get_gear(first_index, last_index, line, lines, line_i + j)
                        if gear != None:
                            gear.value = part_number
                            prev_gear = next((x for x in gears if (x.idx == gear.idx and x.line_idx == gear.line_idx)), None)
                            if prev_gear != None:
                                gears_value.append(prev_gear.value * gear.value)
                            else:
                                gears.append(gear)

            

            first_index = -1
            last_index = -1

        i += 1
            
    line_i += 1

print("Gears Value: ", sum(gears_value))
print("Part Numbers Value: ", sum(part_numbers))