#include <stdio.h>
void main(){
    int n;
    printf("Enter the size of the array: ");
    scanf("%d", &n);
    int a[n];
    int freq[256] = {0};
    printf("Enter elements\n");
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
        freq[a[i]]++;
    }
    int max = 0, max_element;
    for(int i = 0; i < n; i++){
        if(freq[a[i]] > max){
            max = freq[a[i]];
            max_element = a[i];
        }        
    }
    printf("%d has highest frequency and occurs %d times", max_element, max);
}