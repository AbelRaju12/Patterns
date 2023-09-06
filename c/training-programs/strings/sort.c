#include <stdio.h>
int main()
{
    char str[256], c, temp;
    int count = 0;
    printf("Enter the string : ");
    scanf("%[^\n]%c",str,&c);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++){
        for(int j = i + 1; j < count;j++){
            if(str[i] > str[j]){
                temp = str[i];
                str[i] = str[j];
                str[j] = temp;
            }
        }
    }
    printf("String after sorting = %s",str);
    return 0;
}