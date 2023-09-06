#include <stdio.h>
// #include <string.h>
int main(){
    char str[20];
    int count = 0;
    scanf("%[^\n]", str);
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    for(int i = 0; i < count; i++)
    {
        if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u'||str[i]=='A'||str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
        {
            for(int j = i; j < count; j++)
            {
                str[j]=str[j+1];
            }
            i--;
            count--;
        }
    }
    printf("\nAfter deleting the vowels string is : %s",str);
    return 0;
}