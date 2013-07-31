#include <stdio.h>
#include <stdlib.h>

void bubble_sort(int arr[], int length)
{
    /*
    Sorts into increasing order
    For decreasing order change the comparison of elements of array
    */
    for (int j = 1; j < length; j++) {
        int flag = 0;
        for (int k = 1; k <= length; k++) {
            if (arr[k] < arr[k - 1]) {
                int temp;
                temp = arr[k];
                arr[k] = arr[k - 1];
                arr[k - 1] = temp;
                flag = 1;
            }
        }
        if (flag == 0) {
            return;
        }
    }
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

    bubble_sort(arr, length);

    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
