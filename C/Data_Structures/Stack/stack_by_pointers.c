#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

enum action {START, PUSH, POP, TOP, QUIT, END};

typedef struct node
{
    int data;
    struct node *lower;

}stack_node;

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

void push(stack_node **top_stack, int *status, int data)
{
    *status = START;
    stack_node *node = malloc(sizeof(node));
    if (node == NULL)
    {
        *status = PUSH;
        return;
    }

    node -> data = data;
    if (*top_stack == NULL){
        node -> lower = NULL;
    }
    else{
        node -> lower = *top_stack;
    }
    *top_stack = node;
}

int pop(stack_node **top_stack, int *status)
{
    *status = START;
    if (*top_stack == NULL){
        *status = POP;
        return -1;
    }

    stack_node *node = *top_stack;
    int data = node -> data;
    *top_stack = node -> lower;
    free(node);

    return data;
}

int peek(stack_node **top_stack, int *status)
{
    *status = START;
    if (*top_stack == NULL){
        *status = POP;
        return -1;
    }

    return (*top_stack) -> data;
}

int main(void)
{
    enum action choice;
    int status;
    stack_node *top = NULL;

    while ((choice = get_user_action()) != QUIT)
    {
        clear_screen();
        int data;
        switch (choice)
        {
        case PUSH:
            printf("Enter data to be pushed -> ");
            scanf("%d", &data);
            push(&top, &status, data);
            if (status == PUSH){
                printf("Not enough memory\n");
            }
            else{
                printf("%d pushed onto the stack", data);
            }
            break;
			
        case POP:
            data = pop(&top, &status);
            if (status == POP){
                printf("Stack underflow\n");
            }
            else{
                printf("The data is %d\n", data);
            }
            break;
			
        case TOP:
            data = peek(&top, &status);
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
        getchar();
        getchar();
    }
}
