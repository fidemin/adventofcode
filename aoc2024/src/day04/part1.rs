use std::fs;

fn check_at_for_target_with_direction(target: &str, content_matrix: &Vec<&str>, y: usize, x: usize, y_direction: i32, x_direction: i32, debug: bool) -> bool {
    let m = content_matrix.len();
    let n = content_matrix.get(0).unwrap().len();

    let mut current_y = y as i32;
    let mut current_x = x as i32;

    let mut current_target_index = 0;
    let mut final_chars = Vec::new();

    while current_y >= 0 && current_y < m as i32 && current_x >= 0 && current_x < n as i32 && current_target_index < target.len() {
        let current_char = content_matrix.get(current_y as usize).unwrap().chars().nth(current_x as usize).unwrap();
        let current_target_char = target.chars().nth(current_target_index).unwrap();
        if current_char != current_target_char {
            break;
        }
        final_chars.push(current_char);

        current_y = current_y + y_direction;
        current_x = current_x + x_direction;
        current_target_index = current_target_index + 1;
    }

    let result = current_target_index == target.len();
    if debug && result {
        println!("Final chars: y={}, x={}, directions=({}, {}) chars={:?}, result={}",y, x, y_direction, x_direction, final_chars, result);
    }
    return result;
}

fn count_at_for_target(target: &str, content_matrix: &Vec<&str>, y: usize, x: usize) -> i32 {
    let mut count = 0;

    for y_direction in -1..2 { // -1, 0, 1
        for x_direction in -1..2 { // -1, 0, 1
            if y_direction == 0 && x_direction == 0 {
                continue;
            }
            let result = check_at_for_target_with_direction(target, content_matrix, y, x, y_direction, x_direction, false);
            if result {
                count = count + 1;
            }
        }
    }

    return count;
}

fn count_target(target: &str, content_matrix:&Vec<&str>) -> i32 {
    let mut count = 0;
    let m = content_matrix.len();
    let n = content_matrix.get(0).unwrap().len();

    let mut y: usize = 0;
    let mut x: usize = 0;

    while y < m && x < n {
        count += count_at_for_target(target, &content_matrix, y, x);

        x = x + 1;
        if x >= n {
            x = x - n;
            y = y + 1;
        }

    }
    return count;
}

fn parse_file(file_path: &str) -> String {
    let contents = fs::read_to_string(file_path).expect("Reading file failed");
    return contents;
}

pub fn solve(file_path: &str) {
    let all_contents = parse_file(file_path);
    let mut content_matrix: Vec<&str> = Vec::new(); 
    for content in all_contents.lines() {
        content_matrix.push(content);
    }

    let mut result = 0;
    result += count_target("XMAS", &content_matrix);
    println!("Result: {}", result);
    // result += count_target("SAMX", &content_matrix);
    // println!("Result: {}", result);

}