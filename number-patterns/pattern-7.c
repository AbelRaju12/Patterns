//12345
//1234
//123
//12
//1
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        k = 1;
        for(int j = 1; j <= num - i + 1; j++){
            // k = k + 2;
            // printf("%d ", (k - 2));
            printf("%d ", j);            
        }
        printf("\n");
    }
    return 0;
}