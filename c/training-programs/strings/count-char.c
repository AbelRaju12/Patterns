#include <stdio.h>
#include <string.h>
void main()
{
	char str[100], ch;
	printf("Enter a string: ");
	fgets(str, 100, stdin);
	printf("Enter a character you want to count: ");
	scanf("%c", &ch);
	int count = 0;
    for(int i = 0;i < strlen(str); i++){
        if(str[i] == ch){
            count++;
        }
    }
	printf("total occurence of '%c': %d", ch, count);
}