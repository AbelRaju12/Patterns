// 1111111
// 0000000
// 1111111
// 0000000
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= 5; i++){
        for(int j = 1; j <= 5; j++){
            if( i % 2 == 1){
                printf("1 ");
            }
            else
                printf("0 ");
        }
        printf("\n");
    }
    return 0;
}