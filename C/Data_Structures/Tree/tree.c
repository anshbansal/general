#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum action {START, TRAVERSE, QUIT, END};

typedef struct node {
    int data;
    struct node *father;
    struct node *right;
    struct node *left;
} tree_node;

tree_node * make_node(int data) {
    return &(tree_node){.data = data};
}

bool isleft(tree_node *n) {

}


//Utility functions after this
void clear_screen(void)
{
    system("cls");
}

static enum action get_user_action(void)
{
    int choice = START;
    do {
        clear_screen();
        printf("%d Traverse\n"
               "%d Exit\n\n"
               "Enter your choice -> ", TRAVERSE, QUIT);
        scanf("%d", &choice);
    } while (!(START < choice && choice < END));
    return (enum action) choice;
}

int main() {
    tree_node *root = make_node();
    enum action choice;
    while ((choice = get_user_action()) != QUIT) {
        clear_screen();
        int data;
        switch (choice) {

            case TRAVERSE:
                printf("In traverse");
                break;

            default:
                assert(!"You should not have reached this.\n");

        }
        getchar();
        getchar();
    }
    return 0;
}
