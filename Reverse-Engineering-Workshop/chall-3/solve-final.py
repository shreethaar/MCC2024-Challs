def validate_checksum(input_str):
    v5, v4 = 0, 0
    for char in input_str:
        v5 = (ord(char) + v5) % 255
        v4 = (v5 + v4) % 255
    return v5, v4

def find_string(target_v4, target_v5, min_length):
    import itertools
    import string
    
    # Use printable characters, avoiding control characters
    printable_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Try different approaches to generate the string
    for length in range(min_length, min_length + 5):  # Allow slight variation in length
        # Try exhaustive search with different strategies
        for prefix_len in range(length):
            # Generate all possible combinations
            for chars in itertools.product(printable_chars, repeat=length):
                chars_list = list(chars)
                
                # Reset checksum calculation
                v5, v4 = 0, 0
                for char in chars_list:
                    char_ord = ord(char)
                    v5 = (v5 + char_ord) % 255
                    v4 = (v5 + v4) % 255
                
                # Check if we've hit the target
                if v5 == target_v5 and v4 == target_v4:
                    generated_str = ''.join(chars_list)
                    print(f"Generated string: {generated_str}")
                    print(f"Length: {len(generated_str)}")
                    print(f"Checksum V5: {v5} (target: {target_v5})")
                    print(f"Checksum V4: {v4} (target: {target_v4})")
                    return generated_str
    
    raise ValueError("Could not generate a valid string.")

# Parameters from the original code
v4_target = 126  # 0x7E
v5_target = 239  # 0xEF
min_length = 16  # Minimum length as required by strlen(lpString) > 15

result = find_string(v4_target, v5_target, min_length)
