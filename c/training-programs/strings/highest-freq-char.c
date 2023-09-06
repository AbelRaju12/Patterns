#include <stdio.h>
// #include <string.h>
int main(){
    char str[20];
    char ch;
    int count = 0, max = 0;
    int freq[256] = {0};
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
        freq[str[i]]++;
    }
    for(int i = 0; i < count; i++){
        if(max <= freq[str[i]]){
            max = freq[str[i]];
            ch = str[i];
        }
    }
    printf("\n Maximum Occurring Character in a String %s is '%c'  %d times", str, ch, max);
    return 0;
}