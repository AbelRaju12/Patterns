// 11111
// 11111
// 11011
// 11111
// 11111
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            if(i == j && i == num / 2 + 1){
                printf("0 ");
            }
            else{
                printf("1 ");
            }
        }
        printf("\n");
    }
}