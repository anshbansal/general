#include<stdio.h>

#define CUR row[factor]
#define PRE row[factor2]

int main()
{
    int cases, rows, factor, factor2;
    int row[2][100];
    register int i, j, k;

    scanf("%d", &cases);
    for(i = 0; i < cases; i++)
    {
        scanf("%d", &rows);
        //Initializing both rows to 0
        for(j = 0; j < 100; j++)
            row[0][j] = row[1][j] = 0;

        for(j = 0; j < rows; j++)
        {
            factor = j % 2;
            factor2 = (j + 1) % 2;
            for(k = 0; k <= j; k++)
            {
                scanf("%d", &CUR[k]);
                if(k == 0 )
                    CUR[k] += PRE[k];
                else if(k == j)
                    CUR[k] += PRE[k - 1];
                else
                    CUR[k] += (PRE[k] > PRE[k - 1]) ? PRE[k] : PRE[k - 1];
            }
        }
        //factor is already set at the end of last loop
        factor2  = -1;
        for(k = 0; k < rows; k++)
            if(CUR[k] > factor2)
                factor2 = CUR[k];

        printf("%d\n", factor2);
    }
    return 0;
}
