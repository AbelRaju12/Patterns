#include <stdio.h>
int main(){
    int n, val, loc;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter elements\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    printf("Enter index\n");
    // val = a[n-1]
    // n = n - 1
    scanf("%d", &loc);
    for(int i = loc; i < n - 1; i++){
        a[i]= a[i + 1];
    }
    n--;
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}

// for(int i = 0; i < n; i++){
//         if(a[i] == val){
//             for( int j = i; j < n - 1; j++){
//                 a[j] = a[j + 1];
//             }
//             n--;
//             i--;
//         }
//     }