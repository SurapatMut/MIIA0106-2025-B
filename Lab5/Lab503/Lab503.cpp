#include <iostream>
#include <string>

using namespace std;

void swapvalues(int a, int b)
{
	int tmp;
	tmp = a;
	a = b;
	b = tmp;
	cout << "Inside swapvalues function: " << endl;
	cout << "a = " << a << " b = " << b << endl;

}

void swapRef(int &a, int &b)
{
	int tmp;
	tmp = a;
	a = b;
	b = tmp;
	cout << "Inside swapvalues function: " << endl;
	cout << "a = " << a << " b = " << b << endl;

}

int main()
{
	int a, b;
	cout << "Enter a integer: ";
	cin >> a;
	cout << "Enter b integer: ";
	cin >> b;
	cout << "Before swapvalues function: " << endl;
	cout << "a = " << a << " b = " << b << endl;
	swapvalues(a, b);
	cout << "a = " << a << " b = " << b << endl; 

	swapRef(a, b);
	cout << "a = " << a << " b = " << b << endl;
    
	
	return 1;
}