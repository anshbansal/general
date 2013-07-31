#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

static const int MAX_SIZE = 100;
enum action {START, PUSH, POP, TOP, QUIT, END};

void clear_screen(void)
{
    system("cls");
}

static enum action get_user_action(void)
{
    int choice = START;
    do
    {
        clear_screen();
        printf("%d Push data\n"
               "%d Pop Data\n"
               "%d See the top of the stack\n"
               "%d Exit\n\n"
               "Enter your choice -> ", PUSH, POP, TOP, QUIT);
        scanf("%d", &choice);
    } while (!(START < choice && choice < END));
    return (enum action) choice;
}

void push(int *arr, int *length, int *status, int data)
{
    *status = START;
    if (*length == MAX_SIZE){
        *status = PUSH;
        return;
    }
    arr[(*length)++] = data;
}

int pop(int *arr, int *length, int *status)
{
    *status = START;
    if (*length == 0){
        *status = POP;
        return -1;
    }
    return arr[--(*length)];
}

int peek(int *arr, int *length, int *status)
{
    *status = START;
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
            data = peek(arr, &length, &status);
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
