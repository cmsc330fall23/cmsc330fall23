pub fn sum_evens(i: i32, j: i32) -> i32 {
    let mut sum = 0; // Change sum to mut

    for k in i..j {
        if k % 2 == 0 {
            sum += k;
        }
    }

    sum
}

pub fn distance((ax, ay): (f64, f64), (bx, by): (f64, f64)) -> f64 {
    ((bx - ax).powi(2) + (by - ay).powi(2)).sqrt() // should be powi; i is for integer function, f is for float)
}

pub fn raise_1(arr: &mut [i32]) {
    for i in arr {
        *i += 1; // i is a reference, so should be *i)
    }
}

pub fn add_hello(a: &mut String) {
    // Make it &mut

    a.push_str("hello");
}

pub fn create_hello_world() -> String {
    let mut s = String::from("");

    add_hello(&mut s); // &mut s and make add_hello(a: &mut String))

    s.push_str("world");

    return s;
}

pub fn get_first_elem(a: &Vec<u32>) -> u32 {
    if (a.len() == 0) {
        return 0;
    }

    return *a.get(0).unwrap(); //Unwrap the some and dereference
}
