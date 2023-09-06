#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = i; j < num;j++){ //num-i+1
            printf(" ");
        }
        for(int k = 1; k <= i; k++){
            // if(k == i || k == 1 || i == num)
            //     printf("*");
            // else
            //     printf(" ");
            printf("*");
        }
        printf("\n");
    }
    return 0;
}