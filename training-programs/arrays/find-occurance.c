#include<stdio.h>
int main(){
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int arr[n];
    int occ[100] = {0};
    printf("Enter elements\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        occ[arr[i]]++;
    }
    for(int i = 0; i < n; i++){
        printf("%d occurs %d times\n", i + 1, occ[i]);
    }
    return 0;
}