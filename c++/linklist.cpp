#include<stdio.h>

struct Node
{
	int data;
	Node* next;
};

void insert(Node*, int);

int main()
{
	int n, i;
	printf("enter no of items");
	scanf("%d", &n);

	Node* first = NULL;
	
	printf("state1 %d \n",n);

	for (i = 0; i < n; i++)
	{
		printf("state4\n");
		insert(first, i + 1);
		printf("%d\n", first->data);
	}

	printf("state2\n");

	int sum = 0;
	while(first->next != NULL)
	{
		sum += first->data;
		printf("%d", first->data);
	}
	

	return 0;
}

void insert(Node* first, int data)
{
	printf("insert1\n");
	if (first == NULL)
	{
		Node* temp = new Node;
		temp->data = data;
		temp->next = NULL;
		first = temp;

		printf("%d\n", first->data);
	}
	else
	{
		Node* temp = first;
		while(temp->next != NULL)
		{
			temp = temp->next;
		}
		Node* n = new Node;
		temp->next = n;
		n->data = data;
		n->next = NULL;

	}

	printf("state3\n");
}




