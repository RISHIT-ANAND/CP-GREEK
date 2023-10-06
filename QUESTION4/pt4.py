def count_bits_needed(N):
    # Special case: If N is 0, it requires only 1 bit.
    if N == 0:
        return 1
    
    # Initialize a counter for bits and a divisor.
    bits_count = 0
    divisor = 1
    
    # Increment the divisor by a power of 2 until it's greater than or equal to N.
    while divisor <= N:
        divisor *= 2
        bits_count += 1
    
    return bits_count

# Example usage:
N = 15  # Replace with the decimal number you want to convert to binary
bits_needed = count_bits_needed(N)
print(f"Number of bits needed to store {N} as a binary number: {bits_needed}")
