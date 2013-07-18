#include<stdio.h>

#define ARR_SIZE 10000

int main()
{
    int tests, nums;
    register int i, j;
    int num[ARR_SIZE], temp;

    scanf("%d", &tests);
    for(i = 0; i < tests; i++)
    {
        scanf("%d", &nums);
        for(j = 0; j < ARR_SIZE; j++)
            num[j] = 0;

        for(j = 0; j < nums; j++)
        {
            scanf("%d", &temp);
            num[temp - 1]++;
        }

        temp = 0;
        for(j = 1; j < ARR_SIZE; j++)
            if(num[j] > num[temp])
                temp = j;
        printf("%d %d\n", temp + 1, num[temp]);

    }
    return 0;
}
