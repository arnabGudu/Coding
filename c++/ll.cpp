#include<stdio.h>

struct node
{
	int data;
	node* next;
};

void insert(node* last, data)
{
	node* temp = new node;
	last->next = temp;
	last->data = data;
	last->next = NULL;
}
