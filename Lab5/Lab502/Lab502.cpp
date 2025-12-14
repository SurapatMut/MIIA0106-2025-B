#include <iostream>
#include <string>

using namespace std;

int maxOfthree(int a, int b, int c)
{
	if (a >= b && a >= c)
		return a;
	else if (b >= a && b >= c)
		return b;
	else
		return c;
}

int minofthree(int a, int b, int c)
{
	if (a <= b && a <= c)
		return a;
	else if (b <= a && b <= c)
		return b;
	else
		return c;
}

int main()
{
	int a, b, C;
	int maxvalue = 100000000;
	int minvalue = -100000000;

	cout << "Enter a integer: ";
	cin >> a;
	cout << "Enter b integer: ";
	cin >> b;
	cout << "Enter C integer: ";
	cin >> C;

	maxvalue = maxOfthree(a, b, C);
	cout << "The maximum value is: " << maxvalue << endl;
	
	minvalue = minofthree(a, b, C);
	cout << "The minimum value is: " << minvalue << endl;


	return 1;
}