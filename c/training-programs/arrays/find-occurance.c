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
    int element;
    printf("Enter the element: ");
    scanf("%d", &element);
    printf("%d occurs %d times", element, occ[element]);
    return 0;
}