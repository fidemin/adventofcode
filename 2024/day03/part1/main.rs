
use regex::Regex;

fn main() {
    let contents = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
    let regex = Regex::new(r"mul\([1-9]\d{0,2}\)").unwrap();

    for cap in regex.captures_iter(contents) {
        println!("{}", cap.get(0).unwrap().as_str());
    } 
    


    

}
