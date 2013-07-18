/**
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    long long int NUM = 600851475143;
    int prime = 3;

    for (long long int i = prime; i <= NUM; i += 2)
    {
        while (NUM % i == 0)
        {
            prime = i;
            NUM = NUM / i;
        }
    }
    printf("%d", prime);

    return 0;
}
