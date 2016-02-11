#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
	int input;
	cout<<"enter input : ";
	cin>>input;
	int left = input >> 3;
	int right = input ^ left << 3;
	cout<<input<<"\t"<<left<<"\t"<<right<<endl;


	int x = (right >> 0 & 1) ^ (right >> 2 & 1);
	x = (x << 0) | (x << 2); 
	cout<<(right ^ x)<<endl;

	return 0;
}

/*
001100
1

*/
