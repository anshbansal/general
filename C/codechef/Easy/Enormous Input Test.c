#include<stdio.h>

int main()
{
    int n, k, t;
    register int i, total = 0;

    scanf("%d %d", &n, &k);
    for(i = 0; i < n; i++)
    {
        scanf("%d", &t);
        if(t % k == 0)
            total++;
    }
    printf("%d", total);
    return 0;
}
