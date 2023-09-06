// 12345
// 23455
// 34555
// 45555
// 55555
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = i; j <= num; j++){      
            printf("%d ", j);
        }
        for(int k = 1; k < i; k++){
            printf("%d ", num);
        }
        printf("\n");
    }
}