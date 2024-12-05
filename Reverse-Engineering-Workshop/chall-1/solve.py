reference_bytes = [
    0x32, 0x00, 0x09, 0x06, 0x0A, 0x08, 0x00, 
    0x45, 0x11, 0x0A, 0x45, 0x28, 0x26, 
    0x26, 0x57, 0x55, 0x57, 0x51, 0x44, 
    0x44, 0x65
]

password = [byte ^ 0x65 for byte in reference_bytes]
password_str = ''.join(chr(b) for b in password)
print(password_str)