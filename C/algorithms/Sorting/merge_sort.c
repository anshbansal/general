#include<stdio.h>
#include<stdlib.h>

static void merge_parts(int arr[], int length)
{
    /*
    Sorts into increasing order
    For decreasing order change the comparison of elements of array
    */
    /*
    Till one of the sub-array is placed into the temporary array in a sorted manner we need
    to keep checking whether array has been sorted. After that only the 1st part of the
    array needs to be checked because 2nd part is already sorted in the original array.
    */
    int ans[length];
	int mid = length/2;
    int i = 0, k = 0, j = mid;
    while (i < mid && j < length){
        ans[k++] = (arr[i] < arr[j]) ? arr[i++] : arr[j++];
    }

    while (i < mid){
        ans[k++] = arr[i++];
    }

    for (i = 0; i < j; i++){
        arr[i] = ans[i];
    }
}

void merge_sort(int arr[], int length)
{
    if (length > 1)
    {
        int mid = length/2;
        merge_sort(arr,         mid);
        merge_sort(arr + mid,   length - mid);
        merge_parts(arr, length);
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

    merge_sort(arr, length);

    for (int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
