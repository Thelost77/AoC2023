import os
import numpy as np

file = open(os.path.dirname(__file__) + '/input.txt', 'r')

input = file.readlines()
times = input[0].split()[1:]
distances = input[1].split()[1:]

all_time = ''
for time in times:
    all_time += time

all_distance = ''
for distance in distances:
    all_distance += distance

times = [all_time]
distances = [all_distance]

print(times, distances)


output = 1
for j in range(len(times)):
    time = int(times[j])
    possible_ways = 0
    for i in range(1, time):
        vel = i
        time_to_go = time - i
        distance_to_beat = int(distances[j])
        if vel * time_to_go > distance_to_beat:
            possible_ways += 1
    output *= possible_ways





print(output)