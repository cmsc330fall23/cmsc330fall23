pub fn sum_evens(i: i32, j: i32) -> i32 {
    let sum = 0;

    for k in i..j {
        if k % 2 == 0 {
            sum += k;
        }
    }

    sum
}

pub fn distance((ax, ay): (f64, f64), (bx, by): (f64, f64)) -> f64 {
    ((bx - ax).powf(2) + (by - ay).powf(2)).sqrt()
}

pub fn raise_1(arr: &mut [i32]) {
    for i in arr {
        i += 1;
    }
}

pub fn add_hello(a: String) {
    a.push_str("hello");
}

pub fn create_hello_world() -> String {
    let mut s = String::from("");

    add_hello(s);
    s.push_str("world");

    return s;
}

pub fn get_first_elem(a: &Vec<u32>) -> u32 {
    if a.len() == 0 {
        return 0;
    }

    return a.get(0);
}
