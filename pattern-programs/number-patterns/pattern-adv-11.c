// 1 
// 2 3
// 4 5 6 7
// 8 9 10 11 12 13 14 15
// 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
#include <stdio.h>
int main(){
    int num, k = 1, count = 1;
    scanf("%d", &num);
    for(int i = 1; i <= num; i++){
        for(int j = 1; j <= count; j++){       // for odd nup.s i*2-1 for even i*2
            printf("%d ",k);
            k++;
        }
        count = count * 2;        
        printf("\n");
    }
    return 0;
}