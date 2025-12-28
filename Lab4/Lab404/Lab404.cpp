#include <iostream>
using namespace std;	

int main()
{
	int number = 21;
	cout << " Multiplication Table of " << number << "\n";
	for (int i = 1; i <= 12; i++)
	{
		cout << number << " x " << i << " = " << number * i << "\n";
	}
	return 0;
}