#include <stdio.h>
#include <stdlib.h>

void selection_sort(int arr[], int length)
{
    /*
    Sorts into increasing order
    For decreasing order change the comparison of elements of array
    */
    for (int j = 0; j < length - 1; j++) {
        int temp = j;
        for (int k = j + 1; k < length; k++){
            if (arr[k] < arr[temp]){
                temp = k;
            }
        }

        int temp2;
        temp2     = arr[j];
        arr[j]    = arr[temp];
        arr[temp] = temp2;
    }
}

int main()
{
    int length;
    for (;;) {
        printf("Enter a positive length: ");
        scanf("%d", &length);
        if (length > 1){
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

    selection_sort(arr, length);

    for (int i = 0; i < length; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
