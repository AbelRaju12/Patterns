#include<stdio.h>
int sum(int a){
    if( a == 0){
        return 0;
    }
    return sum (a / 10) + a % 10;
}
int main()
{
    int a, result;
    printf("Enter the number:\n");
    scanf("%d", &a);
    result = sum(a);
    printf("Sum of dgits is: %d\n", result);
    return 0;
}