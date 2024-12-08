use std::fs;
use std::env;
use std::collections::HashMap;


fn main() {
    let key = "FILE_PATH";

    let file_path = env::var(key).expect("FILE_PATH is required");

    let contents = fs::read_to_string(file_path).expect("Reading file failed");

    let mut left_list: Vec<i32> = Vec::new();
    let mut right_list: Vec<i32> = Vec::new();

    for line in contents.lines() {
        // e.g. line "1 2"
        let mut iter = line.split_whitespace();
        let left = iter.next().unwrap().parse::<i32>().unwrap();
        let right = iter.next().unwrap().parse::<i32>().unwrap();

        left_list.push(left);
        right_list.push(right);
    }

    let mut count_map: HashMap<i32, i32> = HashMap::new();

    // iterate vector
    for i in 0..left_list.len() {
        let value = right_list.get(i).unwrap();
        let count = count_map.entry(*value).or_insert(0);
        *count += 1;
    }

    let mut result = 0;

    for i in 0..left_list.len() {
        let value = left_list.get(i).unwrap();

        if let Some(&count) = count_map.get(value) {
            result += count * value;
        }
    }

    println!("{result}");
}
