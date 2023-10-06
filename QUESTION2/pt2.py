def reverse_string(input_str):
    # Base case: if the string is empty or has only one character, it's already reversed
    if len(input_str) <= 1:
        return input_str
    else:
        # Recursive case: reverse the substring starting from the second character
        # and append the first character at the end
        return reverse_string(input_str[1:]) + input_str[0]

# Example usage:
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Original String:", input_string)
print("Reversed String:", reversed_string)
