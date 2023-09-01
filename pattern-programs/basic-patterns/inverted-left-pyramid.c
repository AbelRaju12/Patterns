#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num - i + 1; j++){
            // if(i == 1 || j == 1 || j == num - i + 1){
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