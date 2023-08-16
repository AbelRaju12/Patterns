#include <stdio.h>
// #include <string.h>
int main(){
    char str[20];
    int count = 0, vowel = 0, consonant = 0;
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++){
        if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
        {
            vowel++;
        } else if((str[i]>=65 && str[i]<=90)|| (str[i]>=97 && str[i]<=122)) {
            consonant++;
        }
    }
    printf("Total number of vowels are : %d and Consonants are : %d",vowel,consonant);
    return 0;
}