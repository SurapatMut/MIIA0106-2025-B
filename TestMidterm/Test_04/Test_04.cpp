#include <iostream>
#include <string>
using namespace std;	

int main()
{
	const int N = 5;
	int id[N];
	//TODO
	for (int i = 0; i < N; i ++)
	{
		cout << "Student ID" << (i + 1) << " : ";
		cin >> id[i];
	}
	//TODO
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = 0; j < N - 1 - i; j++)
		{
			if (id[j] < id[j + 1])
			{
				int temp = id[j];
				id[j] = id[j + 1];
				id[j + 1] = temp;
			}
		}
	}
	//TODO
	for (int i = 0; i < N; i++)
	{
		cout << "Student ID" << (i + 1) << " : " << id[i] << endl;
	}
}