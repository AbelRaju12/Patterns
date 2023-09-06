// 11011
// 11011
// 00000
// 11011
// 11011
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            if(j == num / 2 + 1 || i == num / 2 + 1){
                printf("0 ");
            }
            else{
                printf("1 ");
            }
        }
        printf("\n");
    }
}