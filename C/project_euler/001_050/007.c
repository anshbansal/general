/**
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
*/
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int primes = 1;
    long long int i, number = 1;

    while (primes < 10001)
    {
        number += 2;
        for (i = 3; i < number; i += 2)
        {
            if(number % i == 0)
                break;
        }

        if(i == number)
            primes++;
    }

    printf("%lld",number);
    return 0;
}
