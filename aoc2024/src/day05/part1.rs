
use core::num;
use std::fs;
use std::collections::HashMap;
use std::collections::HashSet;

fn check_single_pair(page_ordering_rule_map: &HashMap<i32, HashSet<i32>>, num1: i32, num2: i32) -> bool {
    if page_ordering_rule_map.contains_key(&num1) {
        let set = page_ordering_rule_map.get(&num1).unwrap();
        if set.contains(&num2) {
            return true;
        }
    }

    if page_ordering_rule_map.contains_key(&num2) {
        let set = page_ordering_rule_map.get(&num2).unwrap();
        if set.contains(&num1) {
            return false;
        }
    }

    // no rule found
    return true;
}


fn check_satisfy_rule(rule_map: &HashMap<i32, HashSet<i32>>, page_update: &Vec<i32>) -> bool {
    let result = true;

    let n = page_update.len();

    for i in 0..n-1 {
        for j in i+1..n {
            let first_num = page_update[i];
            let second_num = page_update[j];

            if !check_single_pair(rule_map, first_num, second_num) {
                return false;
            }
        }
    }

    return true;
}

fn page_ordering_rules_maps(page_ordering_rules: &Vec<String>) -> HashMap<i32, HashSet<i32>> {
    let mut page_ordering_rules_map: HashMap<i32, HashSet<i32>> = HashMap::new();

    for rule_string in page_ordering_rules {
        let rule: Vec<&str> = rule_string.split("|").collect();
        let first_num = rule[0].parse::<i32>().unwrap();
        let second_num = rule[1].parse::<i32>().unwrap();

        if page_ordering_rules_map.contains_key(&first_num) {
            let set = page_ordering_rules_map.get_mut(&first_num).unwrap();
            set.insert(second_num);
        } else {
            let mut set = HashSet::new();
            set.insert(second_num);
            page_ordering_rules_map.insert(first_num, set);
        }
    }
    println!("{:?}", page_ordering_rules_map);
    return page_ordering_rules_map;
}

fn parse_page_update(page_update: String) -> Vec<i32> {
    let mut page_update_vec : Vec<i32> = Vec::new();
    let strs: Vec<&str> = page_update.split(",").collect();

    for str in strs {
        let num = str.parse::<i32>();
        page_update_vec.push(num.unwrap());
    }

    return page_update_vec;
}

fn sum_of_all_valid_middle_nums(page_ordering_rules: &Vec<String>, page_updates: &Vec<String>) -> i32 {
    let mut sum = 0;
    let page_ordering_rules_map = page_ordering_rules_maps(page_ordering_rules);

    for page_update in page_updates {
        let page_update_vec = parse_page_update(page_update.to_string());
        // println!("{:?}", page_update_vec);

        if check_satisfy_rule(&page_ordering_rules_map, &page_update_vec) {
            sum += page_update_vec[page_update_vec.len() / 2];
        }

    }
    return sum;
}

fn parse_file(file_path: &str) -> (Vec<String>, Vec<String>) {
    let contents = fs::read_to_string(file_path).expect("Reading file failed");
    let mut is_first = true;
    let mut page_ordering_rules = Vec::new();
    let mut page_updates = Vec::new();

    for content in contents.lines() {
        // println!("{}", content);
        if content == "" {
            is_first = false;
            continue;
        }

        if is_first {
            page_ordering_rules.push(content.to_string());
        } else {
            page_updates.push(content.to_string());
        }
    }
    return (page_ordering_rules, page_updates);
}

pub fn solve(file_path: &str) {
    let (page_ordering_rules, page_updates) = parse_file(file_path);
    println!("rules: {}", page_ordering_rules.len());
    println!("updates: {}", page_updates.len());
    let result = sum_of_all_valid_middle_nums(&page_ordering_rules, &page_updates);
    println!("Result: {}", result);
}