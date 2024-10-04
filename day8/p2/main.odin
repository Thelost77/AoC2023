package main

import "core:fmt"
import "core:math"
import "core:os"
import "core:slice"
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

get_starting_nodes :: proc(list_of_nodes: []string) -> [dynamic]Node {
	nodes: [dynamic]Node
	for node in list_of_nodes {
		if len(node) == 0 do continue
		if node[2] == 'A' do append(&nodes, get_node(list_of_nodes, node[:3]))
	}
	return nodes
}

are_currents_done :: proc(currents: [dynamic]Node) -> bool {
	are_done := true
	for curr in currents {
		if curr.name[2] != 'Z' {
			are_done = false
			break
		}
	}
	return are_done
}

Cycle :: struct {
	operations: int,
	cycle:      int,
}


main :: proc() {
	file, _ := os.open("../test3.txt")
	//file, _ := os.open("../input.txt")
	defer os.close(file)

	data, _ := os.read_entire_file(file)

	lines := strings.split(string(data), "\n")

	instructions := lines[0]
	list_of_nodes := lines[2:]

	currents := get_starting_nodes(list_of_nodes)
	cycles: [dynamic]Cycle

	for &curr in currents {
		counter := 0
		for curr.name[2] != 'Z' {
			for curr_instr in instructions {
				if curr.name[2] == 'Z' do break
				if curr_instr == 'R' {
					curr = get_node(list_of_nodes, curr.right)
				}
				if curr_instr == 'L' {
					curr = get_node(list_of_nodes, curr.left)
				}
				counter += 1
			}
		}
		fmt.println(curr.name, " -> ", counter)
		cnt := 0
		for {
			for curr_instr in instructions {
				if curr_instr == 'R' {
					curr = get_node(list_of_nodes, curr.right)
				}
				if curr_instr == 'L' {
					curr = get_node(list_of_nodes, curr.left)
				}
				if curr.name[2] == 'Z' do break
			}
			cnt += 1
			if curr.name[2] == 'Z' do break
		}
		fmt.println(curr.name, " -> ", cnt)
		append(&cycles, Cycle{counter, cnt})
	}


	// Funkcja obliczająca NWD (Greatest Common Divisor)
	gcd :: proc(a: int, b: int) -> int {
		a := a
		b := b
		for b != 0 {
			a, b = b, a % b
		}
		return a
	}

	// Funkcja obliczająca LCM (Least Common Multiple)
	lcm :: proc(a, b: int) -> int {
		return abs(a * b) / gcd(a, b)
	}

	max := 0
	for cycle in cycles {
		if cycle.operations > max do max = cycle.operations
	}

	i := 0
	o1 := lcm(cycles[i].cycle, cycles[i + 1].cycle)
	o2 := lcm(o1, cycles[i + 2].cycle)
	o3 := lcm(o2, cycles[i + 3].cycle)
	o4 := lcm(o3, cycles[i + 4].cycle)
	o5 := lcm(o4, cycles[i + 5].cycle)
	out := lcm(o5, max)
	fmt.println(out)


}
