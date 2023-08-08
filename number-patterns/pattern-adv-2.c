// 12345
// 23456
// 34567
// 45678
// 56789
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = i; j < i + num; j++){
            printf("%d ", j);
        }
        printf("\n");
    }
}