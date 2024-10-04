package main

import "core:fmt"
import "core:os"
import "core:strings"

Node :: struct {
	name:  string,
	left:  string,
	right: string,
}

get_node :: proc(list_of_nodes: []string, node_name: string) -> Node {
	for nodes in list_of_nodes {
		if nodes[:3] == node_name {
			return Node{node_name, nodes[7:10], nodes[12:15]}
		}
	}
	return Node{}
}


main :: proc() {
	//file, _ := os.open("../test1.txt")
	//file, _ := os.open("../test2.txt")
	file, _ := os.open("../input.txt")
	defer os.close(file)

	data, _ := os.read_entire_file(file)

	lines := strings.split(string(data), "\n")

	instructions := lines[0]
	list_of_nodes := lines[2:]

	curr := get_node(list_of_nodes, "AAA")
	instructions_count := 0

	for curr.name != "ZZZ" {
		for curr_instr in instructions {
			if curr.name == "ZZZ" do break
			if curr_instr == 'R' {
				curr = get_node(list_of_nodes, curr.right)
			}
			if curr_instr == 'L' {
				curr = get_node(list_of_nodes, curr.left)
			}
			instructions_count += 1
		}
	}
	fmt.println(instructions_count)
}
