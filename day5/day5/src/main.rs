use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::collections::HashMap;

fn get_from_dict(file: File, key: i64) -> i64 {
    for line in BufReader::new(file).lines() {
        let unwraped_line = line.unwrap();
        let values: Vec<&str> = unwraped_line.split_whitespace().collect();
        let values_start = values[0].parse::<i64>().unwrap();
        let keys_start = values[1].parse::<i64>().unwrap();
        let length = values[2].parse::<i64>().unwrap();

        if key < keys_start || key > keys_start + length {
            continue;
        }

        let diff = key - keys_start;

        return values_start + diff;
    }
    return key;
}

fn main() {
    let mut seeds = File::open("C:\\Projects\\AoC2023\\day5\\seeds.txt").unwrap();
    let mut seeds_to_soil = File::open("C:\\Projects\\AoC2023\\day5\\seeds_to_soil_dict.txt").unwrap();
    let mut soil_to_fertilizer = File::open("C:\\Projects\\AoC2023\\day5\\soil_to_fertilizer_dict.txt").unwrap();
    let mut fertilizer_to_water = File::open("C:\\Projects\\AoC2023\\day5\\fertilizer_to_water_dict.txt").unwrap();
    let mut water_to_light = File::open("C:\\Projects\\AoC2023\\day5\\water_to_light_dict.txt").unwrap();
    let mut light_to_temperature = File::open("C:\\Projects\\AoC2023\\day5\\light_to_temperature_dict.txt").unwrap();
    let mut temperature_to_humidity = File::open("C:\\Projects\\AoC2023\\day5\\temperature_to_humidity_dict.txt").unwrap();
    let mut humidity_to_location = File::open("C:\\Projects\\AoC2023\\day5\\humidity_to_location_dict.txt").unwrap();

    let locations = Vec::new();
    for line in BufReader::new(seeds).lines() {
        let line = line.unwrap();
        let seeds: Vec<&str> = line.split_whitespace().collect();
        for seed in seeds {
            let mut soil = get_from_dict(seeds_to_soil, seed.parse::<i64>().unwrap());
            let mut fertilizer = get_from_dict(soil_to_fertilizer, soil);
            let mut water = get_from_dict(fertilizer_to_water, fertilizer);
            let mut light = get_from_dict(water_to_light, water);
            let mut temperature = get_from_dict(light_to_temperature, light);
            let mut humidity = get_from_dict(temperature_to_humidity, temperature);
            let mut location = get_from_dict(humidity_to_location, humidity);
            locations.push(location);
        }
    }
    // create_dict(seeds_to_soil);
}
