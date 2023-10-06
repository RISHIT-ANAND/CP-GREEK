def display_multiplication_table(n, current=1):
    if current <= 10:
        print(f"{n} x {current} = {n * current}")
        display_multiplication_table(n, current + 1)

# Example usage:
n = 5  # Replace with the desired number for the multiplication table
print(f"Multiplication table for {n} (first 10 entries):")
display_multiplication_table(n)
