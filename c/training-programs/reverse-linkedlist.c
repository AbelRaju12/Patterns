#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

void insert(struct Node** head, int data){
    struct Node* newNode = (struct Node*)malloc(sizeof(struct  Node));
    newNode->data = data;
    newNode->next = *head;
    *head = newNode;
}

void reverse(struct Node** head){
    struct Node* prev = NULL;
    struct Node* current = *head;
    struct Node* next = NULL;

    while(current != NULL){
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;

}

void printlist(struct Node* head){
    while(head != NULL){
        printf("%d-->", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

int main(){
    struct Node* head = NULL;
    insert(&head, 2);
    insert(&head, 4);
    insert(&head, 9);
    insert(&head, 3);
    insert(&head, 7);

    printf("Original list\n------------\n");
    printlist(head);

    reverse(&head);

    printf("\nReversed list\n------------\n");
    printlist(head);

    return 0;
}