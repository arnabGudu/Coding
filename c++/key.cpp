#include<stdio.h>
#include<conio.h>

int main()
{
	while(true)
	{
		char c = getch();
		printf("%c", c);
		if (c == ' ')
			break;
	}
}
