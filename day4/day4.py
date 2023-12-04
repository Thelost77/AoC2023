import os

file = open(os.path.dirname(__file__) + '/test1.txt', 'r')
lines = file.readlines()

class NewLine:
    def __init__(self, line, iterations = 1):
        self.line = line
        self.iterations = iterations

def to_int(x):
    return int(x)

def get_value(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return pow(2, x - 1)
values = []
new_lines = list(map(lambda x: NewLine(x), lines))

for i in range(len(new_lines)):
    new_line = new_lines[i]
    line = new_line.line
    corrected_line = line[9:].split('|')
    winning_numbers = list(map(to_int, filter(lambda x: x != '', corrected_line[0].split(' '))))
    our_numbers = list(map(to_int, filter(lambda x: x != '', corrected_line[1].split(' '))))

    matched_numbers = list(filter(lambda x: x in winning_numbers, our_numbers))
    value = get_value(len(matched_numbers))
    for line_to_add_iterations in new_lines[i+1 : i + 1 + len(matched_numbers)]:
        line_to_add_iterations.iterations += new_line.iterations
    values.append(value)

print(sum(values))
print(sum(list(map(lambda x: x.iterations, new_lines))))
    
# Eleganckie rozwiązanie z reddita
s = 0
cards = [1 for _ in lines]

for index, line in enumerate(lines):
    line = line.split(":")[1]
    a, b = line.split("|")
    a, b = a.split(), b.split()

    n = len(set(a) & set(b))

    if n > 0:
        s += 2 ** (n - 1)

    for i in range(n):
        cards[index + i + 1] += cards[index]

print(s, sum(cards))