#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum status {STACK_SUCCESS, STACK_FAILURE};

typedef struct node {
    void *data;
    struct node *lower;
} stack_node;

typedef struct stack {
    size_t elem_size;
    size_t stack_size;
    stack_node *top;
} STACK;

enum status stack_init(STACK *stack, size_t elem_size)
{
    stack->elem_size = elem_size;
    stack->stack_size = 0;
    stack->top = NULL;
    return STACK_SUCCESS;
}

stack_node * stack_node_create(STACK *stack)
{
    stack_node *node = malloc(sizeof(stack_node));
    if (node == NULL) {
        return NULL;
    }
    node->data = malloc(stack->elem_size);
    if (node->data == NULL) {
        free(node);
        return NULL;
    }
    return node;
}

enum status stack_push(STACK *stack, void *data)
{
    stack_node *node = stack_node_create(stack);
    if (node == NULL) {
        return STACK_FAILURE;
    }

    memcpy(node->data, data, stack->elem_size);

    node->lower = stack->top;
    stack->top = node;
    stack->stack_size += 1;
    return STACK_SUCCESS;
}

enum status stack_pop(STACK *stack, void *data)
{
    if (stack->top == NULL) {
        return STACK_FAILURE;
    }
    stack_node *node = stack->top;
    memcpy(data, node->data, stack->elem_size);
    stack->top = node->lower;

    free(node->data);
    free(node);

    stack->stack_size -= 1;
    return STACK_SUCCESS;
}

enum status stack_peek(STACK *stack, void *data)
{
    if (stack->top == NULL) {
        return STACK_FAILURE;
    }
    memcpy(data, stack->top->data, stack->elem_size);
    return STACK_SUCCESS;
}

void stack_cleanup(STACK *stack)
{
    while (stack->top != NULL) {
        stack_node *node = stack->top;
        stack->top = stack->top->lower;
        free(node->data);
        free(node);
    }
}

//Stack Implementation before this.
//Things that are used to use the stack are placed after this.
enum action {START, PUSH, POP, TOP, LENGTH, QUIT, END};

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

int main(void)
{
    enum action choice;
    STACK stack;
    stack_init(&stack, sizeof(int));

    while ((choice = get_user_action()) != QUIT) {
        clear_screen();
        int data;
        switch (choice) {

            case PUSH:
                printf("Enter data to be pushed -> ");
                scanf("%d", &data);
                if (stack_push(&stack, &data) == STACK_SUCCESS) {
                    printf("%d pushed onto the stack\n", *(int *)stack.top->data);
                } else {
                    printf("Not enough memory\n");
                }
                break;

            case POP:
                if (stack_pop(&stack, &data) == STACK_SUCCESS){
                    printf("The data is %d\n", data);
                } else {
                    printf("Stack underflow\n");
                }
                break;

            case TOP:
                if (stack_peek(&stack, &data) == STACK_SUCCESS){
                    printf("The data at top is %d\n", data);
                } else {
                    printf("Nothing in the stack\n");
                }
                break;

            case LENGTH:
                printf("Length is %d\n", stack.stack_size);
                break;

            default:
                assert(!"You should not have reached this.\n");

        }
        getchar();
        getchar();
    }
    stack_cleanup(&stack);
}
