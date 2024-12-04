def sub_4036C0(input_word):
    # Hardcoded array similar to v5 in the original function
    v5 = [
        -76, 58, -27, 34, 41, -75, -110, -42, -92, 94,
        -86, -92, -76, 75, 107, -46, 46, -83, -83, -101,
        -42, 29, -68, 84, 23, -83, 63, 120, -23, -91,
        -108, 126, -23, 112, -47, -83, -113, 127, -102, -67,
        -1, -60, -11, -11, -23, -105, -12, -76, 33, -3,
        -14, 51, -11, -7
    ]
    
    v3 = 0  # Running sum
    
    # XOR first 40 bytes with 0x53 and calculate sum
    for i in range(40):
        # Ensure byte stays in 0-255 range
        v5[i] = (v5[i] ^ 0x53) & 0xFF
        v3 += v5[i]
    
    # Return the 6th element of the input (equivalent to this[6])
    return input_word[6]

# Demonstration
test_input = [33] * 16# Example input
result = sub_4036C0(test_input)
print(f"Result: {result}")
