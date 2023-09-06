#include <stdio.h>
#include <stdlib.h>

// Creating a node
struct node {
  int data;
  struct node *next;
};
struct node* createnode(int data, struct node* nextnode){
    struct node* temp = (struct node*)malloc(sizeof(struct node));
    temp->data = data;
    temp->next = nextnode;
    return temp;
}

int main() {
  // Initialize nodes
  struct node *head = 0, *ptr;
  struct node *next = (struct node *)malloc(sizeof(struct node));
  int values[] = {100,200,300,400,500};
  int n = 5;
  for(int i=n-1;i>=0;i--)
	{
		ptr    = createnode(values[i],ptr);
		head = ptr;
	}
	
	//printing LinkedList
	while(ptr->next != NULL)
	{
		printf("%d ",ptr->data);
		ptr = ptr->next;
	}


}