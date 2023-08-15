#include<stdio.h>
#include<conio.h>
void main() {
  int rem, sum = 0, i, num;
  printf("please enter number: ");
  scanf("%d", &num);
  for (i = 1; i <= num / 2; i++) {
    rem = num % i;
    if (rem == 0) {
      sum = sum + i;
    }
  }
  if (sum == num)
    printf("given no. is perfect number");
  else
    printf("given no. is not a perfect number");
  getch();
}