#include <iostream>
#include <string>

using namespace std;

int main()
{
	for (int i = 1;
		i < 11;
		i++)
	{
		cout  << "\n " << i << "\n";
	}

	cout << "------Start While------ \n";
	int j = 1;
	while (j < 11)
	{
		cout << " \n " << j << endl;
		j++; // j= j+1; j +=1;
	}

	cout << "------Start Do While----- \n";
	int k = 1;
	do
	{
		cout << "\n " << k << "\n";
		k++; // j= j+1; j +=1;

	} while (k < 11);

	return 1;
}