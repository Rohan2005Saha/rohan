#include <stdio.h>

// Function to perform the Tower of Hanoi move
void towerOfHanoi(int n, char from_rod, char to_rod, char aux_rod) {
    // Base case: If there's only one disk, move it from the source to the destination rod
    if (n == 1) {
        printf("Move disk 1 from rod %c to rod %c\n", from_rod, to_rod);
        return;
    }

    // Move the top n-1 disks from the source rod to the auxiliary rod
    towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);

    // Move the nth disk from the source rod to the destination rod
    printf("Move disk %d from rod %c to rod %c\n", n, from_rod, to_rod);

    // Move the n-1 disks from the auxiliary rod to the destination rod
    towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
}

int main() {
    int n;  // Number of disks

    // Get the number of disks from the user
    printf("Enter the number of disks: ");
    scanf("%d", &n);

    // Call the function to solve the Tower of Hanoi problem
    towerOfHanoi(n, 'A', 'C', 'B');  // A, B, and C are names of the rods

    return 0;
}
