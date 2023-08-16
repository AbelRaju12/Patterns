#include <stdio.h>
// #include <string.h>
int main(){
    char str1[20], str2[20], ch;
    int count = 0, i;
    scanf("%[^\n]%c", str1, &ch);
    printf("str1 = %s\n", str1);
    for(int i = 0; str1[i] != '\0'; i++){
        count++;
    }
    for(i = 0; i < 256; i++){
        str2[i] = str1[i];        
    }
    str2[i] = '\0';
    printf("After copying, str2 = %s", str2);
    return 0;
}