// 55555
// 54444
// 54333
// 54322
// 54321
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = num; j > num - i; j--){      
            printf("%d ", j);
        }
        for(int k = 1; k <= num - i; k++){
            printf("%d ", num - i + 1);
        }
        printf("\n");
    }
}