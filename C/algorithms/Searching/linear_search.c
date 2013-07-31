#include <stdio.h>
#include <stdlib.h>

int linear_search(const int arr[], int length, int element)
{
    /*
    Searches for an element in the array arr
    If present returns first index else returns -1
    */
    for (int i = 0; i < length; i++) {
        if (arr[i] == element) {
            return i;
        }
    }
    return -1;
}

int main()
{
    int length;
    for (;;) {
        printf("Enter a positive length: ");
        scanf("%d", &length);

        if (length > 1) {
            break;
        } else {
            printf("You entered length = %d\n\n", length);
        }
    }

    int *arr = malloc(sizeof(int) * length);
    if (arr == NULL) {
        perror("The following error occurred");
        exit(-1);
    }

    for (int i = 0; i < length; i++) {
        scanf("%d", &arr[i]);
    }

    int element;
    printf("\nEnter the element to be searched: ");
    scanf("%d", &element);

    int index = linear_search(arr, length, element);

    if (index == -1) {
        printf("\nElement not in the array");
    } else {
        printf("\nIndex of element is %d", index);
    }

    free(arr);
    return 0;
}
