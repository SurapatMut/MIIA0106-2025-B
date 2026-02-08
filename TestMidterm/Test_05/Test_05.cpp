#include <iostream>
#include <string>
using namespace std;	

void swapVlaue(int* x, int* y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}
int main() {
	int a, b;
	cin >> a >> b;
	swapVlaue(&a, &b);
	cout << a << " " << b;
 
	return 0;
}