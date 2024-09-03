#include <stdio.h>
#include <stdlib.h>

#define MAX 5  // Define the maximum size of the circular queue

int queue[MAX];
int front = -1, rear = -1;

// Function to insert an element into the circular queue
void insert() {
    int item;
    if ((front == 0 && rear == MAX - 1) || (rear == (front - 1) % (MAX - 1))) {
        printf("Queue is full! Insertion not possible.\n");
        return;
    }
    printf("Enter the element to insert: ");
    scanf("%d", &item);

    if (front == -1) {  // Insert the first element
        front = rear = 0;
    } else if (rear == MAX - 1 && front != 0) {
        rear = 0;  // Circularly wrap the rear
    } else {
        rear++;
    }
    queue[rear] = item;
    printf("%d inserted into the queue.\n", item);
}

// Function to delete an element from the circular queue
void delete() {
    if (front == -1) {
        printf("Queue is empty! Deletion not possible.\n");
        return;
    }

    printf("%d deleted from the queue.\n", queue[front]);
    if (front == rear) {  // Queue has only one element
        front = rear = -1;
    } else if (front == MAX - 1) {
        front = 0;  // Circularly wrap the front
    } else {
        front++;
    }
}

// Function to display the elements in the circular queue
void display() {
    if (front == -1) {
        printf("Queue is empty! Nothing to display.\n");
        return;
    }
    printf("Queue elements are:\n");
    if (rear >= front) {
        for (int i = front; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
    } else {
        for (int i = front; i < MAX; i++) {
            printf("%d ", queue[i]);
        }
        for (int i = 0; i <= rear; i++) {
            printf("%d ", queue[i]);
        }
    }
    printf("\n");
}

// Main function to drive the menu
int main() {
    int choice;
    while (1) {
        printf("\nCircular Queue Menu:\n");
        printf("1. Insert\n");
        printf("2. Delete\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                insert();
                break;
            case 2:
                delete();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);  // Exit the program
            default:
                printf("Invalid choice! Please enter a valid option.\n");
        }
    }
    return 0;
}
