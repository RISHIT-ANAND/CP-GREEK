fn main() {
    let input = String::from("Hello, World!");
    let reversed = reverse_string(&input);
    println!("Original: {}", input);
    println!("Reversed: {}", reversed);
}

fn reverse_string(input: &str) -> String {
    if input.is_empty() {
        String::new()
    } else {
        let first_char = input.chars().next().unwrap();
        let remaining_chars = &input[1..];
        let reversed = reverse_string(remaining_chars);
        format!("{}{}", reversed, first_char)
    }
}
