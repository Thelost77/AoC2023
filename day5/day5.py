import os
import threading
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

def get_from_dict_reverse(desc, value):
    for line in desc:
        values = line.replace('\n', '').split()
        values_start = int(values[0])
        keys_start = int(values[1])
        length = int(values[2])
        if value < values_start or value > values_start + length:
            continue        

        diff = value - values_start;

        return keys_start + diff;
    
    return value

def get_smallest_location_and_range(desc):
    smallest_location = int(10 ** 100000)
    range = 0
    for line in desc:
        values = line.replace('\n', '').split()
        values_start = int(values[0])
        keys_start = int(values[1])
        length = int(values[2])

        if values_start < smallest_location or (values_start == smallest_location and range < length):
            smallest_location = values_start
            range = length

    return (smallest_location, range)


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

def get_seed(location):
    humidity = get_from_dict_reverse(humidity_to_location, location)
    temperature = get_from_dict_reverse(temperature_to_humidity, humidity)
    light = get_from_dict_reverse(light_to_temperature, temperature)
    water = get_from_dict_reverse(water_to_light, light)
    fertilizer = get_from_dict_reverse(fertilizer_to_water, water)
    soil = get_from_dict_reverse(soil_to_fertilizer, fertilizer)
    return get_from_dict_reverse(seeds_to_soil, soil)

locations = []
min_location = int(10 ** 100000)
i = 0
min_seed = 0

smallest, length = get_smallest_location_and_range(humidity_to_location)

def is_in_seeds(seeds, value):
    i = 0
    while i < len(seeds):
        begin = int(seeds[i])
        end = int(seeds[i]) + int(seeds[i + 1])
        if value >= begin and value < end:
            return True
        i += 2
    return False


print(get_seed(15880236))
# def vectorization(num):
#     seed = get_seed(num)
#     return is_in_seeds(seeds, seed)

# results = []
# def calculate(part, prev_part):
#     max = int((smallest + length) * part)
#     prev_max = int((smallest + length) * prev_part)
#     array = np.arange(prev_max,  max, 1)
#     print(len(array))
#     vectorized_func = np.vectorize(vectorization)
#     result_array = vectorized_func(array)
#     for i in range(len(result_array)):
#         if result_array[i] == True:
#             results.append(array[i])
#             return

# threads = []
# for i in range(1, 17):
#     t = threading.Thread(target=calculate, args=(i / 16, (i - 1) / 16))
#     t.daemon = True;
#     threads.append(t);

# for i in range(16):
#     threads[i].start()

# for i in range(16):
#     threads[i].join()

# print(results)


# for j in range(len(result_array)):
#     if result_array[j] < min_location:
#         min_location = result_array[j]
        # min_seed = array[j]
# minimum = result_array.min()
# if minimum < min_location:
#     min_location = minimum       

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