#include <stdio.h>
int gcd(int num1, int num2)
{
    if (num2 == 0)
        return num1;
    return gcd(num2, num1 % num2);
}
 
int main()
{
    int num1, num2, maxNum;
    printf("Find GCD or HCF of two numbers using recursion\n");
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    printf("GCD or HCF of numbers %d and %d is %d ", num1, num2, gcd(num1, num2));
    return 0;
}