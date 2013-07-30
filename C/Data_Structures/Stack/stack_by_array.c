#include<stdio.h>
#include<stdlib.h>
#include<errno.h>

static const int MAX_SIZE = 100;
static const int MIN = 1;
static const int MAX = 4;

void intro();

void push(int *, int *, int);
int pop(int *, int *);
int top(int *, int *);

int main()
{
    int arr[MAX_SIZE];
    int length = 0;

    for (;;)
    {
        int choice = MAX + 1;
        while (MAX < choice || choice < MIN)
        {
            system("cls");
            intro();
            printf("Enter your choice -> ");
            scanf("%d", &choice);
        }

        system("cls");
        int data;
        errno = 0;
        switch (choice)
        {
        case 1:
            printf("\nEnter data to be pushed -> ");
            scanf("%d", &data);
            push(arr, &length, data);
            if (errno == 1){
                printf("\nStack overflow");
            }
            break;
        case 2:
            data = pop(arr, &length);
            if (errno == 2){
                printf("\nStack underflow");
            }
            else{
                printf("\nThe data is %d", data);
            }
            break;
        case 3:
            data = top(arr, &length);
            if (errno == 1){
                printf("\nStack overflow");
            }
            else if (errno == 2){
                printf("\nStack underflow");
            }
            else{
                printf("\nThe data at top is %d", data);
            }
            break;
        case 4:
            return 0;
        }
        printf("\nLength is %d", length);
        getchar();
        getchar();
    }
}

void intro()
{
    printf("1 Push data\n");
    printf("2 Pop Data\n");
    printf("3 See the top of the stack\n");
    printf("4 Exit this program\n\n");
}

void push(int *arr, int *length, int data)
{
    if (*length == MAX_SIZE){
        errno = 1;
        return;
    }
    arr[(*length)++] = data;
}

int pop(int *arr, int *length)
{
    if (*length == 0){
        errno = 2;
        return -1;
    }
    return arr[--(*length)];
}

int top(int *arr, int *length)
{
    if (*length == 0){
        errno = 2;
        return -1;
    }
    else if (*length == MAX_SIZE){
        errno = 1;
        return -1;
    }
    return arr[*length - 1];
}
