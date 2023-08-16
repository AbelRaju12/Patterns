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
    for(int i = 0; i < 256; i++){
        if(freq[i] == 1){
            printf("%c ", i);
        }
    }
    return 0;
}