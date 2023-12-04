import os

string_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def replace_first_occurrence(s, old, new):
    idx = s.find(old)
    if idx != -1:
        s = s[:idx] + new + s[idx+len(old):]
    return s

def find_in_string_digits(c, index, word, digits):
    for digit in filter(lambda x: x[0] == c, string_digits.keys()):
        if word[index:-1].find(digit) == 0:
            digits.append(string_digits[digit])
            return len(digit) - 1 
    return 1
# Problem jest taki, ze tutaj jak jest np. threeight to powinno to rozponać jako 3 i 8, a u mnie usuwa tą 3
def find_digit_in_word(word, digits):
    i = 0
    while i < len(word):         
        c = word[i]
        if c == '' or c == '\n':
            break
        if c.isnumeric():
            digits.append(c)
            i += 1
        else:
            i += find_in_string_digits(c, i, word, digits)

file = open(os.path.dirname(__file__) + '/input.txt', 'r')

values = []
for line in file.readlines():
    digits = []

    find_digit_in_word(line, digits)
    if len(digits) > 0:
        values.append(int(digits[0] + digits[-1]))

print(sum(values));
    
import re

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text

def calibration(text):
    return [int(l[0] + l[-1]) for l in re.sub(r"[A-z]", "", text).split("\n")]
file = open(os.path.dirname(__file__) + '/input.txt', 'r')
text = file.read()
print(calibration(text))
good_values = calibration(replace_words(text))

print(sum(good_values))