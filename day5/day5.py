import os

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

locations = []
new_seeds = []
i = 0
while i < len(seeds):
    for j in range(int(seeds[i + 1])):
        new_seeds.append(int(seeds[i]) + j)
    i += 2

for seed in seeds:
    soil = get_from_dict(seeds_to_soil, int(seed))
    fertilizer = get_from_dict(soil_to_fertilizer, soil)
    water = get_from_dict(fertilizer_to_water, fertilizer)
    light = get_from_dict(water_to_light, water)
    temperature = get_from_dict(light_to_temperature, light)
    humidity = get_from_dict(temperature_to_humidity, temperature)
    location = get_from_dict(humidity_to_location, humidity)
    locations.append(location)

new_locations = []
for seed in new_seeds:
    soil = get_from_dict(seeds_to_soil, int(seed))
    fertilizer = get_from_dict(soil_to_fertilizer, soil)
    water = get_from_dict(fertilizer_to_water, fertilizer)
    light = get_from_dict(water_to_light, water)
    temperature = get_from_dict(light_to_temperature, light)
    humidity = get_from_dict(temperature_to_humidity, temperature)
    location = get_from_dict(humidity_to_location, humidity)
    new_locations.append(location)

print(locations)
print(min(locations))

print(new_locations)
print(min(new_locations))