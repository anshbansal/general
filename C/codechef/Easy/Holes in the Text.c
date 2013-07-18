#include<stdio.h>

int main()
{
    int cases, char_count;
    register int i;
    char text[100], *c;

    scanf("%d", &cases);
    for(i = 0; i < cases; i++)
    {
        scanf("%s", &text);
        c = &text[0];
        char_count = 0;
        while(*c != '\0')
        {
            if(*c == 'A' || *c == 'D' || *c == 'O' || *c == 'P' || *c == 'Q' || *c == 'R')
                char_count++;
            else if(*c == 'B')
                char_count += 2;
            c++;
        }
        printf("%d\n", char_count);
    }
    return 0;
}

