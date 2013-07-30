#include<assert.h>
#include<errno.h>
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
    int choice = 0;
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

void push(int *arr, int *length, int data)
{
    if (*length == MAX_SIZE){
        errno = PUSH;
        return;
    }
    arr[(*length)++] = data;
}

int pop(int *arr, int *length)
{
    if (*length == 0){
        errno = POP;
        return -1;
    }
    return arr[--(*length)];
}

int top(int *arr, int *length)
{
    if (*length == 0){
        errno = POP;
        return -1;
    }
    else if (*length == MAX_SIZE){
        errno = PUSH;
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
        int data;
        errno = 0;

        switch (choice)
        {
        case PUSH:
            printf("Enter data to be pushed -> ");
            scanf("%d", &data);
            push(arr, &length, data);
            if (errno == PUSH){
                printf("Stack overflow\n");
            }
            break;
        case POP:
            data = pop(arr, &length);
            if (errno == POP){
                printf("Stack underflow\n");
            }
            else{
                printf("The data is %d\n", data);
            }
            break;
        case TOP:
            data = top(arr, &length);
            switch (errno)
            {
            case PUSH:
                printf("Stack overflow\n");
                break;
            case POP:
                printf("Stack underflow\n");
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
