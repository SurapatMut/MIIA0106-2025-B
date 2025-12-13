#include <iostream>
#include <string>

using namespace std;

int main()
{
	cout << "start \n";
	int l = 2;
	do 
	{
		cout << "\n" << l << endl;
		l= l+2; // l= l+2; l +=2;
	} while (l < 21);
	return 1;
}