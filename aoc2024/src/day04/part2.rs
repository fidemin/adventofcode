use std::fs;

fn get_char_at(content_matrix: &Vec<&str>, y: usize, x: usize) -> char {
    return content_matrix.get(y).unwrap().chars().nth(x).unwrap();
}

fn check_xmas_chars(char1: char, char2: char) -> bool {
    return (char1 == 'M' && char2 == 'S') || (char1 == 'S' && char2 == 'M');
}

fn check_xmas(content_matrix: &Vec<&str>, y: usize, x: usize) -> bool {
    if y == 0 || y == content_matrix.len() - 1 || x == 0 || x == content_matrix.get(0).unwrap().len() - 1 {
        return false;
    }

    let cuurent_char = get_char_at(content_matrix, y, x);
    if cuurent_char != 'A' {
        return false;
    }

    let top_left_char = get_char_at(content_matrix, y - 1, x - 1);
    let bottom_right_char = get_char_at(content_matrix, y + 1, x + 1);
    if !(check_xmas_chars(top_left_char, bottom_right_char)) {
        return false;
    }

    let top_right_char = get_char_at(content_matrix, y - 1, x + 1);
    let bottom_left_char = get_char_at(content_matrix, y + 1, x - 1);
    if !(check_xmas_chars(top_right_char, bottom_left_char)) {
        return false;
    }
    
    return true;
    
}

fn count_xmas(content_matrix:&Vec<&str>) -> i32 {
    let mut count = 0;
    let m = content_matrix.len();
    let n = content_matrix.get(0).unwrap().len();

    for y in 0..m {
        for x in 0..n {
            if check_xmas(content_matrix, y, x) {
                count += 1;
            }
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
    result += count_xmas(&content_matrix);
    println!("Result: {}", result);
}