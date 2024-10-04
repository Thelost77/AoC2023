package main

import "core:fmt"
import "core:os"
import "core:strings"

main :: proc() {
	file, _ := os.open("input.txt")
	defer os.close(file)

	data, _ := os.read_entire_file(file)

	lines := strings.split(string(data), "\n")

	for line in lines {
		parts := strings.split(line, " ")
		hand := parts[0]
		if len(parts) == 1 do break
	}

}
