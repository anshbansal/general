#include<stdio.h>

int main()
{
    short t, temp;
    int num, menus;
    scanf("%hd", &t);
    while(t--)
    {
        scanf("%d", &num);
        temp = 2048;
        menus = 0;

        while(num > 0)
        {
            while (num >= temp)
            {
                num-=temp;
                menus++;
            }
            temp /= 2;
            if(temp == 0)
                temp = 1;
        }
        printf("%d\n", menus);
    }
    return 0;
}
