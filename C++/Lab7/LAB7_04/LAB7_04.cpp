// TODO: แสดงค่าทุกตัวใน array โดยใช้ pointer เท่านั้น
#include <iostream>
using namespace std;

int main() {
    int arr[] = { 10, 20, 30, 40 };
    int* p = arr;

    // TODO
	cout << "Array elements using pointer:" << endl;
	for (int i = 0; i < 4; i++) 
	{
		cout << *(p + i) << endl;
	}
    return 0;
}