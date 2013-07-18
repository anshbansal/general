/**
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/
#include<stdio.h>
#include<stdlib.h>

long long int answer = 1;
int numbers[20];

void update(int index, int num)
{
    /*
    This is used to update the array of numbers

    In sequence all the numbers from 1 to 20 are checked for divison with primes.
    If it is divisible then the array is divided.
    */
    while (numbers[index] % num == 0)
    {
        answer *= num;
        for (int j = index; j < 20; j++)
        {
            if (numbers[j] % num == 0)
                numbers[j] /= num;
        }
    }
}

int main()
{
    int primes[] = {2,3,5,7,11,13,17,19};
    int number_of_primes = sizeof(primes) / sizeof(int);

    for (int i = 1; i <= 20; i++)
        numbers[i-1] = i;

    for (int i = 1; i < 20; i++)
        for (int j = 0; j < number_of_primes; j++)
        update(i, primes[j]);

    printf("%lld", answer);

    return 0;
}
