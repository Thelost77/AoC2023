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
    'zero': '0',
}

def replace_first_occurrence(s, old, new):
    idx = s.find(old)
    if idx != -1:
        s = s[:idx] + new + s[idx+len(old):]
    return s

def find_in_string_digits(c, index, word, digits):
    for digit in filter(lambda x: x[0] == c, string_digits.keys()):
        if word.find(digit) == index:
            digits.append(string_digits[digit])
            return replace_first_occurrence(word, digit, '')
    return None

def find_digit_in_word(word, digits):
    if word == '' or word == '\n':
        return digits
    new_word = ''
    for i in range(len(word)):
        c = word[i]
        if c.isnumeric():
            digits.append(c)
            new_word = replace_first_occurrence(word, c, '')
            break
        else:
            temp = find_in_string_digits(c, i, word, digits)
            if temp != None:
                new_word = temp
                break
        new_word = replace_first_occurrence(word, c, '')
        break
    return find_digit_in_word(new_word, digits)

file = open(os.path.dirname(__file__) + '\\input.txt', 'r')

values = []
for line in file.readlines():
    digits = []

    find_digit_in_word(line, digits)
    values.append(int(digits[0] + digits[-1]))

# print(sum(values));
    
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
file = open(os.path.dirname(__file__) + '\\input.txt', 'r')
text = file.read()
# print(calibration(text))
# print()
good_values = calibration(replace_words(text))

for i in range(1000):
    if good_values[i] != values[i]:
        print(i)
        # print(good_values[i])
        # print(values[i])