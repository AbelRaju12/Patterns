#include<stdio.h>
#include<conio.h>
int main() {
   int num1, num2, i;
    printf("please enter first number: ");
    scanf("%d",&num1);
    printf("please enter second number: ");
    scanf("%d",&num2);
    if(num2 > num1){
        for(i=1;i<=num2;i++){
            num1++;
        }
        printf("sum = %d", num2);
    }
    else{
        for(i=1;i<=num1;i++){
            num2++;
        }
        printf("sum = %d", num2);
    }

    getch();
} 
