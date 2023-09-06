#include<stdio.h>
void main(){
	int num, flag = 1;
    scanf("%d", &num);
    for(int i = 2; i < num; i++){
        if(num % i == 0){
            flag = 0;
            break;
        }
    }
    if(flag == 0){
        printf("Not prime");
    }
    else{
        printf("Prime");
    }
} 