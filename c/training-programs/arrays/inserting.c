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
    printf("Enter value and location\n");
    scanf("%d", &val);
    scanf("%d", &loc);
    for(int i = n - 1; i >= loc - 1; i--){
        a[i + 1]= a[i];
    }
    a[loc - 1] = val;
    for(int i = 0; i <= n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}