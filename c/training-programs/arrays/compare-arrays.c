#include<stdio.h>
int main(){
    int n, flag = 0, j;
    printf("Enter the size of the arrays: ");
    scanf("%d", &n);
    int arr1[n], arr2[n];
    printf("Enter elements for array 1\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr1[i]);
    }
    printf("Enter elements for array 2\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &arr2[i]);
    }
    for(int i = 0; i < n; i++){
        for(j = 0; j < n; j++){
            if(arr1[i] == arr2[j]){
                break;
            }
            else{
                continue;
            }
        }
        if(j == n){
            printf("%d is not present in the second array\n", arr1[i]);
        }
    }
    return 0;
}

    // int arr1[]={1,2,5,3,4,5};
    // int arr2[]={2,3,1,9,5};
    // int size1=sizeof(arr1)/sizeof(arr1[0]);
    // int size2=sizeof(arr2)/sizeof(arr2[0]);
    // if(size1 == size2){
    //     printf("size of both arrays are equal");
    // }else{
    //     printf("size of arrays are not equal");
    // }