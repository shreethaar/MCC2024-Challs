#include <stdint.h>
#include <stdio.h>

uint32_t rotate_right(uint32_t value, int shift) {
    return (value >> shift) | (value << (32 - shift));
}

uint32_t rotate_left(uint32_t value, int shift) {
    return (value << shift) | (value >> (32 - shift));
}

int main() {
    uint32_t target = 0xF298DC9E;
    uint32_t eax, ecx;

    // Reverse the final steps to find the original value
    eax = target;
    
    // Undo ROR 7 and SHR 1
    eax <<= 1;
    eax = rotate_right(eax, -7);  // ROR with negative is equivalent to ROL
    
    // Undo ADD and XOR
    ecx = eax;
    eax += 0xFFA3887A;
    ecx ^= 0xCB89034;
    eax -= ecx;
    
    // Undo SHR 9
    eax >>= 9;
    
    // Undo LEA and XOR operations
    ecx = eax - 0xD1507BA;
    eax = 0x0B20083FF ^ ecx;

    printf("Final EAX value: 0x%08X\n", eax);
    return 0;
}
