package main

import "core:fmt"
import "core:os"
import "core:strings"

Valid_Moves :: enum u8 {
	None,
	North,
	East,
	South,
	West,
}

Opposite_Moves := map[Valid_Moves]Valid_Moves {
	Valid_Moves.West  = Valid_Moves.East,
	Valid_Moves.East  = Valid_Moves.West,
	Valid_Moves.South = Valid_Moves.North,
	Valid_Moves.North = Valid_Moves.South,
}

Game_Pos :: struct {
	x:           int,
	y:           int,
	valid_moves: [2]Valid_Moves,
}

Turns := map[string][2]Valid_Moves {
	"|" = [2]Valid_Moves{Valid_Moves.North, Valid_Moves.South},
	"-" = [2]Valid_Moves{Valid_Moves.East, Valid_Moves.West},
	"L" = [2]Valid_Moves{Valid_Moves.North, Valid_Moves.East},
	"J" = [2]Valid_Moves{Valid_Moves.North, Valid_Moves.West},
	"7" = [2]Valid_Moves{Valid_Moves.South, Valid_Moves.West},
	"F" = [2]Valid_Moves{Valid_Moves.South, Valid_Moves.East},
	"." = [2]Valid_Moves{Valid_Moves.None, Valid_Moves.None},
}

print_game_map :: proc(game_map: [dynamic][]string) {
	for line in game_map {
		fmt.println(line)
	}
}

contains_at :: proc(arr: []string, el: string) -> int {
	for c, i in arr {
		if c == el do return i
	}
	return -1
}

contains :: proc(arr: [2]Valid_Moves, el: Valid_Moves) -> bool {
	for move in arr {
		if el == move do return true
	}
	return false
}

add_valid_move :: proc(valid_moves: ^[2]Valid_Moves, move_to_add: Valid_Moves) {
	for &move in valid_moves {
		if move == Valid_Moves.None {
			move = move_to_add
			return
		}

	}
}

find_valid_moves_for_starting_point :: proc(
	game_map: [dynamic][]string,
	starting_point: ^Game_Pos,
) {
	next_x := starting_point.x - 1
	if next_x >= 0 {
		valid_moves := Turns[game_map[starting_point.y][next_x]]
		if contains(valid_moves, Valid_Moves.East) do add_valid_move(&starting_point.valid_moves, Valid_Moves.West)
	}

	next_x = starting_point.x + 1
	if next_x < len(game_map[starting_point.y]) {
		valid_moves := Turns[game_map[starting_point.y][next_x]]
		if contains(valid_moves, Valid_Moves.West) do add_valid_move(&starting_point.valid_moves, Valid_Moves.East)

	}


	next_y := starting_point.y - 1
	if next_y >= 0 {
		valid_moves := Turns[game_map[next_y][starting_point.x]]
		if contains(valid_moves, Valid_Moves.South) do add_valid_move(&starting_point.valid_moves, Valid_Moves.North)

	}

	next_y = starting_point.y + 1
	if next_y < len(game_map) {
		valid_moves := Turns[game_map[next_y][starting_point.x]]
		if contains(valid_moves, Valid_Moves.North) do add_valid_move(&starting_point.valid_moves, Valid_Moves.South)
	}

}

get_next_pos :: proc(
	move: Valid_Moves,
	curr_pos: Game_Pos,
	game_map: [dynamic][]string,
) -> Game_Pos {

	switch move {
	case .North:
		return Game_Pos{curr_pos.x, curr_pos.y - 1, Turns[game_map[curr_pos.y - 1][curr_pos.x]]}
	case .South:
		return Game_Pos{curr_pos.x, curr_pos.y + 1, Turns[game_map[curr_pos.y + 1][curr_pos.x]]}
	case .East:
		return Game_Pos{curr_pos.x + 1, curr_pos.y, Turns[game_map[curr_pos.y][curr_pos.x + 1]]}
	case .West:
		return Game_Pos{curr_pos.x - 1, curr_pos.y, Turns[game_map[curr_pos.y][curr_pos.x - 1]]}
	case .None:
		return curr_pos

	}


	return Game_Pos{}
}
get_next_mov :: proc(valid_moves: [2]Valid_Moves, prev_mov: Valid_Moves) -> Valid_Moves {
	opposite_move := Opposite_Moves[prev_mov]
	for move in valid_moves {
		if move != opposite_move do return move
	}
	return Valid_Moves.None
}

Vector2 :: struct {
	x: int,
	y: int,
}

main :: proc() {
	file, _ := os.open("../test1.txt")
	//file, _ := os.open("../input.txt")
	defer os.close(file)

	data, _ := os.read_entire_file(file)

	lines := strings.split(string(data), "\n")

	game_map: [dynamic][]string
	starting_pos: Game_Pos
	for line, j in lines {
		if len(line) == 0 do break
		line := strings.split(line, "")
		s_pos := contains_at(line, "S")
		if s_pos != -1 {
			starting_pos.y = j
			starting_pos.x = s_pos
		}
		append(&game_map, line)
	}
	print_game_map(game_map)
	find_valid_moves_for_starting_point(game_map, &starting_pos)

	prev_mov := starting_pos.valid_moves[0]
	curr_mov := prev_mov
	curr_pos := get_next_pos(prev_mov, starting_pos, game_map)
	visited_nodes := map[Vector2]int{}
	steps := 1
	for !(curr_pos.x == starting_pos.x && curr_pos.y == starting_pos.y) {
		curr_pos_vec := Vector2{curr_pos.x, curr_pos.y}
		fmt.println(game_map[curr_pos_vec.y][curr_pos_vec.x])
		visited_nodes[curr_pos_vec] = steps
		valid_moves := Turns[game_map[curr_pos.y][curr_pos.x]]
		temp := curr_mov
		curr_mov = get_next_mov(valid_moves, curr_mov)
		prev_mov = temp
		curr_pos = get_next_pos(curr_mov, curr_pos, game_map)
		fmt.println(curr_pos)
		steps += 1
	}
	prev_mov = starting_pos.valid_moves[1]
	//fmt.println(starting_pos)
	curr_mov = prev_mov
	curr_pos = get_next_pos(prev_mov, starting_pos, game_map)
	steps = 1
	for false && !(curr_pos.x == starting_pos.x && curr_pos.y == starting_pos.y) {
		curr_pos_vec := Vector2{curr_pos.x, curr_pos.y}
		fmt.println(game_map[curr_pos_vec.y][curr_pos_vec.x])
		if curr_pos_vec in visited_nodes && steps < visited_nodes[curr_pos_vec] do visited_nodes[curr_pos_vec] = steps
		valid_moves := Turns[game_map[curr_pos.y][curr_pos.x]]
		temp := curr_mov
		curr_mov = get_next_mov(valid_moves, curr_mov)
		prev_mov = temp
		curr_pos = get_next_pos(curr_mov, curr_pos, game_map)
		steps += 1
	}
	max := 0
	for k, v in visited_nodes {
		fmt.println(v)
		if max < v do max = v
	}
	fmt.println(max)

}
