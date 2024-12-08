use std::fs;
use std::env;

fn is_safe(is_skip: bool, skip_p: Option<usize>, levels: &Vec<i32>) -> bool {
    // safe: all levels are increasing or all levels are decreasing
    // length of levels is 5. fixed

    let mut levels = levels.clone();

    if is_skip {
        levels.remove(skip_p.unwrap());
    }

    let first_level = levels.get(0).unwrap();
    let second_level = levels.get(1).unwrap();

    if first_level == second_level {
        return false;
    }

    if (first_level - second_level).abs() > 3 {
        return false;
    }

    for i in 1..levels.len() - 1 {
        let this_level = levels.get(i).unwrap();
        let next_level = levels.get(i + 1).unwrap();

        if first_level < second_level {
            if this_level >= next_level {
                return false;
            }
        } else {
            if this_level <= next_level {
                return false;
            }
        }

        let abs_diff = (this_level - next_level).abs();
        if abs_diff > 3 {
            return false;
        }

    }

    return true;
}

fn main() {
    let key = "FILE_PATH";

    let file_path = env::var(key).expect("FILE_PATH is required");

    let contents = fs::read_to_string(file_path).expect("Reading file failed");


    let mut safe_count = 0;
    for line in contents.lines() {
        // e.g. line = "1 3 4 2 5"

        let iter = line.split_whitespace();

        let mut levels: Vec<i32> = Vec::new();

        for value in iter {
            let number = value.parse::<i32>().unwrap();
            levels.push(number);
        }

        if is_safe(false, None, &levels) {
            safe_count += 1;
        } else {
            for i in 0..levels.len() {
                if is_safe(true, Some(i), &levels) {
                    safe_count += 1;
                    break;
                }
            }
        }
    }

    println!("{safe_count}");
}
