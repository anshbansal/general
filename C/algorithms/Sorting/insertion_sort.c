#include<stdio.h>
#include<stdlib.h>

void insertion_sort(int arr[], int length)
{
    /*
    Sorts into increasing order
    For decreasing order change the comparison of elements of array
    */
    for (int j = 1; j < length; j++)
    {
        int temp = arr[j];
        int k;
        for (k = j - 1; k >= 0 && arr[k] > temp; k--){
            arr[k + 1] = arr[k];
        }
        arr[k + 1] = temp;
    }
}

int main()
{
    int length;
    while (1)
    {
        printf("Enter a positive length: ");
        scanf("%d", &length);
        if (length > 1){
            break;
        }
        else{
            printf("You entered length = %d\n\n", length);
        }
    }

    int *arr = malloc(sizeof(int) * length);
    if (arr == NULL)
    {
        perror("The following error occurred");
        exit(-1);
    }

    for (int i = 0; i < length; i++){
        scanf("%d", &arr[i]);
    }

    insertion_sort(arr, length);

    for (int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
