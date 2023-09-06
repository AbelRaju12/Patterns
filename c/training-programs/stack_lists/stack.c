#include<stdio.h>
#include<stdlib.h>
#define n 10
int stack[n];
int top = -1;
void push(){
    printf("Enter the element to be pushed: ");
    int element;
    scanf("%d", &element);
    if(top != n - 1){
        top = top + 1;
        stack[top] = element;
    }
    else{
        printf("Overflow...!\n");
    }
}
void pop(){
    int item;
    if(top != -1){
        printf("%d has been popped\n", stack[top]);
        stack[top--];
    }
    else{
        printf("Underflow...!\n");
    }
}
void peek(){
    int item;
    item = stack[top];
    if(top == -1)
        printf("stack is empty!!\n");
    else
        printf("%d\n", item);
}
void display(){
    for(int i = top; i >= 0; i--){
        printf("%d\n", stack[i]);
    }
}

void main(){
    while(1){
        int N;
        printf("enter a choice: ");
        scanf("%d", &N);
        switch (N)
        {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            default:
                exit(0);
                break;
        }
    }
}