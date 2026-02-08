#include <iostream>
#include <string>

using namespace std;

int main()
{
	int count, num;
	num = 0;
	for (count = 1; count < 100; count++)
	{
		if (count % 2 != 0) {
			count = num + count;
		}
	}
	cout << count; 
		return 0;
	
} 