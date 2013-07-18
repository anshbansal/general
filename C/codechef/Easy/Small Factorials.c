#include<stdio.h>

#define LIMIT 1000000
#define ANS_SIZE 26

//The second define is ceil(156/(no. of zeros)) in the first define
//In the second last printf the %04d needs to be changed to no. of zeros in 1st define
int main()
{
    int tests, num, ans[ANS_SIZE];
    register short int i, j, k, m;
    long temp;

    scanf("%d", &tests);
    for(k = 1; k <= tests; k++)
    {
        scanf("%d", &num);
        ans[0] = 1;
        for(i = 1; i < ANS_SIZE; i++)
            ans[i] = 0;

        for(i = 2; i <= num; i++)
        {
            ans[ANS_SIZE - 1] *= i;
            for(j = ANS_SIZE - 2 ; j >= 0 ; j--)
            {
                temp = ans[j] * i;
                ans[j] = temp % LIMIT;
                ans[j + 1] += temp/LIMIT;

                for(m = j + 1; m < ANS_SIZE - 1; m++)
                {//This checks whether increment to next array index takes it above the LIMIT
                    if(ans[m] >= LIMIT)
                    {
                        temp = ans[m];
                        ans[m] = temp % LIMIT;
                        ans[m + 1] += temp/LIMIT;
                    }
                    else
                        break;
                }
            }
        }

        for(i = (ANS_SIZE - 1); i >= 0; i--)
            if(ans[i])
                break;

        printf("%d", ans[i]);
        i--;
        for(; i >= 0; i--)        
            printf("%06d", ans[i]);

        printf("\n");
    }
    return 0;
}