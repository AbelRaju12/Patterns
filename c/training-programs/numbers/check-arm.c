#include<stdio.h>
#include<math.h>
#include<conio.h>
void main(){
	int num, original, count = 0, digit, temp = 0, pow = 1;
    scanf("%d", &num);
    original = num;
    while(num > 0){
        num = num / 10;
        count++;
    }
    num = original;
    while(num > 0){
        digit = num % 10;
        pow = 1;
        for(int i = 0; i < count; i++){
            pow = pow * digit;
        }
        temp = temp + pow;
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