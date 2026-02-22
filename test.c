#include <stdio.h>

int main() {
    int input[20], output[30];
    int n, i, j = 0, count = 0;

    // Get the number of bits
    printf("Enter number of bits: ");
    scanf("%d", &n);

    // Get the bits
    printf("Enter the bits (only 0 and 1): ");
    for (i = 0; i < n; i++) {
        scanf("%d", &input[i]);
    }

    // Bit stuffing process
    for (i = 0; i < n; i++) {
        output[j] = input[i];
        j++;

        if (input[i] == 1) {
            count++;
            if (count == 5) {
                output[j] = 0; // Stuff a 0 after five 1s
                j++;
                count = 0;     // Reset the counter
            }
        } else {
            count = 0; // Reset counter if a 0 is found
        }
    }

    // Print the stuffed frame
    printf("Stuffed bits: ");
    for (i = 0; i < j; i++) {
        printf("%d", output[i]);
    }
    printf("\n");

    return 0;
}
