// 1
// 3 2
// 3 5 4 3
// 4 5 7 6 5 4
// 5 6 7 9 8 7 6 5
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        k = i;
        for(int j = 3; j <= i; j++){
            printf("%d ",k);
            k++;
        }        
        for(int j = i * 2 - 1; j >= i; j--){
            printf("%d ",j);
        }
        printf("\n");
    }
    return 0;
}