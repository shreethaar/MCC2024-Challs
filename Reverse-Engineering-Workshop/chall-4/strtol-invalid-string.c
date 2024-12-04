
#include <stdio.h>
#include <stdlib.h>

int main() {
    const char *invalidString = "abc123";  // Non-numeric string
    
    char *endptr;
    
    // Attempt to convert the invalid string
    long value = strtol(invalidString, &endptr, 10);  // Base 10 for decimal

    // Check if the conversion was successful
    if (*endptr == '\0') {
        printf("Converted value: %ld\n", value);
    } else {
        printf("Conversion failed. First unconverted character: '%c'\n", *endptr);
    }

    return 0;
}
