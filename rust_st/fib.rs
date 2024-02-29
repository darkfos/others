fn main() {
    fibonachi(4);
}


fn fibonachi(number_stop: i16) {
    //Счетчик
    let mut start = 0;

    //Начало последовательности фибоначчи
    let mut fib_on = 0;
    let mut fib_tw = 1;

    //Вывод первух 2=х значений
    println!("Number: {fib_on}");
    println!("Number: {fib_tw}");

    loop {
        if start == number_stop - 2 {
            break;
        }
        
        let result_number = fib_on + fib_tw;
        println!("Number: {}", result_number);
        fib_on = fib_tw;
        fib_tw = result_number;
        start += 1;
    }
}