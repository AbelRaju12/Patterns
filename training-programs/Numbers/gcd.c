#include <stdio.h>
int main()
{
    int num1, num2, i, gcd;
    printf("Program to find HCF or GCD of two numbers\n");
    printf("Enter the first number: ");
    scanf("%d", &num1);
    printf("Enter the second number: ");
    scanf("%d", &num2);
    for(i=1; i <= num1 && i <= num2; ++i)
    {
        if(num1%i==0 && num2%i==0)
            gcd = i;
    }
    printf("G.C.D of number %d and %d is %d", num1, num2, gcd);
    return 0;
}