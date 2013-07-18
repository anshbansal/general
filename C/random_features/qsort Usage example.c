/*
Shows the use of qsort function. It needs a function that returns
    +ve value if a should be after  b
    -ve value if a should be before b
    0 if a and b are equivalent
*/
#include<stdio.h>
#include<stdlib.h>

int compare (const void * a, const void * b)
{
    /*
    To get array sorted into increasing order we return
    +ve value when a > b i.e. a is after b
    -ve value when a < b i.e. a is before b
    0 value when a == b  i.e. both are equivalent
    */
    return (*(int*)a - *(int*)b);
}

int main()
{
    int values[6] = { 40, 10, 100, 90, 20, 25};
    qsort(values, 6, sizeof(*values), compare);
    for(int i = 0; i < 6; i++)
        printf("%d ",values[i]);
}
