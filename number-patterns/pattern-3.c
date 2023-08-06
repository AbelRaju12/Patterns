// 10101
// 01010
// 10101
// 01010
// 10101
#include <stdio.h>
int main(){
    int num, num2;
    scanf("%d%d", &num, &num2);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= num2; j++){
            if( (i + j) % 2 == 0){
                printf("1 ");
            }
            else{
                printf("0 ");
            }
        }
        printf("\n");
    }
    return 0;
}
