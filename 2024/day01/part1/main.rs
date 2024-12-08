use std::fs;
use std::env;


fn main() {
    let key = "FILE_PATH";

    let file_path = env::var(key).expect("FILE_PATH is required");

    let contents = fs::read_to_string(file_path).expect("Reading file failed");

    let mut left_list: Vec<i32> = Vec::new();
    let mut right_list: Vec<i32> = Vec::new();

    let mut length = 0;
    for line in contents.lines() {
        // e.g. line "1 2"
        let mut iter = line.split_whitespace();
        let left = iter.next().unwrap().parse::<i32>().unwrap();
        let right = iter.next().unwrap().parse::<i32>().unwrap();

        left_list.push(left);
        right_list.push(right);

        length += 1;
    }

    left_list.sort();
    right_list.sort();

    let mut result = 0;

    for i in 0..length {
        let left = left_list.get(i).unwrap();
        let right = right_list.get(i).unwrap();

        let abs_diff = (left - right).abs();
        result += abs_diff;
    }

    println!("{result}");
}
