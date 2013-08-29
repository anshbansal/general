#include<stdio.h>

int max_subarray(int array[], int *low, int *high);

static void initialize(int *sum, int *low, int *high);
static void update_var(int increase, int *sum, int *low, int *high, int i);

int main()
{
    //The maximum subarray-sum is 43 for the following
    int array[16] = {13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7};
    int low = 0;
    int high = 15;

    printf("%d", max_subarray(array, &low, &high));
    printf("\n%d %d", low, high);

    return 0;
}

int max_subarray(int array[], int *low, int *high)
{
    int max_sum, max_low, max_high;
    int bet_sum, bet_low, bet_high;
    int inc_sum, inc_low, inc_high;

    initialize(&max_sum, &max_low, &max_high);
    initialize(&bet_sum, &bet_low, &bet_high);
    initialize(&inc_sum, &inc_low, &inc_high);

    for (int i = *low; i <= *high; i++)
    {
        if (max_sum + bet_sum + array[i] > max_sum) {
            update_var(bet_sum + array[i], &max_sum, &max_low, &max_high, i);
            initialize(&bet_sum, &bet_low, &bet_high);
            initialize(&inc_sum, &inc_low, &inc_high);

        } else {
            update_var(array[i], &bet_sum, &bet_low, &bet_high, i);
            if (inc_sum + array[i] > inc_sum) {
                update_var(array[i], &inc_sum, &inc_low, &inc_high, i);
                if (inc_sum > max_sum) {
                    max_sum = inc_sum;
                    max_low = inc_low;
                    max_high = inc_high;
                    initialize(&bet_sum, &bet_low, &bet_high);
                    initialize(&inc_sum, &inc_low, &inc_high);
                }
            }
        }
    }
    *low = max_low;
    *high = max_high;
    return max_sum;
}

static void update_var(int increase, int *sum, int *low, int *high, int i)
{
    *sum += increase;
    *high = i;
    if (*low == -1) {
        *low = i;
    }
}

static void initialize(int *sum, int *low, int *high)
{
    *sum = 0;
    *low = -1;
    *high = -1;
}
