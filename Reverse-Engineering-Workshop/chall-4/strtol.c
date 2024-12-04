#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *hexString = "0x1A3F";  // Hexadecimal input
    const char *decString = "12345";   // Decimal input
    const char *octString = "0750";    // Octal input

    char *endptr;
    
    // Hexadecimal conversion
    long hexValue = strtol(hexString, &endptr, 0);  // Base 0 for automatic detection
    if (*endptr == '\0') {
        printf("Hexadecimal value: %ld\n", hexValue);  // Output: 6719 (0x1A3F in decimal)
    } else {
        printf("Invalid hexadecimal string\n");
    }

    // Decimal conversion
    long decValue = strtol(decString, &endptr, 10);  // Base 10 for decimal
    if (*endptr == '\0') {
        printf("Decimal value: %ld\n", decValue);  // Output: 12345
    } else {
        printf("Invalid decimal string\n");
    }

    // Octal conversion
    long octValue = strtol(octString, &endptr, 0);  // Base 0 for automatic detection
    if (*endptr == '\0') {
        printf("Octal value: %ld\n", octValue);  // Output: 492 (0750 in octal)
    } else {
        printf("Invalid octal string\n");
    }

    return 0;
}
