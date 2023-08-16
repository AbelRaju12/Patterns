#include <stdio.h>
int main()
{
    char str1[256], str2[256],c;
    int count = 0;
    printf("Enter the first string : ");
    scanf("%[^\n]%c",str1,&c);
    printf("Enter the second string : ");
    scanf("%[^\n]%c",str2,&c);
    for(int i = 0; str1[i] != '\0'; i++){
        count++;
    }
    for(int j = 0; str2[j] != '\0'; j++){
        str1[count] = str2[j];
        count++;
    }
    printf("%s",str1);    
    return 0;
}