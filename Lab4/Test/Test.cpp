#include <iostream>
#include <string>

using namespace std;

int main()
{
	int a = 10;
	do
	{
		cout << "\n" << a << endl;
		a = a - 2; //a = a-2; a -=2;
	} while (a > 1);
	
	return 1; 
}