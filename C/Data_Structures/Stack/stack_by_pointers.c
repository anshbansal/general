#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum action {START, PUSH, POP, TOP, LENGTH, QUIT, END};
enum status {SUCCESS, FAILURE};

typedef struct node {
    void *data;
    struct node *lower;
} stack_node;

typedef struct stack {
    size_t elem_size;
    size_t stack_size;
    stack_node *top;
} stack_struct;

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
               "%d See the length of the stack\n"
               "%d Exit\n\n"
               "Enter your choice -> ", PUSH, POP, TOP, LENGTH, QUIT);
        scanf("%d", &choice);
    } while (!(START < choice && choice < END));
    return (enum action) choice;
}

enum status stack_create(stack_struct **stack, size_t elem_size)
{
    (**stack).elem_size = elem_size;
    (**stack).stack_size = 0;
    (**stack).top = NULL;
    return SUCCESS;
}

enum status push(stack_struct **stack, void *data)
{
    stack_node *node = malloc(sizeof(node));
    if (node == NULL) {
        return FAILURE;
    }

    node->data = malloc(sizeof((**stack).elem_size));
    if (node->data == NULL) {
        return FAILURE;
    }
    memcpy(node->data, data, (**stack).elem_size);

    node->lower = (**stack).top;
    (**stack).top = node;
    (**stack).stack_size += 1;
    return SUCCESS;
}

enum status pop(stack_struct **stack, void *data)
{
    if ((**stack).top == NULL) {
        return FAILURE;
    }
    stack_node *node = (**stack).top;
    memcpy(data, node->data, (**stack).elem_size);
    (**stack).top = node->lower;

    free(node->data);
    free(node);

    (**stack).stack_size -= 1;
    return SUCCESS;
}

enum status peek(stack_struct **stack, void *data)
{
    if ((**stack).top == NULL) {
        return FAILURE;
    }
    memcpy(data, (**stack).top->data, (**stack).elem_size);
    return SUCCESS;
}

void stack_delete(stack_struct **stack)
{
    while ((**stack).top != NULL)
    {
        stack_node *node = (**stack).top;
        (**stack).top = (**stack).top->lower;
        free(node->data);
        free(node);
    }
    free(*stack);
}

int main(void)
{
    enum action choice;
    stack_struct *stack = malloc(sizeof(stack_struct));
    if (stack == NULL)
    {
        printf("Not enough memory\n");
        return 1;
    }
    stack_create(&stack, sizeof(int));

    while ((choice = get_user_action()) != QUIT) {
        clear_screen();
        int data;
        switch (choice) {

            case PUSH:
                printf("Enter data to be pushed -> ");
                scanf("%d", &data);
                if (push(&stack, &data) == SUCCESS) {
                    printf("%d pushed onto the stack\n", *(int *)stack->top->data);
                } else {
                    printf("Not enough memory\n");
                }
                break;

            case POP:
                if (pop(&stack, &data) == SUCCESS){
                    printf("The data is %d\n", data);
                } else {
                    printf("Stack underflow\n");
                }
                break;

            case TOP:
                if (peek(&stack, &data) == SUCCESS){
                    printf("The data at top is %d\n", data);
                } else {
                    printf("Nothing in the stack\n");
                }
                break;

            case LENGTH:
                printf("Length is %d\n", stack->stack_size);
                break;

            default:
                assert(!"You should not have reached this.\n");

        }
        getchar();
        getchar();
    }
    stack_delete(&stack);
}
