
def reverse_transformation(target=-224863074):
    # We'll use a brute-force approach with some intelligent constraints
    for v4 in range(0, 100000):  # Reasonable range of inputs
        # Reproduce the exact transformation
        step1 = v4 ^ 2986378239
        step2 = step1 >> 9
        
        intermediate = ((step2 - 219482042) ^ 213422132) + step2 - 6059910
        
        # Rotate left (reverse of right rotation)
        rotated = ((intermediate << 1) | (intermediate >> 31)) & 0xFFFFFFFF
        rotated = ((rotated << 25) | (rotated >> 7)) & 0xFFFFFFFF
        
        final = rotated ^ 2389123371
        
        # Check if we've found the target
        if final == target:
            return v4
    
    return None

# Find the solution
result = reverse_transformation()
print(f"Input that satisfies the condition: {result}")
