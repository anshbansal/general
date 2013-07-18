#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

#define SORTING_ALGO_CALL merge_sort

#define BUFFER_SIZE 32768
char buffer[BUFFER_SIZE];
int bufcount;
int bufpos;

int get_next_char()
{
    if (!bufcount)
    {
        bufcount = fread(buffer, 1, BUFFER_SIZE, stdin);
        bufpos = 0;
        if (!bufcount){
            return EOF;
        }
    }
    bufcount--;
    return buffer[bufpos++];
}

int readnum()
{
    int res = 0;
    char ch;
    do
    {
        ch = get_next_char();
    } while (!isdigit(ch) && ch != EOF);

    if (ch == EOF){
            return 0xbaadbeef;    // Don't expect this to happen.
    }

    do
    {
        res = (res * 10) + ch - '0';
        ch = get_next_char();
    } while(isdigit(ch));
    return res;
}

void merge_parts(int arr[], int length)
{
    /*
    Sorts into increasing order
    For decreasing order change the comparison in for-loop
    */
    int ans[length];
    //This while and next if-else puts the merged array into temporary array ans
	//in a sorted manner
	int mid = length/2;
    int i = 0, k = 0, j = mid;
    while (i < mid && j < length){
        ans[k++] = (arr[i] < arr[j]) ? arr[i++] : arr[j++];
    }

    while(i < mid){
        ans[k++] = arr[i++];
    }

    //This for-loop puts array ans into original array arr
    for(i = 0; i < j; i++){
        arr[i] = ans[i];
    }
}

void merge_sort(int arr[], int length)
{
    if(length > 1)
    {
        int mid = length/2;
        merge_sort(arr,         mid);
        merge_sort(arr + mid,   length - mid);
        merge_parts(arr, length);
    }
}

int main()
{
    int length = readnum();
    int *arr;
    arr = malloc(sizeof(int) * length);

    for (int i = 0; i < length; i++){
        arr[i] = readnum();
    }

    SORTING_ALGO_CALL(arr, length);

    for (int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }

    free(arr);
    return 0;
}
