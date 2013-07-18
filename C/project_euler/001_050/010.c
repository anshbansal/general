/**
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/
#include<stdio.h>
#include<stdlib.h>

#define NUMBERS 2000000
int main()
{
    char flag[NUMBERS];

    register int i;
    long long int sum = 0;

    for (i = 0; i < NUMBERS; i++)
        flag[i] =  'a'; //unchecked or prime

    for (i = 2; i < NUMBERS; i++)
    {
        if (flag[i] == 'a')
        {
            sum += i;

            int mul_factor = 2;
            while ( (i * mul_factor) < NUMBERS )
            {
                flag[i * mul_factor] = 'b';
                mul_factor++;
            }
        }
    }
    printf("%lld", sum);
    return 0;
}
