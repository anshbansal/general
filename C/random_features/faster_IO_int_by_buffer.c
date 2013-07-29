/*
Faster IO for integers using buffers.

Here sorting is secondary and may not be most efficient
*/
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<time.h>

#define SORTING_ALGO_CALL merge_sort

char buffer[4096];
int bufcount;
int bufpos;

int get_next_char()
{
    if (!bufcount)
    {
        bufcount = fread(buffer, 1, 4096, stdin);
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
    int ans[length];
    int i, j, k;
    int temp = length/2;
    //This while and next if-else puts the merged array into temporary array ans
    for (j = temp, i = k = 0; (i < temp && j < length); k++){
        ans[k] = (arr[i] < arr[j]) ? arr[i++] : arr[j++];
    }

    if(i >= temp){
        while(j < length){
            ans[k++] = arr[j++];
        }
    }
    else{
        while(i < temp){
            ans[k++] = arr[i++];
        }
    }

    //This while loops puts array ans into original array arr
    for(i = 0; i < length; i++){
        arr[i] = ans[i];
    }
}

void merge_sort(int arr[], int length)
{
    if(length > 1)
    {
        merge_sort(&arr[0], (length/2));
        merge_sort(&arr[length/2], (length - length/2));
        merge_parts(arr, length);
    }
}

int main()
{
    clock_t time1, time2;
    double time_taken;

//FIRST READ
    time1 = clock();

    int length = readnum();
    while (length < 1)
    {
        printf("\nYou entered length = %d\n", length);
        printf("\nEnter a positive length: ");
        length = readnum();
    }

//SECOND READ, PRINT
    time2 = clock();
    time_taken = (double)(time2 - time1) / CLOCKS_PER_SEC;
    printf("\nReading length = %f\n", time_taken);

    int *arr;
    if ((arr = malloc(sizeof(int) * length)) == NULL)
    {
        perror("The following error occurred");
        exit(-1);
    }

//FIRST READ
    time1 = clock();

    for (int i = 0; i < length; i++){
        arr[i] = readnum();
    }

//SECOND READ, PRINT AND NEXT FIRST READ
    time2 = clock();
    time_taken = (double)(time2 - time1) / CLOCKS_PER_SEC;
    printf("\nReading array = %f\n", time_taken);
    time1 = clock();

    SORTING_ALGO_CALL(arr, length);

//SECOND READ, PRINT
    time2 = clock();
    time_taken = (double)(time2 - time1) / CLOCKS_PER_SEC;
    printf("\nSorting array = %f\n", time_taken);

/*
    for (int i = 0; i < length; i++){
        printf("%d ", arr[i]);
    }
*/
    free(arr);
    return 0;
}
