
use std::env;

mod day03;
mod day04;

fn main() {
    let day_ = env::args().nth(1).expect("No day provided");
    let part_ = env::args().nth(2).expect("No part provided");
    let file_path = env::args().nth(3).expect("No file path provided");
    if day_ == "day03" {
        if part_ == "part1" {
            day03::part1::solve(&file_path);
        } else if part_ == "part2" {
            day03::part2::solve(&file_path);
        } else {
            println!("Invalid part provided");
        }
    } else if day_ == "day04" {
        if part_ == "part1" {
            day04::part1::solve(&file_path);
        } else if part_ == "part2" {
            // day04::part2::solve(&file_path);
        } else {
            println!("Invalid part provided");
        }
    } else {
        println!("Invalid day provided");
    }
}
