// 1
// 1 2 3
// 1 2 3 4 5
// 1 2 3 4 5 6 7
// 1 2 3 4 5 6 7 8 9
#include <stdio.h>
int main(){
    int num;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= i * 2 - 1; j++){       // for odd nup.s i*2-1 for even i*2
            printf("%d ",j);
        }
        
        printf("\n");
    }
    return 0;
}