#include<stdio.h>
#include<math.h>
#include<conio.h>
void main(){
	int num, original, count = 0, digit, temp = 0;
    scanf("%d", &num);
    original = num;
    while(num > 0){
        num = num / 10;
        count++;
    }
    num = original;
    while(num > 0){
        digit = num % 10;
        temp = temp + pow(digit, count);
        num = num / 10;
    }
    if(temp == original){
        printf("It is an armstrong");
    }
    else{
        printf("Its not an armstrong");
    }
    getch();
} 