def generate_checksum(string):
    """
    Reimplementation of the sub_403A20 checksum algorithm
    
    Args:
    string (str): Input string to generate checksum for
    
    Returns:
    int: 16-bit checksum (v5 | (v4 << 8))
    """
    v5 = 0
    v4 = 0
    
    for char in string:
        # Convert char to unsigned byte
        byte = ord(char) & 0xFF
        
        # Calculate v5
        v5 = (byte + v5) % 255
        
        # Calculate v4
        v4 = (v5 + v4) % 255
    
    # Combine v5 and v4 into a 16-bit value
    return v5 | (v4 << 8)

def find_matching_string(target_checksum, min_length=16, max_length=20):
    """
    Attempt to find a string that matches the target checksum
    
    Args:
    target_checksum (int): The 16-bit checksum to match
    min_length (int): Minimum length of the string to try
    max_length (int): Maximum length of the string to try
    
    Returns:
    str or None: A string that matches the checksum, or None if not found
    """
    # Define character set (printable ASCII characters)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?'
    
    from itertools import product
    import time
    
    start_time = time.time()
    attempts = 0
    
    # Start with strings of minimum length
    for length in range(min_length, max_length + 1):
        # Generate all possible combinations
        for combo in product(chars, repeat=length):
            test_string = ''.join(combo)
            attempts += 1
            
            # Check if the checksum matches
            if generate_checksum(test_string) == target_checksum:
                end_time = time.time()
                print(f"Found after {attempts} attempts in {end_time - start_time:.2f} seconds")
                return test_string
            
            # Optional: print progress to show the script is working
            if attempts % 100000 == 0:
                print(f"Attempted {attempts} combinations...")
    
    return None

# Find string with checksum 6252
result = find_matching_string(6252)

if result:
    print(f"Found matching string: {result}")
    print(f"Checksum verification: {generate_checksum(result) == 6252}")
else:
    print("No matching string found")
