#include <stdio.h>
#include <stdlib.h>

static int compare (const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

static int bin_proc(const int arr[], int min, int max, int element)
{
    if (min >= max){
        return arr[max] == element ? max : -1;
    }

    //Don't change this assignment of mid. It avoids overflow
    int mid = min + (max - min)/2;

    if (arr[mid] < element) {
        return bin_proc(arr, mid + 1, max, element);
    }
    else {
        return bin_proc(arr, min, mid, element);
    }
}

int bin_search(const int arr[], int length, int element)
{
    /*
    Searches for an element in the array arr
    If present returns index else returns -1
    */
    if (length < 1){
        return -1;
    }
    return bin_proc(arr, 0, length - 1, element);
}

int main()
{
    int length;
    for (;;)
    {
        printf("Enter a positive length: ");
        scanf("%d", &length);
        if (length > 0){
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

    int element;
    printf("\nEnter the element to be searched: ");
    scanf("%d", &element);

    qsort(arr, length, sizeof(int), compare);
    int index = bin_search(arr, length, element);

    if (index == -1){
        printf("\nElement not in the array");
    }
    else{
        printf("\nIndex of element is %d\n", index);
    }

    free(arr);
    return 0;
}
