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
    }
    // for(int i = 0; i < n; i++){
    //     for(int j = i + 1; j < n;j++){
    //         if(arr[i] == arr[j]){
    //             for(int k = j; k < n; k++){
    //                 arr[k] = arr[k+1];
    //             }
    //             n--;
    //             j--;
    //         }
    //     }
    // }
    // for(int i = 0; i < n; i++){
    //     printf("%d ", arr[i]);
    // }
     for(int i = 0; i < n; i++){
        occ[arr[i]]++;
        if(occ[arr[i]] == 1){
            printf("%d ",arr[i]);
        }
    }
    return 0;
}