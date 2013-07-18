#include<stdio.h>

int main()
{
    int draw;
    float balance;

    scanf("%d %f", &draw, &balance);

    if(draw % 5 == 0 && balance >= draw + 0.5)
        balance -= draw + 0.5;

    printf("%.2f", balance);

    return 0;
}
