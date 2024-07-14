import random
import string

def generate_random_hex_chars(num_chars):
    # Define the set of hexadecimal characters
    hex_chars = string.hexdigits.lower()
    
    # Generate the random string
    random_hex_string = ''.join(random.choices(hex_chars, k=num_chars))
    
    return random_hex_string

# Example usage
num_chars = int(input("Enter the number of characters for the hexadecimal string: "))
random_hex_string = generate_random_hex_chars(num_chars)
print("Generated random hexadecimal string:", random_hex_string)
