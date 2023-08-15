#include <stdio.h>
#include <string.h>

int occ(char *str, char ch){
    int count = 0;
    for(int i = 0;i < strlen(str); i++){
        if(str[i] == ch){
            count++;
        }
    }
    return count;
}

void main()
{
	int count;
	char str[100], ch;
	printf("Enter a string: ");
	fgets(str, 100, stdin);
	printf("Enter a character you want to count: ");
	scanf("%c", &ch);
	count = occ(str, ch);
	printf("total occurence of '%c': %d", ch, count);
}