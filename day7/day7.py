import os
import numpy as np

file = open(os.path.dirname(__file__) + '/input.txt', 'r')

card_dict = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

hand_types = {
    'FIVE_OF_A_KIND': 6,
    'FOUR_OF_A_KING': 5,
    'FULL_HOUSE': 4,
    'THREE_OF_A_KIND': 3,
    'TWO_PAIR': 2,
    'ONE_PAIR': 1,
    'HIGH_CARD': 0
}

def get_hand_type(hand):
    chars_nums = {}
    for c in hand:
        if c in chars_nums:
            chars_nums[c] += 1
        else:
            chars_nums[c] = 1
    
    for v in sorted(chars_nums.values(), reverse=True):
        if v == 5:
            return hand_types['FIVE_OF_A_KIND']
        if v == 4:
            return hand_types['FOUR_OF_A_KING']
        if v == 3 and 2 in chars_nums.values():
            return hand_types['FULL_HOUSE']
        if v == 3:
            return hand_types['THREE_OF_A_KIND']
        if v == 2 and len(list(filter(lambda x: chars_nums[x] == 2 and x != c, chars_nums))) > 0:
            return hand_types['TWO_PAIR']
        if v == 2 and len(list(filter(lambda x: chars_nums[x] == 2 and x != c, chars_nums))) == 0:
            return hand_types['ONE_PAIR']
        else:
            return hand_types['HIGH_CARD']

hand_rank_dict = {}
for line in file.readlines():
    splited = line.split()
    hand = splited[0]
    rank = splited[1]
    hand_rank_dict[hand] = int(rank)

def sorting_func(x):
    tup = (get_hand_type(x[0]),)
    for i in range(5):
        tup += (card_dict[x[0][i]],)
    return tup

sorted_dict = dict(sorted(hand_rank_dict.items(), key = sorting_func ))

value = 0
rank = 1
values = file = open(os.path.dirname(__file__) + '/values.txt', 'r').readlines()
for key in sorted_dict:
    if values[rank-1] != sorted_dict[key]:
        print(f"For rank {rank} with key {key}")
    print(f"Hand Type: {get_hand_type(key)} Key: {key}, Value: {sorted_dict[key]}")
    value += sorted_dict[key] * rank
    rank += 1

print(value)
