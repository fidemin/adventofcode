use std::fs;

use regex::Regex;

fn parse_and_return_mult_contents(contents: &str) -> i32 {
    let regex = Regex::new(r"mul\(([1-9]\d{0,2})\,([1-9]\d{0,2})\)").unwrap();

    let mut result = 0;
    for cap in regex.captures_iter(contents) {
        let first_num = cap.get(1).unwrap().as_str().parse::<i32>().unwrap();
        let second_num = cap.get(2).unwrap().as_str().parse::<i32>().unwrap();
        result += first_num * second_num;
    } 
    return result;
}

fn parse_file(file_path: &str) -> String {
    let contents = fs::read_to_string(file_path).expect("Reading file failed");
    return contents;
}

pub fn solve(file_path: &str) {
    let all_contents = parse_file(file_path);
    let contents = all_contents.trim();
    let result = parse_and_return_mult_contents(contents);
    println!("Result: {}", result);
}
