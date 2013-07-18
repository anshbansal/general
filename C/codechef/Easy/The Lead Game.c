#include<stdio.h>

int main()
{
    int cases, round_score[2], score[2] ={0 , 0}, largest[2] = {0, 0};

    scanf("%d", &cases);
    while(cases--)
    {
        scanf("%d %d", &round_score[0], &round_score[1]);

        score[0] += round_score[0];
        score[1] += round_score[1];

        if(score[0] > score[1])
        {
            if (score[0] - score[1] > largest[0])
                largest[0] = score[0] - score[1];
        }
        else
        {
            if (score[1] - score[0] > largest[1])
                largest[1] = score[1] - score[0];
        }
    }

    if(largest[0] > largest[1])
        printf("1 %d", largest[0]);
    else
        printf("2 %d", largest[1]);

    return 0;
}
