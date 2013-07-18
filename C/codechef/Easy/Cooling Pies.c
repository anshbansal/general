#include<stdio.h>
#include<stdlib.h>

int compare (const void * a, const void * b)
{//Produces descending order
  return ( *(int*)b - *(int*)a);
}


int main()
{
    int cases, nums, pies[100], weights[100], ans;
    register int i, j;

    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d", &nums);
        for(i = 0; i < nums; i++)
            scanf("%d", &pies[i]);
        for(i = 0; i < nums; i++)
            scanf("%d", &weights[i]);

        qsort(&pies, nums, sizeof(int), compare);
        qsort(&weights, nums, sizeof(int), compare);

        ans = 0;
        for(i = 0, j = 0; i < nums; i++)
        {
            if(weights[j] >= pies[i])
            {
                ans++;
                j++;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
