package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"


Card_Value :: enum u8 {
	Two = 2,
	Three,
	Four,
	Five,
	Six,
	Seven,
	Eight,
	Nine,
	Ten,
	Jack,
	Queen,
	King,
	Ace,
}

Hand_Type :: enum u8 {
	HIGH_CARD,
	ONE_PAIR,
	TWO_PAIR,
	THREE_OF_A_KIND,
	FOUR_OF_A_KIND,
	FULL_HOUSE,
	FIVE_OF_A_KIND,
}

get_hand_type :: proc(hand: string) -> Hand_Type {
    label_map : map[rune]int
    for c in hand {
	if c in label_map {
	    label_map[c] += 1
	} else {
	    label_map[c] = 1
	}
    }

    for _, val in label_map {

    }
    for key, val in label_map {
	if val == 5 do return Hand_Type.FIVE_OF_A_KIND
	if val == 4 do return Hand_Type.FOUR_OF_A_KIND
	if val == 3 && 
    }
	return Hand_Type.FIVE_OF_A_KIND
}

main :: proc() {
	file, err := os.open("test.txt")
	defer os.close(file)

	data, err1 := os.read_entire_file(file)

	cards: map[string]int
	ranked_bids: []int

	lines := strings.split(string(data), "\n")

	for line in lines {
		parts := strings.split(line, " ")
		hand := parts[0]
		bid, err := strconv.parse_int(strings.trim_space(parts[1]))
		cards[hand] = bid
	get_hand_type(hand)
	}

	fmt.println(cards)


}
