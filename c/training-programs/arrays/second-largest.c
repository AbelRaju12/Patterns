#include <stdio.h>
int main(){
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter elements\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    int max = a[0];
    int second_max = a[0];
    for(int i = 1; i < n; i++){
        if(a[i] > max){
            second_max = max;
            max = a[i];
        }
    }
    // int second_max = a[0];
    // for(int i = 1; i < n; i++){
    //     if(a[i] > second_max && a[i] != max){
    //         second_max = a[i];
    //     }
    // }
    printf("second largest element is %d", second_max);
}