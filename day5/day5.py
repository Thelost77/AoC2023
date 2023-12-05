import os

file = open(os.path.dirname(__file__) + '/input.txt', 'r')
lines = file.readlines()
indexes = []
for index, line in enumerate(lines):
    if ':' in line:
        indexes.append(index)
seeds = lines[0].split()[1:]

def get_from_dict(dict, element):
    if element in dict:
        return dict[element]
    return element

i = 1
seeds_to_soil = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
soil_to_fertilizer = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
fertilizer_to_water = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
water_to_light = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
light_to_temperature = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
temperature_to_humidity = lines[indexes[i] + 1 : indexes[i + 1] - 1]; i += 1
humidity_to_location = lines[indexes[i] + 1:]

def create_dict(desc):
    dict = {}
    for line in desc:
        values = list(map(lambda x: int(x), line.replace('\n', '').split()))
        values_start = values[0]
        keys_start = values[1]
        length = values[2]

        for i in range(length):
            dict[keys_start + i] = values_start + i
    return dict

seeds_to_soil_dict = create_dict(seeds_to_soil)
soil_to_fertilizer_dict = create_dict(soil_to_fertilizer)
fertilizer_to_water_dict = create_dict(fertilizer_to_water)
water_to_light_dict = create_dict(water_to_light)
light_to_temperature_dict = create_dict(light_to_temperature)
temperature_to_humidity_dict = create_dict(temperature_to_humidity)
humidity_to_location_dict = create_dict(humidity_to_location)

locations = []

for seed in seeds:
    soil = get_from_dict(seeds_to_soil_dict, int(seed))
    fertilizer = get_from_dict(soil_to_fertilizer_dict, soil)
    water = get_from_dict(fertilizer_to_water_dict, fertilizer)
    light = get_from_dict(water_to_light_dict, water)
    temperature = get_from_dict(light_to_temperature_dict, light)
    humidity = get_from_dict(temperature_to_humidity_dict, temperature)
    location = get_from_dict(humidity_to_location_dict, humidity)
    locations.append(location)

print(locations)
print(min(locations))