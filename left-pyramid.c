#include <stdio.h>

int main(){
    int num;
    char ch[100];
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= i; j++){
            // if(j == i || i == num || j == 1){
            //     printf("* ");
            // }
            // else{
            //     printf("  ");
            // }
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}