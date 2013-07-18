/**
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/
#include<stdio.h>
#include<stdlib.h>

int rev(int product);

int main()
{
    int product = 0, palin = 0;

    for (int i = 999; i > 99; i--)
    {
        for (int j = i; j > 99; j--)
        {
            product = i * j;

            //if palindrome and bigger then currently biggest palindrome
            if ( (product == rev(product)) && (product > palin) )
                palin = product;
        }
    }
    printf("%d", palin);
    return 0;
}

int rev(int product)
{
    int rev_pro = 0;
    while (product > 0)
    {
        rev_pro *= 10;
        rev_pro += (product % 10);
        product = product /10;
    }
    return rev_pro;
}
