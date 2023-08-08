// 01110
// 10001
// 10001
// 10001
// 01110
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num; j++){
            if((i == 1 || i == num) && (j == num || j == 1)){
                printf("0 ");
            }
            else if(i == 1 || j == 1 || i == num || j == num){
                printf("1 ");
            }
            else{
                printf("0 ");
            }
        }
        printf("\n");
    }
}