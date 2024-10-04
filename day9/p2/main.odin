package main

import "core:fmt"
import "core:os"
import "core:strconv"
import "core:strings"

find_next_value_in_numbers :: proc(numbers: [dynamic]int) -> int {
	return 0
}

sum :: proc(numbers: [dynamic]int) -> int {
	sum := 0
	for num in numbers {
		sum += num
	}
	return sum
}

is_all_zero :: proc(numbers: [dynamic]int) -> bool {
	for n in numbers {
		if n != 0 do return false
	}
	return true
}

main :: proc() {
	file, _ := os.open("../input.txt")
	//file, _ := os.open("../test.txt")
	defer os.close(file)

	data, _ := os.read_entire_file(file)

	lines := strings.split(string(data), "\n")
	next_values: [dynamic]int
	for line in lines {
		if len(line) == 0 do break

		numbers: [dynamic]int
		for num in strings.split(line, " ") {
			n, _ := strconv.parse_int(num)
			append(&numbers, n)
		}

		steps: [dynamic][dynamic]int
		curr_step := 0

		append(&steps, numbers)

		for !is_all_zero(steps[curr_step]) {
			next_step: [dynamic]int
			for i := len(steps[curr_step]) - 1; i > 0; i -= 1 {
				inject_at(&next_step, 0, steps[curr_step][i] - steps[curr_step][i - 1])
			}
			append(&steps, next_step)
			curr_step += 1

		}
		next_element := 0
		for i := len(steps) - 1; i > 0; i -= 1 {
			step := steps[i]
			next_step := steps[i - 1]
			next_element = next_step[0] - step[0]
			inject_at(&steps[i - 1], 0, next_element)
		}

		append(&next_values, next_element)
	}
	fmt.println(next_values)
	fmt.println(sum(next_values))

}
