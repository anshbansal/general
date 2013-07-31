#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

enum action {START, PUSH, POP, TOP, QUIT, END};
enum status {SUCCESS, FAILURE};

typedef struct node {
    int data;
    struct node *lower;

} stack_node;

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

enum status push(stack_node **top_stack, int data)
{
    stack_node *node = malloc(sizeof(node));
    if (node == NULL) {
        return FAILURE;
    }

    node -> data = data;
    if (*top_stack == NULL) {
        node -> lower = NULL;
    } else {
        node -> lower = *top_stack;
    }
    *top_stack = node;
    return SUCCESS;
}

enum status pop(stack_node **top_stack, int *data)
{
    if (*top_stack == NULL) {
        return FAILURE;
    }
    stack_node *node = *top_stack;
    *data = node -> data;
    *top_stack = node -> lower;
    free(node);

    return SUCCESS;
}

enum status peek(stack_node **top_stack, int *data)
{
    if (*top_stack == NULL) {
        return FAILURE;
    }
    *data = (*top_stack) -> data;
    return SUCCESS;
}

int main(void)
{
    enum action choice;
    int status;
    stack_node *top = NULL;

    while ((choice = get_user_action()) != QUIT) {
        clear_screen();
        int data;
        switch (choice) {

            case PUSH:
                printf("Enter data to be pushed -> ");
                scanf("%d", &data);
                if (push(&top, data) == SUCCESS){
                    printf("%d pushed onto the stack", data);
                } else {
                    printf("Not enough memory\n");
                }
                break;

            case POP:
                if (pop(&top, &data) == SUCCESS){
                    printf("The data is %d\n", data);
                } else {
                    printf("Stack underflow\n");
                }
                break;

            case TOP:
                if (peek(&top, &data) == SUCCESS){
                    printf("The data at top is %d\n", data);
                } else {
                    printf("Nothing in the stack\n");
                }
                break;

            default:
                assert(!"You should not have reached this.");

        }
        getchar();
        getchar();
    }
}
