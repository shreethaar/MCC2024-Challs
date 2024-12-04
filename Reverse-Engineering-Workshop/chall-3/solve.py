def sub_403A20(string):
    v5 = 0
    v4 = 0
    for char in string:
        v5 = (ord(char) + v5) % 255
        v4 = (v5 + v4) % 255
    return (v4 << 8) | v5

# Hardcoded test string you used
test_string = "AAAAAAAAAAAAAAAA"

# Calculate checksum
checksum = sub_403A20(test_string)
print(f"String: {test_string}")
print(f"Checksum: {checksum}")
print(f"Hex Checksum: 0x{checksum:04X}")
