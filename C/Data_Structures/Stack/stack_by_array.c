#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

static const int MAX_SIZE = 100;
enum action {START, PUSH, POP, TOP, QUIT, END};
enum status {SUCCESS, FAILURE};

void clear_screen(void)
{
    system("cls");
}

static enum action get_user_action(void)
{
    int choice = START;
    do {
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

enum status push(int *arr, int *length, int data)
{
    if (*length == MAX_SIZE) {
        return FAILURE;
    }
    arr[(*length)++] = data;
    return SUCCESS;
}

enum status pop(int *arr, int *length, int *data)
{
    if (*length == 0) {
        return FAILURE;
    }
    *data = arr[--(*length)];
    return SUCCESS;
}

enum status peek(int *arr, int *length, int *data)
{
    if (*length == 0) {
        return FAILURE;
    }
    *data = arr[*length - 1];
    return SUCCESS;
}

int main(void)
{
    int arr[MAX_SIZE];
    int length = 0;

    enum action choice;
    while ((choice = get_user_action()) != QUIT) {
        clear_screen();
        int data;
        switch (choice) {

            case PUSH:
                printf("Enter data to be pushed -> ");
                scanf("%d", &data);
                if (push(arr, &length, data) == SUCCESS) {
                    printf("%d pushed onto the stack\n", data);
                } else {
                    printf("Stack overflow\n");
                }
                break;

            case POP:
                if (pop(arr, &length, &data) == SUCCESS) {
                    printf("The data is %d\n", data);
                } else {
                    printf("Stack underflow\n");
                }
                break;

            case TOP:
                if (peek(arr, &length, &data) == SUCCESS) {
                    printf("The data at top is %d\n", data);
                } else {
                    printf("Nothing in the stack\n");
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
