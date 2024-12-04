def process_data():
    # Equivalent to the original array initialization
    v5 = [
        -76, 58, -27, 34, 41, -75, -110, -42, -92, 94,
        -86, -92, -76, 75, 107, -46, 46, -83, -83, -101,
        -42, 29, -68, 84, 23, -83, 63, 120, -23, -91,
        -108, 126, -23, 112, -47, -83, -113, 127, -102, -67,
        -1, -60, -11, -11, -23, -105, -12, -76, 33, -3,
        -14, 51, -11, -7
    ]
    
    # XOR operation with 0x53 for first 40 elements
    v3 = 0
    for i in range(40):
        # Convert to unsigned 8-bit integer (0-255 range) 
        # Equivalent to (unsigned __int8) in C
        v5[i] = (v5[i] ^ 0x53) & 0xFF
        v3 += v5[i]
    
    return v3

# Example usage
result = process_data()
print(f"Checksum (v3): {result}")
