import os
import numpy as np

file = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = file.readlines()
indexes = []
for index, line in enumerate(lines):
    if ':' in line:
        indexes.append(index)
seeds = lines[0].split()[1:]


def get_from_dict(desc, key):
    for line in desc:
        values = line.replace('\n', '').split()
        values_start = int(values[0])
        keys_start = int(values[1])
        length = int(values[2])
        if key < keys_start or key > keys_start + length:
            continue        

        diff = key - keys_start;

        return values_start + diff;
    
    return key


i = 1
seeds_to_soil = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
soil_to_fertilizer = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
fertilizer_to_water = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
water_to_light = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
light_to_temperature = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
temperature_to_humidity = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
humidity_to_location = lines[indexes[i] + 1:]



def get_location(seed):
    soil = get_from_dict(seeds_to_soil, seed)
    fertilizer = get_from_dict(soil_to_fertilizer, soil)
    water = get_from_dict(fertilizer_to_water, fertilizer)
    light = get_from_dict(water_to_light, water)
    temperature = get_from_dict(light_to_temperature, light)
    humidity = get_from_dict(temperature_to_humidity, temperature)
    return get_from_dict(humidity_to_location, humidity)

locations = []
min_location = int(10 ** 100000)
i = 0
min_seed = 0
# while i < len(seeds):
array = np.arange(3283824077 - 2, 3283824077 + 2, 1, dtype=np.int64)
vectorized_func = np.vectorize(get_location)
result_array = vectorized_func(array)
print(get_location(3283824077))
print(result_array)
# for j in range(len(result_array)):
#     if result_array[j] < min_location:
#         min_location = result_array[j]
#         min_seed = array[j] 

    # i += 2
    # print(i / len(seeds) * 100, " %")

# array = np.arange(min_seed - 10000, min_seed + 10000, 1, dtype=np.float64)
# vectorized_func = np.vectorize(get_location)
# result_array = vectorized_func(array)
# print(result_array.min())


# for seed in seeds:
#     locations.append(get_location(int(seed)))


# print(locations)
# print(min(locations))

# print(min_location)
# print(min_seed)