package main

import "core:fmt"
import "core:os"
import "core:slice"
import "core:sort"
import "core:strconv"
import "core:strings"

Card_Value := map[rune]u8 {
	'J' = 1,
	'2' = 2,
	'3' = 3,
	'4' = 4,
	'5' = 5,
	'6' = 6,
	'7' = 7,
	'8' = 8,
	'9' = 9,
	'T' = 10,
	'Q' = 11,
	'K' = 12,
	'A' = 13,
}

Hand_Type :: enum u8 {
	HIGH_CARD,
	ONE_PAIR,
	TWO_PAIRS,
	THREE_OF_A_KIND,
	FULL_HOUSE,
	FOUR_OF_A_KIND,
	FIVE_OF_A_KIND,
}

array_contains_other_elements :: proc(arr: []int, element: int, index: int) -> bool {
	for el, i in arr {
		if el == element && i != index do return true
	}
	return false
}

get_hand_value :: proc(hand: string) -> [5]u8 {
	hand_value: [5]u8
	for rune, i in hand {
		hand_value[i] = Card_Value[rune]
	}
	return hand_value

}
get_hand_type :: proc(hand: string) -> Hand_Type {
	label_map: map[rune]int
	number_of_jokers := 0
	for c in hand {
		if c == 'J' {
			number_of_jokers += 1
			continue
		}
		if c in label_map {
			label_map[c] += 1
		} else {
			label_map[c] = 1
		}
	}
	values: [dynamic]int
	for _, val in label_map {
		append(&values, val)
	}
	sorted_values := values[:]
	slice.reverse_sort(sorted_values)
	for val, i in sorted_values {
		if val == 5 || val + number_of_jokers == 5 do return Hand_Type.FIVE_OF_A_KIND
		else if val == 4 || val + number_of_jokers == 4 do return Hand_Type.FOUR_OF_A_KIND
		else if (val == 3 || val + number_of_jokers == 3) && array_contains_other_elements(sorted_values, 2, i) do return Hand_Type.FULL_HOUSE
		else if val == 3 || val + number_of_jokers == 3 do return Hand_Type.THREE_OF_A_KIND
		else if (val == 2 || val + number_of_jokers == 2) && array_contains_other_elements(sorted_values, 2, i) do return Hand_Type.TWO_PAIRS
		else if val == 2 || val + number_of_jokers == 2 do return Hand_Type.ONE_PAIR
		else do return Hand_Type.HIGH_CARD
	}
	return Hand_Type.FIVE_OF_A_KIND
}

Camel_Card :: struct {
	hand_type:  Hand_Type,
	hand_value: [5]u8,
	bid:        int,
	hand:       string,
}

compare_hand_values :: proc(val1: [5]u8, val2: [5]u8) -> bool {
	for i := 0; i < 5; i += 1 {
		if val1[i] == val2[i] do continue
		return val1[i] < val2[i]
	}
	return false
}

sort_camel_cards :: proc(camel_cards: [dynamic]Camel_Card) -> [dynamic]Camel_Card {
	l := len(camel_cards) - 1
	for i := 0; i < l; i += 1 {
		for j := 0; j < l - i; j += 1 {
			if camel_cards[j].hand_type == camel_cards[j + 1].hand_type {
				if compare_hand_values(camel_cards[j].hand_value, camel_cards[j + 1].hand_value) {
					camel_cards[j], camel_cards[j + 1] = camel_cards[j + 1], camel_cards[j]
				}
			} else {
				if camel_cards[j].hand_type < camel_cards[j + 1].hand_type {
					camel_cards[j], camel_cards[j + 1] = camel_cards[j + 1], camel_cards[j]
				}

			}
		}
	}
	return camel_cards
}

main :: proc() {
	//file, err := os.open("test.txt")
	file, err := os.open("input.txt")
	defer os.close(file)

	data, err1 := os.read_entire_file(file)

	camel_cards: [dynamic]Camel_Card

	lines := strings.split(string(data), "\n")

	for line in lines {
		parts := strings.split(line, " ")
		hand := parts[0]
		if len(parts) == 1 do break
		bid, err := strconv.parse_int(strings.trim_space(parts[1]))

		camel_card := Camel_Card{get_hand_type(hand), get_hand_value(hand), bid, hand}
		append(&camel_cards, camel_card)
	}
	outcome := 0
	sort_camel_cards(camel_cards)
	l := len(camel_cards) - 1

	for i := 0; i <= l; i += 1 {
		fmt.println(i + 1, camel_cards[l - i].hand)
		outcome += (i + 1) * camel_cards[l - i].bid
	}
	fmt.println(outcome)

}
