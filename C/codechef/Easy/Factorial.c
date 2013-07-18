#include<stdio.h>

int main()
{
    register int i, fives;
    int times, num;
    scanf("%d", &times);

    for(i = 0; i < times; i++)
    {
		scanf("%d", &num);
		if(num < 0)
            printf("0\n");
        else
        {
            fives = 0;
            while(num)
            {
                num /= 5;
                fives += num;
            }
            printf("%d\n", fives);
        }
    }
    return 0;
}
