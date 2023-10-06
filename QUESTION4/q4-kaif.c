#include <stdio.h>
#include <math.h>

int countBitsRequired(int decimalNumber) {
    if (decimalNumber == 0) {
        return 1; // Special case: 0 can be represented in 1 bit
    }

    // Calculate the number of bits required using the log2 function
    int bitsRequired = (int)log2(fabs(decimalNumber)) + 1;

    return bitsRequired;
}

int main() {
    int decimalNumber;
    printf("Enter a decimal number: ");
    scanf("%d", &decimalNumber);

    if (decimalNumber < 0) {
        printf("Negative numbers are not supported.\n");
        return 1; // Exit with an error code
    }

    int bitsRequired = countBitsRequired(decimalNumber);
    printf("Number of bits required to store %d in binary: %d\n", decimalNumber, bitsRequired);

    return 0;
}
