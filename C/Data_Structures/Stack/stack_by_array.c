#include<assert.h>
#include<stdio.h>
#include<stdlib.h>

static const int MAX_SIZE = 100;
enum action {PUSH = 1, POP, TOP, QUIT};

void clear_screen(void)
{
    system("cls");
}

static enum action get_user_action(void)
{
    int choice = PUSH - 1;
    do
    {
        clear_screen();
        printf("%d Push data\n"
               "%d Pop Data\n"
               "%d See the top of the stack\n"
               "%d Exit\n\n"
               "Enter your choice -> ", PUSH, POP, TOP, QUIT);
        scanf("%d", &choice);
    } while (choice != PUSH && choice != POP && choice != TOP && choice != QUIT);
    return (enum action) choice;
}

void push(int *arr, int *length, int *status, int data)
{
    *status = PUSH - 1;
    if (*length == MAX_SIZE){
        *status = PUSH;
        return;
    }
    arr[(*length)++] = data;
}

int pop(int *arr, int *length, int *status)
{
    *status = PUSH - 1;
    if (*length == 0){
        *status = POP;
        return -1;
    }
    return arr[--(*length)];
}

int see_top(int *arr, int *length, int *status)
{
    *status = PUSH - 1;
    if (*length == 0){
        *status = POP;
        return -1;
    }
    return arr[*length - 1];
}

int main(void)
{
    int arr[MAX_SIZE];
    int length = 0;

    enum action choice;
    while ((choice = get_user_action()) != QUIT)
    {
        clear_screen();
        int status;
        int data;
        switch (choice)
        {
        case PUSH:
            printf("Enter data to be pushed -> ");
            scanf("%d", &data);
            push(arr, &length, &status, data);
            if (status == PUSH){
                printf("Stack overflow\n");
            }
            else{
                printf("%d pushed onto the stack\n", data);
            }
            break;
        case POP:
            data = pop(arr, &length, &status);
            if (status == POP){
                printf("Stack underflow\n");
            }
            else{
                printf("The data is %d\n", data);
            }
            break;
        case TOP:
            data = see_top(arr, &length, &status);
            switch (status)
            {
            case POP:
                printf("Nothing in the stack\n");
                break;
            default:
                printf("The data at top is %d\n", data);
            }
            break;
        default:
            assert(!"You should not have reached this.");
        }
        printf("Length is %d\n", length);
        getchar();
        getchar();
    }
}
