// 1
// 2 1
// 1 2 3
// 4 3 2 1
// 1 2 3 4 5
#include <stdio.h>
int main(){
    int num, k;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        if(i % 2 == 0){
            k = i;
            for(int j = 1; j <= i; j++){
                printf("%d ", k);
                k--;
            }
        }
        else{
            k = 1;
            for(int j = 1; j <= i; j++){
                printf("%d ", k);
                k++;
            }

        }
        printf("\n");
    }
    return 0;
}