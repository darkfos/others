
fn main() {

    //Точка входа
    let number_one: i16 = 95;
    let number_two: i16 = 95;

    println!("Number one {}", number_one);
    println!("Number two {}", number_two);
    
    let number_three: i16 = (number_one + number_two).into();
    println!("Sum number {}", number_three);

    if number_one > number_two {
        print!("Number max: {}", number_one);
    } else if number_one == number_two {
        print!("Number is equals");
    } else {
        print!("Number max: {}", number_two);
    }
}