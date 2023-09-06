#include<stdio.h>
int sum(int a, int b){
    if( b == 0){
        return a;
    }
    return sum(a, b - 1) + 1;
}
int main()
{
    int a, b, result;
    printf("C Program to add two number using recursion \n");
    printf("Enter the first number:\n");
    scanf("%d", &a);
    printf("Enter the second number:\n");
    scanf("%d", &b);
    result = sum(a, b);
    printf("Sum of two numbers is: %d\n", result);
    return 0;
}