#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j < num - i + 1; j++){ // j < i for inverted rhombus or use j = i to num
            printf(" ");
        }
        for(int k = 1; k <= num; k++){
            // printf("* "); for full rhombus
            if( i == 1 || k == 1 || i == num || k == num){
                printf("* ");
            }
            else{
                printf("  ");
            }
        }        
    printf("\n");
    }
    return 0;
}