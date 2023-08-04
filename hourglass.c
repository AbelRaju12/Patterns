#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j < i; j++){
            printf(" ");
        }
        for(int k = i; k <= num; k++){
            printf("* ");
        }
        printf("\n");
    }
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num - i; j++){
            printf(" ");
        }
        for(int k = 1; k <= i; k++){
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}